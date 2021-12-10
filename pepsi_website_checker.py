from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from twilio_sms import textmyself
import datetime
import time
import random

now = datetime.datetime.now()
prev_hour = None
texts_sent_in_hour = 0
driver = None

while True:
    now = datetime.datetime.now()
    print(f'The Current Time is {now}')
    if prev_hour != now.hour:
        prev_hour = now.hour
        texts_sent_in_hour = 1
        textmyself(f'The Current Time is {now}')

    try:
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        print('Getting micdrop.pepsi.com')
        driver.get("https://micdrop.pepsi.com/")

        waitlist_elem = driver.find_element_by_class_name('SecondaryTitle_secondaryTitle__20ZFv')

        print(f'Waitlist Elem Text: {waitlist_elem.text}')
        if waitlist_elem.text != 'Our waitlist is coming soon. Please check back later.':
            print(f'Waitlist Elem Text has changed. Messaging...')
            if texts_sent_in_hour < 10:
                texts_sent_in_hour += 1
                textmyself(f'CHANGED Waitlist Elem Text has changed: "{waitlist_elem.text}"\n'
                           f'Texts sent in hour: {texts_sent_in_hour}')
                texts_sent_in_hour += 1
                textmyself(f'CHANGED Waitlist Elem Text has changed: "{waitlist_elem.text}"\n'
                           f'Texts sent in hour: {texts_sent_in_hour}')

    except BaseException as e:
        print(f'Exception: {e}')
        if texts_sent_in_hour < 10:
            texts_sent_in_hour += 1
            textmyself(f'EXCEPTION Program has an exception: "{e}"\n'
                       f'Texts sent in hour: {texts_sent_in_hour}')
            texts_sent_in_hour += 1
            textmyself(f'EXCEPTION Program has an exception: "{e}"\n'
                       f'Texts sent in hour: {texts_sent_in_hour}')

    finally:
        driver.quit()

    print()
    time.sleep(int(5 + random.random() * 5))


