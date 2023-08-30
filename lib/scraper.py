from turtle import ht
from bs4 import BeautifulSoup
import requests

headers = {"user-agent": "my-app/0.0.1"}
html = requests.get("https://flatironschool.com/career-services/", headers=headers)

doc = BeautifulSoup(html.text, "html.parser")
courses = doc.select(".heading-25-extrabold color-black")

# Using list comprehension to apply .strip() to each element
for course in courses:
    print(course.content)
