import os
from bottle import route, run

@route('/')
def index():
  return "Bottle - Heroku deployment"
  
run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
