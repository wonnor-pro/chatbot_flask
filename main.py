from flask import Flask, render_template, request, json, jsonify


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dev')
def dev():
    return render_template("dev.html")


@app.route('/sendDate', methods=['GET', 'POST'])
def form_data():
    msg = json.loads(list(request.form.lists())[0][0])
    txt = msg['query']
    n = len(txt)
    print(txt, n)
    return jsonify({'status': '0', 'msg': f'you just typed in {txt}, length = {n}'})


if __name__ == '__main__':
    app.run()
