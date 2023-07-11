from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import undetected_chromedriver as uc
import re
import json

class Courses:
    """
    Class - `Courses`
    Example:
    ```
    topic = Courses(keyword="data science")
    ```\n
    Method :\n
    ``.get_courses() | Response - List of top courses for the keyword``\n
    """
    def __init__(self, keyword):
        self.keyword = keyword
        
    def __scrape_page(self):
        chrome_options = uc.ChromeOptions()
        chrome_options.add_argument('--headless')
        driver = uc.Chrome(options=chrome_options)
        driver.get('https://www.udemy.com/courses/search/?src=ukw&q=' + self.keyword.replace(' ', '+'))
        wait = WebDriverWait(driver, 10)
        return wait, driver
    
    def __replace_after_newline(self, text):
        index = text.find('\n')  # Find the index of the first occurrence of '\n'
        if index != -1:
            return text[:index]  # Return the substring up to the '\n'
        else:
            return text
        
    def __remove_html_tags(self, text):
        clean_text = re.sub('<.*?>', '', text)  # Use regex to remove HTML tags
        return clean_text

    def __extract_numbers(self, string):
        if string == None:
            return None
        number = re.findall(r'\d+', string)  # Find all numeric substrings using regex  # Convert the substrings to integers
        return number[0]
    
    def __extract_amount(self, string):
        if string == None:
            return None
        rupee_index = string.find("₹")  # Find the index of the "₹" sign
        if rupee_index != -1:
            amount = string[rupee_index + 1:]  # Extract the substring after the "₹" sign
            amount = amount.replace(",", "")  # Remove any commas from the extracted amount
            return amount.strip()  # Remove leading/trailing whitespaces
        else:
            return None
        
    def get_courses(self):
        """
        Class - `Courses`
        Example:
        ```
        topic = Courses(keyword="data science")
        topic.get_courses()
        ```
        Returns:
        {
            data : [\n
            { \n
            'title' : 'Title of course',\n
            'link' : 'Link to course',\n
            'description' : 'Description of course',\n
            'instructor' : 'Instructor of course',\n
            'rating' : 'Rating of course out of 5',\n
            'reviews' : 'Number of reviews for course',\n
            'discount_price' : 'Discounted price of course',\n
            'list_price' : 'List price of course',\n
            'duration' : 'Duration of course',\n
            'lectures' : 'Number of lectures in course',\n
            'level' : 'Level of course',\n
            }\n
        ],\n
        message: "Top Courses for {keyword}"
        }
        """
        wait, driver = self.__scrape_page()
        coursesArr = []
        courses = wait.until(lambda d: d.find_elements(By.CLASS_NAME ,'course-card--container--1QM2W'))
        if not courses:
            return 'error in scraping...'
        
        try:
            
            for course in courses:
                title = course.find_element(By.CLASS_NAME, 'course-card--course-title--vVEjC')
                
                link = title.find_element(By.TAG_NAME, 'a').get_attribute('href')
                
                description = course.find_element(By.CLASS_NAME, 'course-card--course-headline--2DAqq')
                
                instructor = course.find_element(By.CLASS_NAME, 'course-card--instructor-list--nH1OC').text.replace('\\','')
                
                rating = course.find_element(By.CLASS_NAME, 'star-rating-module--rating-number--2xeHu')
                
                try:
                    discount_price = course.find_element(By.CLASS_NAME, 'course-card--discount-price--1bQ5Q').text
                except Exception as inst:
                    discount_price = None
                    
                try:
                    list_price = course.find_element(By.CLASS_NAME, 'course-card--list-price--3RTcj').text
                except:
                    list_price = None
                    
                
                reviews = course.find_element(By.CLASS_NAME, 'course-card--reviews-text--1yloi')
                
                meta_info = course.find_element(By.CLASS_NAME, 'course-card--course-meta-info--2jTzN')
                
                meta_info_arr = meta_info.find_elements(By.CLASS_NAME, 'course-card--row--29Y0w')
                
                coursesArr.append({
                    'title' : self.__replace_after_newline(title.text),
                    'link' : link,
                    'description' : self.__remove_html_tags(description.text),
                    'instructor' : instructor,
                    'rating' : rating.text,
                    'reviews' : reviews.text[1:(len(reviews.text)-1)],
                    'discount_price' : self.__extract_amount(discount_price if discount_price else None),
                    'list_price' : self.__extract_amount(list_price if list_price else None),
                    'duration' : self.__extract_numbers(meta_info_arr[0].text),
                    'lectures' : self.__extract_numbers(meta_info_arr[1].text),
                    'level' : meta_info_arr[2].text,
                })
                
            return json.dumps({'data': coursesArr, 'message': "Top Courses for " + self.keyword + ""}, ensure_ascii=False)
        
        except Exception as inst:
            return json.dumps({'data': None, 'message': 'No courses found for ' + self.keyword + ''})
