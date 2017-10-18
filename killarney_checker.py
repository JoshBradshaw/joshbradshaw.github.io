
from selenium import webdriver
import time
import winsound
duration = 10000  # millisecond
freq = 880  # Hz
from twilio.rest import Client
# put your own credentials here
account_sid = "AC374cae134941da7d782e9f8eb796ed22"
auth_token = "7621ef77bf59d3cb75ffcb3850f6f0c2"
client = Client(account_sid, auth_token)


chrome_path = r"C:\Program Files (x86)\Google\Chrome\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("https://reservations.ontarioparks.com/OntarioParks?List")

driver.find_element_by_xpath("""//*[@id="selEquipmentSub"]/option[6]""").click()
time.sleep(4)
driver.find_element_by_xpath("""//*[@id="selPartySize"]/option[4]""").click()
time.sleep(4)
driver.find_element_by_xpath("""//*[@id="MainContentPlaceHolder_QuickDateList"]/option[2]""").click()
time.sleep(4)
driver.find_element_by_xpath("""//*[@id="MainContentPlaceHolder_LocationList"]/option[40]""").click()
time.sleep(4)

availSites = driver.find_elements_by_class_name("area_avail")
critSites = driver.find_elements_by_class_name("area_filt")
unavailSites = driver.find_elements_by_class_name("area_unavail")

def checking():
    if availSites:
        print("We've got something here.")
        winsound.Beep(freq, duration)
        client.messages.create(
            to="+19055311056",
            from_="+12897699670",
            body="There is a campsite available at MEW lake"
            )
        client.messages.create(
            to="+19055316139",
            from_="+12897699670",
            body="There is a campsite available at MEW lake"
            )
    else:
        print("Still nothing...")

    time.sleep(60)
    driver.refresh()

while True:
    checking()