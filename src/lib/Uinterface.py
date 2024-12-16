import eel

eel.init('www')

@eel.expose                         # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)


say_hello_py('Python World!')
eel.say_hello_js('Python World!')   # Call a Javascript function

eel.start('main.html')             # Start (this blocks and enters loop)

