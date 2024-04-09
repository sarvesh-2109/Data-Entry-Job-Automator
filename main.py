from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

# Beautiful Soup
response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
zillow_webpage = response.text

soup = BeautifulSoup(zillow_webpage, "html.parser")

all_link_elements = soup.select(".StyledPropertyCardDataWrapper a")
all_links = [link["href"] for link in all_link_elements]
print(f"There are {len(all_links)} links to individual listings in total: \n")
print(all_links)

all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
all_addresses = [address.getText().replace(" | ", " ").strip() for address in all_address_elements]
print(f"\n After having been cleaned up, the {len(all_addresses)} addresses now look like this: \n")
print(all_addresses)

all_price_elements = soup.select(".PropertyCardWrapper span")
all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in all_price_elements if "$" in price.text]
print(f"\n After having been cleaned up, the {len(all_prices)} prices now look like this: \n")
print(all_prices)

# Selenium
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_option)
wait = WebDriverWait(driver, 10)

for num in range(len(all_links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdPbdo_TZ-j3B3pLXcS6bjzcP8WaSwr6XXbZfOAlc8tVkRmIg/viewform?usp=sf_link")

    form_address = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    form_address.click()
    form_address.send_keys(all_addresses[num])

    form_price = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    form_price.click()
    form_price.send_keys(all_prices[num])

    form_property_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    form_property_link.click()
    form_property_link.send_keys(all_links[num])

    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "Submit")]')))
    submit_button.click()

