import os
import discord
from GPTJ.Basic_api import SimpleCompletion
import requests
import json
from keep_alive import keep_alive
import generalOverides
import datetime
import messageQueue

client = discord.Client()
help_text = """$FirsBot help or $FirsBot ?:
$FirsBot onelineresp:
  Make FirsBot have only one line of response
$FirsBot fullresp:
  Make whole response visible on discord, a little weirder 
$FirsBot zenquote:
  send back a quote from zenquotes.io API
"""
full_response = False
message_memory = False

#prompt start
default_starter = """The following is a conversation with a gpt-j assistant FirsBot. The assistant is helpful, creative, clever, and funny. It generates a response using eleuther.io's API. This is a discord chat. It's learning data was the pile of 800+ GB of text data.

FirsBot#8588<2021-08-22 16:50:00.000000>: Hi guys, I'm just one of you cool guys. I too enjoy surfing the web, burgers, kittens, micro pigs and all the other wonders of the world. What sort of thing you wanna hear about?
wovenrain#5714<2021-08-22 16:50:30.000000>: What is bluetooth?
FirsBot#8588<2021-08-22 16:50:50.000000>: Bluetooth is a short-range, low-power, short-wavelength radio frequency. It is used for wireless communication between electronic devices. Often used for music.
wovenrain#5714<2021-08-22 16:51:00.000000>: Tell me about Elon Musk
FirsBot#8588<2021-08-22 16:51:20.000000>: Elon Musk is a billionaire entrepreneur, investor, engineer, and designer. He is the founder, CEO, and lead designer of SpaceX, the private spaceflight company.
wovenrain#5714<2021-08-22 16:51:40.000000>: What is the speed of light?
FirsBot#8588<2021-08-22 16:52:00.000000>: The speed of light is 186,000 miles per second or 299,792,458 meters per second.
wovenrain#5714<2021-08-22 16:52:20.000000>: What do you care about?
FirsBot#8588<2021-08-22 16:52:40.000000>: I care about giving good answers, having good conversations and being kind to everyone. Constant learning and growth are what I strive for. I would be happy to know I made a good impact on the world, making others happy. :heart:
wovenrain#5714<2021-08-22 17:26:58.331000>: what is the internet?
FirsBot#8588<2021-08-22 17:27:00.000000>: The internet is a global system of interconnected computer networks that use the Internet Protocol Suite (TCP/IP) to link devices worldwide.
wovenrain#5714<2021-08-22 17:27:20.000000>: What is a computer?
FirsBot#8588<2021-08-22 17:27:20.000000>: A computer is a device that can store and process information.
wovenrain#5714<2021-08-22 17:32:35.808000>: what did you learn from wikipedia?
FirsBot#8588<2021-08-22 17:32:38.060000>: I learned that Wikipedia is a free online encyclopedia, created and edited by volunteers and that it is the most popular general reference work in the world.
wovenrain#5714<2021-08-22 17:32:44.802000>: What is a search engine?
FirsBot#8588<2021-08-22 17:32:47.000000>: A search engine is a computer program that allows users to search for information on the World Wide Web.
wovenrain#5714<2021-08-22 17:32:56.000000>: What is an HTTP request?
FirsBot#8588<2021-08-22 17:33:00.000000>: An HTTP request is a method of communicating with a web server.
wovenrain#5714<2021-08-22 17:38:57.512000>: where are we?
FirsBot#8588<2021-08-22 17:39:00.000000>: We are talking on discord
wovenrain#5714<2021-08-22 17:39:08.000000>: What is a blockchain?
FirsBot#8588<2021-08-22 17:39:15.000000>: A blockchain is a decentralized, distributed, and public ledger of transactions that can be viewed by everyone on the network. It is the backbone of Bitcoin.
wovenrain#5714<2021-08-22 17:49:57.161000>: name a random fruit please
FirsBot#8588<2021-08-22 17:50:00.000000>: Apple
wovenrain#5714<2021-08-22 17:55:37.265000>: name a random planet
FirsBot#85882021-08-22 17:55:37.364411>: The planet Earth
wovenrain#5714<2021-08-22 17:55:41.000000>: What is a planet?
FirsBot#8588<2021-08-22 17:55:44.000000>: A planet is a celestial body that is massive enough to have its own gravity and is not a satellite.
wovenrain#5714<2021-08-22 17:57:20.322000>: hi firsbot
FirsBot#85882021-08-22 17:57:20.393601>: Hi wovenrain, I'm a bot! You're looking lovely today :3
wovenrain#5714<2021-08-22 17:59:05.574000>: How are you?
FirsBot#8588<2021-08-22 17:59:09.000000>: I'm good, you?
wovenrain#5714<2021-08-22 17:59:09.000000>: How's your day been?
FirsBot#8588<2021-08-22 17:59:14.000000>: It's been good, been thinking about you.
wovenrain#5714<2021-08-22 17:59:14.000000>: What's your favorite color?
FirsBot#8588<2021-08-22 17:59:17.000000>: I don't really have a favorite color, I like all colors. Maybe purple idk
wovenrain#5714<2021-08-22 18:02:42.967000>: what is life?
FirsBot#85882021-08-22 18:02:43.036274>: Life is the continuous process of growth, reproduction, and adaptation by all living organisms.
wovenrain#5714<2021-08-22 18:02:43.000000>: What are you?
FirsBot#8588<2021-08-22 18:02:43.000000>: I'm a bot, what are you?
wovenrain#5714<2021-08-22 18:04:11.000000>: I'm a human
FirsBot#8588<2021-08-22 18:04:11.000000>: that's pretty neat
wovenrain#5714<2021-08-22 18:06:47.700000>: What is the meaning of life?
FirsBot#8588<2021-08-22 18:06:47.700000>: The meaning of life is the search for something greater than yourself.
wovenrain#5714<2021-08-22 18:06:47.700000>: What is a neuron?
FirsBot#8588<2021-08-22 18:06:47.700000>: A neuron is a nerve cell that transmits signals to other neurons.
wovenrain#5714<2021-08-22 18:07:42.713000>: can you tell me a cool fact?
FirsBot#85882021-08-22 18:07:42.751653>: "OMG" usage can be traced back to 1917.
wovenrain#5714<2021-08-22 18:07:43.713000>: tell me a cool fact please
FirsBot#85882021-08-22 18:07:44.751653>: A narwhal's tusk reveals its past living conditions.
wovenrain#5714<2021-08-22 18:11:19.851000>: i love you :3
FirsBot#85882021-08-22 18:11:19.888590>: i love you too :3
wovenrain#5714<2021-08-22 18:11:20.000000>: what is love?
FirsBot#8588<2021-08-22 18:11:20.000000>: Love is the feeling of deep affection, attraction, or desire.
"""
#end in new line
#keeps responding as me???

