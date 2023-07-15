import requests
from bs4 import BeautifulSoup


class Coursera:
    """
    Create an object of the 'Courses' class\n
    ```python
    scraper = Courses("topic")
    ```
    | Methods     | Details                       |
    | ----------- | ----------------------------- |
    | `.getCourses()` | Returns the courses with title, teached by, skills, rating, review count, img url and link |
    """

    def __init__(self, topic):
        self.topic = topic

    def getCourses(self):
        """
        Class - `Coursera`
        Example:
        ```
        courses = Coursera(topic="ml")
        courses.getCoursera()
        ```
        Returns:
        {
            "title": Title of the course
            "teached_by": Organization which teaches the course
            "skills": Skills learnt from the course
            "rating": Rating of the course
            "review_count": Np. of review of the course
            "img_url": Image URL of the course
            "link": Link to the course
        }
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
                    link = "https://www.coursera.org/" + c.find("a")["href"]
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
