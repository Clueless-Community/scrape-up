from bs4 import BeautifulSoup
import json

from scrape_up.config.request_config import RequestConfig, get


class Coursera:
    """
    Create an object of the 'Courses' class:
    ```python
    scraper = Courses("topic")
    ```
    | Methods                               | Details                                                                                    |
    | ------------------------------------- | ------------------------------------------------------------------------------------------ |
    | `.get_courses()`                       | Returns the courses with title, taught by, skills, rating, review count, img url and link |
    | `.fetchModules(course='Course Name')` | Returns the modules associated with the Coursera.                                          |
    """

    def __init__(self, topic: str, *, config: RequestConfig = RequestConfig()):
        self.topic = topic
        self.config = config

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
                "taught_by": Organization which teaches the course
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
            res = get(url, self.config)
            soup = BeautifulSoup(res.text, "html.parser")

            courses_data = []
            courses = soup.find_all("div", class_="css-1evtm7z")

            for c in courses:
                try:
                    title = c.find("a").getText()
                    taught_by = c.find(
                        "p", class_="cds-ProductCard-partnerNames css-vac8rf"
                    ).getText()
                    skills = c.find(
                        "div", class_="cds-CommonCard-bodyContent"
                    ).p.getText()[20:]
                    review_div = c.find("div", class_="product-reviews css-pn23ng")
                    rating = review_div.find("p", class_="css-2xargn").getText()
                    review_count = (
                        review_div.find("p", class_="css-vac8rf")
                        .getText()
                        .replace("(", "")
                        .replace(")", "")
                    )
                    img = c.find("div", class_="cds-CommonCard-previewImage")
                    img_url = img.find("img")["src"]
                    link = "https://www.coursera.org" + c.find("a")["href"]
                except:
                    pass

                courses_data.append(
                    {
                        "title": title,
                        "taught_by": taught_by,
                        "skills": skills,
                        "rating": rating,
                        "review_count": review_count,
                        "img_url": img_url,
                        "link": link,
                    }
                )
            return courses_data
        except:
            return None

    def fetch_modules(self, course):
        """
        Class - `Coursera`
        Example:
        ```
        courses = Coursera(topic="ml")
        courses.fetch_modules(course="Machine Learning with Python)
        ```
        Note: Some courses have specializations instead of modules. Make sure the code works for both.

        Returns:
        For modules:
        ```js
        {
            "Module 1": Name of the first module
        }
        ```

        For specializations:
        ```js
        {
            "Specialization 1": {
                                    Title: Name of the specialization
                                    Link: Link to the specialization page
                                }
        }
        ```
        """

        courseList = self.get_courses()
        global courseURL
        for i in courseList:
            if i["title"] == course:
                courseURL = i["link"]
        try:
            res = get(courseURL, self.config)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, "html.parser")
                script_tag = soup.find("script", {"id": "__NEXT_DATA__"})
                if script_tag is not None:
                    json_blob = json.loads(script_tag.get_text())
                    product_data = json_blob["props"]["pageProps"]["initialData"][
                        "data"
                    ]["product"]

                type = "Module"
                module_section = soup.find("div", id="modules")
                if module_section == None:
                    module_section = soup.find("div", id="courses")
                    type = "Specialization"
                modules = module_section.find_all(
                    "div", attrs={"data-testid": "accordion-item"}
                )
                modules_data = {}

                for index, m in enumerate(modules):
                    if type == "Module":
                        # For modules
                        mod = m.find("h3").getText()
                    else:
                        # For specializations
                        mod = {}
                        mod["Title"] = m.find("h3").getText()
                        mod["Link"] = "https://www.coursera.org" + m.find("a")["href"]
                    modules_data[f"{type} {index+1}"] = mod
                return modules_data
            else:
                return None
        except:
            return None