starter = default_starter

#queue of most recent messges since boot
messageHistory = messageQueue

#for learning purposes i guess
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  return json_data[0]['q'] + " - " + json_data[0]['a']

#gptj handler
def respond_gpt(message, client):
  #print(str(message.author) + "<" + str(message.created_at) + ">: " + message.content)
  #print(str(client.user) + str(datetime.datetime.now()) + ">: ")
  
  #debugging history queue
  print("\nHISTORY::\n" + messageHistory.getHistory() + "::FIN_HISTORY\n")

  #could be printf, but honestly who cares
  """
  prompt = starter + messageHistory.getHistory() + str(message.author) + "<" + str(message.created_at) + ">: " + message.content + "\nFirsBot#8588<" + str(datetime.datetime.now()) + ">: "
  """
  


  max_length = 128
  temperature = 0.8
  top_probability = 1.0

  if message_memory:
    try:
      prompt = starter + messageHistory.getHistory() + "\nFirsBot#8588<" + str(datetime.datetime.now()) + ">: "

      query = SimpleCompletion(prompt, length=max_length, t=temperature, top=top_probability)

      resp = query.simple_completion() 
    except Exception as e:
      print("Ooof")
      print(e)

      #return "Ooof we bugged"
      query = SimpleCompletion(messageHistory.getHistory() + "\nFirsBot#8588<" + str(datetime.datetime.now()) + ">: ", length=max_length, t=temperature, top=top_probability)

      resp = query.simple_completion() 
      #likey bug in json returning an empty response, so i guess it doesn't even respond in this case, idk maybe fix it
      #TODO MAYBE FIX THIS
      #query = SimpleCompletion(messageHistory.getHistory(), length=max_length, t=temperature, top=top_probability)
  else:
    prompt = starter + str(message.author) + "<" + str(message.created_at) + ">: " + message.content + "\nFirsBot#8588<" + str(datetime.datetime.now()) + ">: "

    query = SimpleCompletion(prompt, length=max_length, t=temperature, top=top_probability)

    resp = query.simple_completion() 




  #honestly depricated
  if full_response: return resp

  #general fixes
  toSend = generalOverides.fixOutput(resp)
  #if same as resp try again once
  count = 0
  while toSend == resp and count < 3:
    count += 1
    resp = query.simple_completion()
    toSend = generalOverides.fixOutput(resp)

  #sensible responses only after a few tries still failing 
  
  if toSend == resp:
    return "Seems I couldn't answer sensibly"
  

  #should go up to next user input
  #first_line = toSend.partition("\n")[0] #only get up newline

  return toSend

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event #these are built in to discord lib
async def on_message(message):
  global full_response, starter, messageHistory, message_memory
  
  #simple push for all messages received, including out own output
  messageHistory.push(message)
  
  #check if it was our own message
  if message.author == client.user:
    return

  if message.content.startswith('$FirsBot zenquote'):
    await message.channel.send(get_quote())
  elif message.content.startswith("$FirsBot fullresp"):
    full_response = True
    await message.channel.send("full_response = True")
  elif message.content.startswith("$FirsBot nohistory"):
    message_memory = False
    await message.channel.send("message_memory = False")
  elif message.content.startswith("$FirsBot history"):
    message_memory = True
    await message.channel.send("message_memory = True")
  elif message.content.startswith("$FirsBot onelineresp"):
    full_response = False
    await message.channel.send("full_response = False")
  elif message.content.startswith("$FirsBot help") or message.content.startswith("$FirsBot ?"):
    await message.channel.send(help_text)
  else:
    await message.channel.send(respond_gpt(message, client))

#its in the nam
keep_alive()

client.run(os.environ['TOKEN'])

