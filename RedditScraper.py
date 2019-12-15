import requests
from lxml import html
import bs4 as bs
import getpass

Username = input("Username: ")
Password = getpass.getpass()

redditURL = "https://www.reddit.com/"


def login(Username, Password):
    # creating session
    print("creating session")
    session_requests = requests.session()

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

    session_requests.get(redditURL)

    print(result.ok)

login(Username, Password)