from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)

app.secret_key="b'\x96b\xf8\xf7\x91,\x16\xeaK\xae,Y\xc2\x10V<\xe7\xce`\x1fH\x15Ii"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post_results', methods=["POST"])
def post_results():
    session['name'] = request.form['name']
    session['dojo_location'] = request.form['dojo_location']
    session['favorite_language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html')

if __name__=="__main__":
    app.run(debug=True)
