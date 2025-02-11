from bottle import Bottle,run, route, template, static_file


app = Bottle()

@app.route('/')
def index():
    return template('index')

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

# Route for 'albums' album page
@route('/buy.html')
def buy():
    return template('buy.html')  # Make sure you have an 'album_gmshow.tpl' template in the 'views/' folder

# Route for 'albums' album page
@route('/cart.html')
def cart():
    return template('cart.html')  # Make sure you have an 'album_gmshow.tpl' template in the 'views/' folder


# Route for 'albums' album page
@route('/checkout.html')
def checkout():
    return template('checkout.html')  # Make sure you have an 'album_gmshow.tpl' template in the 'views/' folder

# Route for 'albums' album page
@route('/success.html')
def success():
    return template('success.html')  # Make sure you have an 'album_gmshow.tpl' template in the 'views/' folder

# Route for 'albums' album page
@route('/select.html')
def select():
    return template('select.html')  # Make sure you have an 'album_gmshow.tpl' template in the 'views/' folder

@route('/albums2.html')
def albums2():
    return template('albums2.html')
    
# Run the app
run(reloader=True)
