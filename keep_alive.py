from flask import Flask
from threading import Thread

app = Flask('')

log = "Hello. I am alive!"

@app.route('/')
def home():
    return log

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

def add_log(toadd):
  global log
  #new line is <br> in html
  log = log + '<br><br>' + toadd