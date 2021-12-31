from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def countFreeGames():
    driver = webdriver.Chrome('C:/Users/mths/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.10/chromedriver')

    driver.get('https://www.epicgames.com/store/pt-BR/free-games')

    try: 
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[1]/div/div[4]/main/div[3]/div/div/div/div/div[2]/span/div/div/section/div/div'))
            )
    finally:
        driver.quit()

    quantity = len(element) - 1

    return quantity
