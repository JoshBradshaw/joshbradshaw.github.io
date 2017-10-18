
from selenium import webdriver
import time

chrome_path = r"C:\Program Files (x86)\Google\Chrome\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("https://reservations.ontarioparks.com/OntarioParks?Map")

driver.find_element_by_xpath("""//*[@id="selEquipmentSub"]/option[4]""").click()
driver.find_element_by_xpath("""//*[@id="selPartySize"]/option[7]""").click()
driver.find_element_by_xpath("""//*[@id="MainContentPlaceHolder_LocationList"]/option[70]""").click()
driver.find_element_by_xpath("""//*[@id="MainContentPlaceHolder_QuickDateList"]/option[2]""").click()

availSites = driver.find_elements_by_class_name("area_avail")
critSites = driver.find_elements_by_class_name("area_filt")
unavailSites = driver.find_elements_by_class_name("area_unavail")

def checking():
	if availSites:
		print("We've got something here.")
	else:
		print("Still nothing...")

	time.sleep(60)
	driver.refresh()

while True:
	checking()