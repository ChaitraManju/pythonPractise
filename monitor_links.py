import requests
from gmail_smtp import sendmail

def monitor(links_to_track):
    for link in links_to_track:
        response = requests.get(link)
        statuscode = response.status_code
        print(f"Status code of {link} is {statuscode}")
        if statuscode == 200:
            print(f"{link} is down")
            sendmail()
        else:
            print(f"{link} is up and running")



