import scrapy
import pandas as pd


class FlipkartSpider(scrapy.Spider):
    name = 'flipkart'
    start_urls = ['https://www.flipkart.com/search?q=mobile+phone+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=2']

    def parse(self, response):
        product_names = response.css('div._4rR01T::text').getall()
        prices = response.css('div._30jeq3._1_WHN1::text').getall()
        descriptions = response.css('ul._1xgFaf::text').getall()
        reviews = response.css('div._3LWZlK::text').getall()

        for item in zip(product_names, prices, descriptions, reviews):
            yield {
                'Product Name': item[0],
                'Prices': item[1],
                'Description': item[2],
                'Reviews': item[3]
            }

        # Follow next page if available
        next_page = response.css('a._1LKTO3::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)


# Run the spider
def run_spider():
    df = pd.DataFrame(columns=["Product Name", "Prices", "Description", "Reviews"])
    settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'filpkart-Scraping-under-50k.csv',
    }
    process = scrapy.crawler.CrawlerProcess(settings)
    process.crawl(FlipkartSpider)
    process.start()


if __name__ == '__main__':
    run_spider()
