import discord

queue = []

# Create
queue = [10]
head = 0
cap = 10


# Get all
def getHistory():
  returnString = ""
  for x in queue[head:]:
    returnString = returnString + str(x.author) + "<" + str(x.created_at) + ">: " + x.content + "\n"
  for x in queue[:head]:
    returnString = returnString + str(x.author) + "<" + str(x.created_at) + ">: " + x.content + "\n"
  return returnString  

# Push
def push(message):
  global head, cap, queue
  head += 1
  if head >= cap:
    #set head 0
    head = 0
  queue[head] = message

# Pop (return too?)
