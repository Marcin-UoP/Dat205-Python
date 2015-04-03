
# loads and reads all words from txt file
file = open("stop-words.txt") 
stopwords = file.readlines()
stopwords = []

for word in stopwords:
    stopwords.append(word.strip())

# function that formulates the question 
def formulate(sentence): 
    input = raw_input(sentence + " ")
    words = input.split(' ')
    for word in words:
        if word in stopwords:
            print "stopword: " + word
            words.remove(word)
    return ' '.join(words)

user = {} 

# Ask for nick name
nickNameInput = formulate("Hey bro, I'm a chat bot, please tell me your nick name")
nickName = nickNameInput.split(' ')[-1]
user['name'] = nickName
# Generates answear including user nick name at the end of the line
print "This is really cool nick name, " + nickName 

input = raw_input("Tell me more... ")
print("Sorry " + nickName + " but I'm not very clever chat bot :/" )
