import twitter, datetime, urllib2 #import external libraries

currentSession = open("/Users/student/Library/Application Support/Google/Chrome/Default/Current Session") #open chrome browsing history

lastSession = currentSession.read() #variable that reads last session info

user = 3091338875 #Twitter user id

file = open("API-key.txt") #open file containing all keys and access tokens

cred = file.readline().strip().split(",") #read credentials

startIndex = lastSession.rfind("http") #start index of last session
endIndex = lastSession.find(chr(0), startIndex) #end index of last session

url = lastSession[startIndex:endIndex] #variable that prepares last session page address
print(url)

urlreceived = urllib2.urlopen(url) 
html = urlreceived.read()

beginTitle = html.find("<title>") + len("<title>") #finding whaever is in between "title" tag
finishTitle = html.find("</title>", beginTitle)
theTitle = html[beginTitle:finishTitle] #prepares title


api = twitter.Api(consumer_key=cred[0],consumer_secret=cred[1],
		  access_token_key=cred[2],access_token_secret=cred[3]) #validating access info

timestamp = datetime.datetime.utcnow() #prepares imestamp to be displayed

response = api.PostUpdate("I really like " + url + " at " + str(timestamp) + " Title is: " + str(theTitle)) #posts web pege url, time and date and page title

print("Status updated to: " + response.text) 

statuses = api.GetUserTimeline(user) #gets last Twitter post and prints it in terminal
print (statuses[0].text)