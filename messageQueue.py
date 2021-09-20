#import discord

# Create
queue = []
cap = 9


# Get all
def getHistory():
  returnString = ""
  for x in queue[0:len(queue)]:
    returnString = returnString + str(x.author) + "<" + str(x.created_at) + ">: " + x.content + "\n"
  return returnString  

# Push
def push(message):
  global cap, queue
  if len(queue) > cap:
    queue.pop(0)
  queue.append(message)

