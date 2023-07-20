import requests
from bs4 import BeautifulSoup
import json


class Coursera:
    """
    Create an object of the 'Courses' class:
    ```python
    scraper = Courses("topic")
    ```
    | Methods                               | Details                                                                                    |
    | ------------------------------------- | ------------------------------------------------------------------------------------------ |
    | `.get_courses()`                       | Returns the courses with title, teached by, skills, rating, review count, img url and link |
    | `.fetchModules(course='Course Name')` | Returns the modules associated with the Coursera.                                          |
    """

    def __init__(self, topic):
        self.topic = topic

    def get_courses(self):
        """
        Class - `Coursera`
        Example:
        ```
        courses = Coursera(topic="ml")
        courses.get_courses()
        ```
        Returns:
        ```js
        [
            {
                "title": Title of the course
                "teached_by": Organization which teaches the course
                "skills": Skills learnt from the course
                "rating": Rating of the course
                "review_count": Np. of review of the course
                "img_url": Image URL of the course
                "link": Link to the course
            }
            ...
        ]
        ```
        """
        url = "https://www.coursera.org/search?query=" + self.topic
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")

            courses_data = {"courses": []}

            courses = soup.find_all("div", class_="css-1cj5od")

            for c in courses:
                try:
                    title = c.find("h2", class_="cds-119 css-h1jogs cds-121").getText()
                    teached_by = c.find(
                        "span", class_="cds-119 css-1mru19s cds-121"
                    ).getText()
                    skills = c.find("p", class_="cds-119 css-12ksubz cds-121").getText()
                    rating = c.find("p", class_="cds-119 css-11uuo4b cds-121").getText()
                    review_count = (
                        c.find("p", class_="cds-119 css-dmxkm1 cds-121")
                        .getText()
                        .replace("(", "")
                        .replace(")", "")
                    )
                    img = c.find("div", class_="css-1doy6bd")
                    img_url = img.find("img")["src"]
                    link = "https://www.coursera.org" + c.find("a")["href"]
                except:
                    pass

                courses_data["courses"].append(
                    {
                        "title": title,
                        "teached_by": teached_by,
                        "skills": skills,
                        "rating": rating,
                        "review_count": review_count,
                        "img_url": img_url,
                        "link": link,
                    }
                )
            return courses_data["courses"]
        except:
            return None

    def fetch_modules(self, course):
        """
        Class - `Coursera`
        Example:
        ```
        courses = Coursera(topic="ml")
        courses.fetch_modules()
        ```
        Returns:
        ```js
        [ modules ]
        ```
        """
        courseList = self.get_courses()
        global ccourseURL
        for i in courseList:
            if i["title"] == course:
                courseURL = i["link"]
        try:
            res = requests.get(courseURL)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, "html.parser")
                script_tag = soup.find("script", {"id": "__NEXT_DATA__"})
                if script_tag is not None:
                    json_blob = json.loads(script_tag.get_text())
                    product_data = json_blob["props"]["pageProps"]["initialData"][
                        "data"
                    ]["product"]

                modules = soup.find_all("div", class_="SyllabusModule")
                modules_data = []
                for m in modules:
                    mod = m.find("h3", class_="headline-2-text bold m-b-2").getText()
                    modules_data.append(mod)

                if modules_data == []:
                    modules = soup.find_all("div", class_="css-13tws8d")
                    for m in modules:
                        mod = m.find(
                            "a", class_="cds-119 cds-113 cds-115 css-1uw69sh cds-142"
                        ).getText()
                        modules_data.append(mod)

                return modules_data
            else:
                return "Server Error. Retry"
        except:
            return "No modules for this course"
