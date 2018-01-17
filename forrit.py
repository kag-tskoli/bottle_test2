import os
from bottle import route, run

@route('/')
def index():
  return "<a href='/about'>About</a>"

@route('/about')
def about():
  return "<h2>About us</h2>"
  
run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
