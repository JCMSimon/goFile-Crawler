import random
from turtle import dot
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from string import ascii_letters, digits




def genURLCode():
	code = "".join([random.choice(ascii_letters + digits) for _ in range(6)])
	return code

def thingy():
	url = "https://gofile.io/d/" + genURLCode()
	driver.get(url)
	try:
		print(f"[GFC] {url} ...")
		pls = WebDriverWait(driver, 2).until(
			EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "This file does not exist.")]')))
	except TimeoutException:
		# this is when "file not found" isnt there
		try:
			filename = WebDriverWait(driver, 5).until(
				EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div[15]/div/div/div/div[1]/div[1]/h4/span'))).get_attribute("innerHTML")
			if filename:
				print(f"File might be at {url} with title '{filename}' <- ignore if no filename")
				input("==>")
			else:
				print(f"[GFC] Nope (3)")
		except TimeoutException:
			print(f"[GFC] Nope (2)")
	else:
		print(f"[GFC] Nope (1)")

def doTheThing():
	while True:
		thingy()

if __name__ == "__main__":
	chrome_options = Options()
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("log-level=3")
	driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
	doTheThing()




