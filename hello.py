from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define route mappings
@app.route('/')
@app.route('/hello')
def hello():
    # Render the page
    return "Hello Python!"

if __name__ == '__main__':
    # Run the app server on localhost:4449 with debug mode on
    app.run(host='127.0.0.1', port=4449, debug=True)
