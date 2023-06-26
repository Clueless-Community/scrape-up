import pandas as pd
import scrapy

class FlipkartSpider(scrapy.Spider):
    name = "flipkart"
    start_urls = ["https://www.flipkart.com/search?q=mobile+phone+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=2"]
    
    def parse(self, response):
        product_name = []
        prices = []
        description = []
        reviews = []
        
        try:
            box = response.css("div._1YokD2._3Mn1Gg")
            names = box.css("div._4rR01T::text").getall()
            
            for name in names:
                product_name.append(name)
            
            prices = box.css("div._30jeq3._1_WHN1::text").getall()
            
            desc = box.css("ul._1xgFaf::text").getall()
            
            for d in desc:
                description.append(d)
            
            revi = box.css("div._3LWZlK::text").getall()
            
            for r in revi:
                reviews.append(r)
            
            df = pd.DataFrame({
                "Product Name": product_name,
                "Prices": prices,
                "Description": description,
                "Reviews": reviews
            })
            
            df.to_csv("flipkart-scraping-under-50k.csv", index=False)
        
        except Exception as e:
            print("An error occurred:", str(e))
