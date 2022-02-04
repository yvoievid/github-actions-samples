import configparser
from flask import Flask

config = configparser.RawConfigParser()
config.read('config.properties')

app = Flask(__name__)

if config.getboolean("features", "feature_1") == True:
	message = "Hello, Sasha!"
else:
	message = "Hello, World!"

@app.route("/")
def hello():
	return message 


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8050)
