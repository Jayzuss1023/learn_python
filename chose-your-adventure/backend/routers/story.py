import uuid
from typing import Optional
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Cookie, Response, BackgroundTasks
from sqlalchemy.orm import Session

from db.database import get_db, SessionLocal
from models.story import Story, StoryNode
from models.job import StoryJob
from schemas.story import (
    CompleteStoryResponse, CreateStoryRequest
)
from schemas.job import StoryJobResponse
# from core.story_generator import StoryGenerator

router = APIRouter(
    prefix="/stories",
    tags=["stories"]
)

def get_session_id(session_id: Optional[str] = Cookie(None)):
    if not session_id:
        session_id = str(uuid.uuid4())
    return session_id

@router.post("/create", response_model=StoryJobResponse)
def create_story(
    request: CreateStoryRequest, # passed params
    background_tasks: BackgroundTasks, # Task to run independently
    response: Response,
    session_id: str = Depends(get_session_id),
    db: Session = Depends(get_db)
):
    response.set_cookie(key="session_id", value=session_id, httponly=True)

    job_id = str(uuid.uuid4())

    # Create new job
    job = StoryJob(
        job_id=job_id,
        session_id=session_id,
        theme=request.theme,
        status="pending"
    )
    db.add(job)
    db.commit()

    # TODO: add background task.
    # Background task will run asyncronously along with create_story
    background_tasks.add_task(
        generate_story_task,
        job_id=job_id,
        theme=job.theme,
        session_id=session_id
    )

    return job

def generate_story_task(job_id: str, theme: str, session_id: str):
    # Necessary for create_story and generate_story_task to run async
    db = SessionLocal()

    # Locate job and update status or fail
    job = db.query(StoryJob).filter(StoryJob.job_id == job_id).first()

    if not job:
        return

    try:
        job.status = "processing"
        db.commit()
        
        story = {} # todo: generate story

        job.story_id = 1 #todo: update story_id
        job.status = "complete"
        job.completed_at = datetime.now()
        db.commit()

    except Exception as e:
        job.status = "failed"
        job.completed_at = datetime.now()
        job.error = str(e)
        db.commit()
    finally:
        db.close()

@router.get("/{story_id}/complete", response_model=CompleteStoryResponse)
def get_complete_story(story_id: int, db: Session = Depends(get_db)):
    story = db.query(Story).filter(Story.id == story_id).first()
    if not story:
        raise HTTPException(status_code=404, detail="Story not found")
    
    build_complete_story(db, story)
    return build_complete_story


def build_complete_story(db: Session, story: Story):
    pass