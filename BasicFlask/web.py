from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    name = "yashika"
    list1 = [1,2,3]
    return render_template('temp.html', name = name, list1 = list1)

if __name__== '__main__':
    app.run(debug = True)
