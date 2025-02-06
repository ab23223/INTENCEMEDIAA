from bottle import run, route, template, static_file

# Route to serve static files like images, CSS, etc.
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

# Route for home page (shows albums or general content)
@route('/')
def index():
    return template('index')  # Make sure you have an 'index.tpl' template in the 'views/' folder

# Route for 'gmshow' album page
@route('/album_gmshow.html')
def album_gmshow():
    return template('album_gmshow.html')  # Make sure you have an 'album_gmshow.tpl' template in the 'views/' folder

# Route for 'car' album page
@route('/album_car.html')
def album_car():
    return template('album_car.html')  # Make sure you have an 'album_gmshow.tpl' template in the 'views/' folder

# Route for 'vk' album page
@route('/album_vk.html')
def album_vk():
    return template('album_vk.html')  # Make sure you have an 'album_gmshow.tpl' template in the 'views/' folder

# Route for 'albums' album page
@route('/albums.html')
def album():
    return template('albums.html')  # Make sure you have an 'album_gmshow.tpl' template in the 'views/' folder

# Run the app
run(reloader=True)
