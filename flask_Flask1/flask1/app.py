from flask import Flask
app = Flask(__name__)



@app.route("/",methods=['GET'])
def helloworld():
    return "<h1>Hello Worlddsgfg!</h1>"

@app.route("/about",methods=['GET'])
def about():
    return "<h1>about my company</h1>"

@app.route("/service",methods=['GET'])
def service():
    return "<h1>company</h1>"





if __name__ == "__main__":
    app.run(debug=True)