import requests
from lxml import html
from bs4 import BeautifulSoup as bs
import getpass

Username = input("Username: ")
Password = getpass.getpass()

redditURL = "https://www.reddit.com/"

# creating session
print("creating session")
session_requests = requests.session()

def login(Username, Password):

    loginURL = "https://www.reddit.com/login/"
    result = session_requests.get(loginURL)

    tree = html.fromstring(result.text)
    print(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='csrf_token']/@value")))[0]

    # making payload
    print("making payload")
    payload = {
        "username": Username,
        "password": Password,
        "crsf_token": authenticity_token
    }

    # actually logging in
    print("actually logging in")
    result = session_requests.post(
        loginURL,
        data=payload,
        headers = dict(referer=loginURL)
    )


def getHeaders():
    result = session_requests.get(redditURL)
    soup = bs(result.text, "html.parser")

    print(soup.find_all("h3", class_="_eYtD2XCVieq6emjKBH3m"), result.ok)

login(Username, Password)
getHeaders()