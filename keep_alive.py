from flask import Flask, send_from_directory
from threading import Thread

app = Flask('')

@app.route('/')

#@app.route('/videos/<filename>')
#def images_folder(filename):  
#    return send_from_directory('videos', filename)
  
def home():
  return "Hello. I am Alive!"

def run():
  app.run(host='0.0.0.0',port=8080)
  
def keep_alive():
  t = Thread(target=run)
  t.start()