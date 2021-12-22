from flask import Flask
from routes import *
from flask_cors import CORS


CORS(app, resources={r"/*": {"origins": "*"}})

#we have to set env variable
# SET FLASK_APP=hello.py

#run in terminal to start server
# flask run

#set env to -> 
#to run in development server [similar to nodemon or line server]

# SET FLASK DEBUG=1

# we can also use this step to run in development server
if __name__=='__main__':
    app.run(debug=True)


