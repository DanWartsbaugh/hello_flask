from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

#localhost:5000/dojo - have it say "Dojo!"
@app.route('/dojo')
def hello_dojo():
    return 'Dojo!'  

#one url pattern and function that can handle Hi Flask, Hi Michael, Hi John
#localhost:5000/say/flask - "Hi Flask!"
#localhost:5000/say/michael - "Hi Michael!"
#localhost:5000/say/john - "Hi John!"
@app.route('/say/<name>')
def say_hi(name):
    return 'Hi ' + name.capitalize() + "!" 

#one url pattern and function that can handle the following:
#localhost:5000/repeat/35/hello - have it say "hello" 35 times
#localhost:5000/repeat/80/bye - have it say "bye" 80 times
#localhost:5000/repeat/99/dogs - have it say "dogs" 99 times
@app.route('/repeat/<int:num>/<word>')
def say_repeat(num,word):
    return   (word + " " )* num

@app.route('/<other>')
def sorry(other):
    if other != "dojo" or other != "say" or other != "repeat":
        return  "Sorry! No response. Try again."

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

