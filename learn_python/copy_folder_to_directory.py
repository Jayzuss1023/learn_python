import os
import shutil
import datetime
import time
import schedule

source_dir = "/Users/jesusflores/desktop/webdev"
destination_dir = "/Users/jesusflores/desktop/property"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    # Creating a new directory "property/todaysDate"
    dest_dir = os.path.join(dest, str(today))

    try:
        # Copies everything inside of the folder 
        # From source directory into destination directory
        shutil.copytree(source, dest_dir)
        print(f"Your file has been created on {dest_dir}")
    except:
        print(f"Folder already exists in {dest_dir}")


# Schedule a new download everyday at a given time
# Without lambda function - parameters are unable to be passed
# schedule.every().day.at("6:55").do(copy_folder_to_directory)
# lambda function needed since our function requires parameters
# lamba is a function that calls another funciton
schedule.every().day.at("22:40").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

while True:
    # run_pending looks for every pending task that has been scheduled but has not yet been ran
    schedule.run_pending()
    time.sleep(60)