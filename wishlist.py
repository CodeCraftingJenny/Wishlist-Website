from flask import Flask, render_template,request

app = Flask(__name__)
items = []

def list_append(item):
    global items
    items.append(item)
@app.route("/", method = ['GET','POST'])
def hello_world():
    if request.method == 'POST':
    item_added = request.form['wishlist_item']
    
    return render_template('wish.html')

app.run(debug = True) 