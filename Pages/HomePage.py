# Import Tools
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# Import Pages
from Locators.HomePageLocators import HomePageLocators
from Pages.MicrosoftLoginPage import MicrosoftLoginPage 

class HomePage():
        
    def __init__(self, driver):
        self.driver = driver
        
    # Header
    def click_on_login_button(self):
        self.driver.find_element(By.XPATH, HomePageLocators.button_for_login_options_modal).click()  
    
    def click_on_logout_button(self):
        self.driver.find_element(By.XPATH, HomePageLocators.button_for_logout).click()
        
    
    # Login Modal
    def click_to_open_microsoft_login_page(self):
        self.driver.find_element(By.XPATH, HomePageLocators.button_for_login_using_madrasati).click()
        pageObject = MicrosoftLoginPage(self.driver)
        return pageObject    
    