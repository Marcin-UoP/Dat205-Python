# Knights to was "ni" video reference
# https://www.youtube.com/watch?v=zIV4poUZAQo

file = open("stop-words.txt")
stopwords = file.readlines()

for word in stopwords:
    next = word.strip()
    print(next)

while True:
    input = raw_input("Say something interesting: ")
    filtered = input.replace(" ni ", " <beep> ")
    print("Your filtered text was: " + filtered)