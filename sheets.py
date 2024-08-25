import re
from datetime import datetime, time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import requests
import constants

# requestsdriver = webdriver.Chrome()
#
#
# driver.get("https://docs.google.com/spreadsheets/d/1Gcs1f7JCxEGLhlPgex6oHdYYWZ0c9aDpWigDJYK1YAc/edit?gid=0#gid=0")


def get_actual_event_names() -> list:
    page = requests.get(constants.Links.team_table)
    soup = BeautifulSoup(page.text, "html.parser")

    all_events = soup.findAll('div', class_=constants.HTML_PATHS.event_cell)

    last_30_event_names = [el.text for el in all_events][-30:]
    print(last_30_event_names)
    upcoming_events = [el for el in last_30_event_names if check_event_is_actual(el)]
    return upcoming_events

def check_event_is_actual(event_name: str) -> bool:
    today = datetime.combine(datetime.now(), time.min)
    if re.search(r'\d\d.\d\d.\d\d', event_name):
        event_date = datetime.strptime(re.search(r'\d\d.\d\d.\d\d', event_name).group(), "%d.%m.%y")
    elif re.search(r'\d\d.\d\d', event_name):
        event_date = datetime.strptime(re.search(r'\d\d.\d\d', event_name).group() + '.' + str(today.year), "%d.%m.%Y")
    else:
        return False
    return event_date >= today