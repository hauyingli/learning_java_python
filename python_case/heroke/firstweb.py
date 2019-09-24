from flask import Flask
app=Flask(__name__)

@app.route("/")
def home():
    return  "hello flask"

@app.route("/test")
def test():
    return  "test flask"

if __name__=="__main__":
    app.run()