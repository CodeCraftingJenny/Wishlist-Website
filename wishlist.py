from flask import Flask, render_template, request, redirect, url_for
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
items = []


def scrape_amazon_product_info(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # get price
        price_element = soup.find('span', {'class': 'a-offscreen'})
        price = price_element.text.strip() if price_element else 'Price not available'

        # get pic
        image_element = soup.find('img', {'id': 'landingImage'})
        image_url = image_element.get('src') if image_element else None

        return {'price': price, 'image_url': image_url}
    except Exception as e:
        print("Error scraping product info:", e)
        return {'price': 'N/A', 'image_url': 'N/A'}


def list_append(item):
    global items
    items.append(item)


def list_delete(item):
    global items
    items.remove(item)


@app.route("/", methods=['GET', 'POST'])
def wishlist():
    if request.method == 'POST':
        url_added = request.form['wishlist_url']
        if url_added != '':
            product_info = scrape_amazon_product_info(url_added)
            if product_info['price'] != 'N/A':
                items.append({'name': url_added, 'price': product_info['price'], 'image': product_info['image_url']})

    return render_template('wish.html', wishlist=items)


@app.route('/delete/<path:item>')
def delete(item):
    try:
        for i in items:
            if i['name'] == item:
                items.remove(i)
                break
    except Exception as e:
        print("Error deleting item:", e)
    return redirect(url_for('wishlist'))



if __name__ == '__main__':
    app.run(debug=True)
