import bs4
import webbrowser
import requests

productURL = 'https://www.amazon.com/DJI-Spark-Portable-Drone-Alpine/dp/B07173X82D/ref=asc_df_B07173X82D/?tag=hyprod-20&linkCode=df0&hvadid=198104292682&hvpos=1o1&hvnetw=g&hvrand=14006295728399730&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9027609&hvtargid=pla-382300687598&psc=1'


def getAmazonPrice(productURL):
    response_obj = requests.get(productURL, headers={
                                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"})
    response_obj.raise_for_status()

    soup = bs4.BeautifulSoup(response_obj.content, 'lxml')
    elems = soup.select(
        '#priceblock_ourprice')
    return elems[0].text.strip()


price = getAmazonPrice(
    'https://www.amazon.com/DJI-Spark-Portable-Drone-Alpine/dp/B07173X82D/ref=asc_df_B07173X82D/?tag=hyprod-20&linkCode=df0&hvadid=198104292682&hvpos=1o1&hvnetw=g&hvrand=14006295728399730&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9027609&hvtargid=pla-382300687598&psc=1')
print('The price for the DJI Spark drone is:  ' + price)
