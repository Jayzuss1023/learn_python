with open("story.txt", "r") as f:
    story = f.read()

# Take a txt file where the user can create there own story 
# by replacing the <words> located in the file
words = set()
answers = {}
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1


for word in words:
    answer = input("Select a word for " + word + " : ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])
