from flask import Flask, render_template, request

app = Flask(__name__)
items = []

@app.route("/", methods=['GET', 'POST'])
def wishlist():
    if request.method == 'POST':
        item_added = request.form['wishlist_item']
        items.append(item_added)
    
    return render_template('wish.html', wish_list=items)

app.run(debug=True)
