from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():

    return render_template("index.html")

#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    print ("Hello")
    return ("nothing")

if __name__ == '__main__':
    app.run()
