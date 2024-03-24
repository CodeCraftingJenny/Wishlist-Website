import requests
from bs4 import BeautifulSoup


def scrape_amazon_product_info(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # get price
        price_element = soup.find('span', {'class': 'a-price-whole'})
        price = price_element.text.strip() if price_element else 'Price not available'

        # get pic
        image_element = soup.find('img', {'id': 'landingImage'})
        image_url = image_element.get('src') if image_element else None

        return {'price': price, 'image_url': image_url}
    except Exception as e:
        print("Error scraping product info:", e)
        return {'price': 'N/A', 'image_url': 'N/A'}


# test demo url
amazon_url = 'https://www.amazon.co.jp/-/zh/dp/B01NCX3W3O/?_encoding=UTF8&pd_rd_w=0aCW0&content-id=amzn1.sym.8a0ce368-8a2b-4c6e-a877-82963f239580&pf_rd_p=8a0ce368-8a2b-4c6e-a877-82963f239580&pf_rd_r=AN44887FJC9EKG3MDRR4&pd_rd_wg=omeKk&pd_rd_r=c24c7cad-cb69-4e9d-9b95-f9c40e783578&ref_=pd_gw_crs_zg_bs_637394&th=1'

# get item detail
product_info = scrape_amazon_product_info(amazon_url)

# print item detail
print("Price:", product_info['price'])
print("Image URL:", product_info['image_url'])

if __name__ == '__main__':
    scrape_amazon_product_info(amazon_url)