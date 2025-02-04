from bottle import run,route,template, static_file
import requests

@route('/static/<filepath:path>')
def server_static(filepath):
     return static_file(filepath, root='./static')


@route('/')
def index():
     return template('homepage')

@route('/index')
def index():
     return template('index')

#main
run(reloader=True) 