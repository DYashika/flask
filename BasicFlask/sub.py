from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    mydict = {'Maths':80, 'C':70, 'Java':60}
    print (mydict)
    return render_template('table.html', mydict=mydict)

if __name__== '__main__':
    app.run(debug = True)
