from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Locators.MicrosoftLoginPageLocators import MicrosoftLoginPageLocators

class MicrosoftLoginPage():
    
    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        self.driver.find_element(By.XPATH,MicrosoftLoginPageLocators.textbox_for_email).clear()
        self.driver.find_element(By.XPATH, MicrosoftLoginPageLocators.textbox_for_email).send_keys(email)
        
    def click_next_to_password_page(self):
        self.driver.find_element(By.XPATH, MicrosoftLoginPageLocators.button_for_next_to_password).click()        
            
    def enter_password(self, password):
        self.driver.find_element(By.XPATH, MicrosoftLoginPageLocators.textbox_for_password).clear()
        self.driver.find_element(By.XPATH, MicrosoftLoginPageLocators.textbox_for_password).send_keys(password)
    
    def click_login_button(self):
        self.driver.find_element(By.XPATH, MicrosoftLoginPageLocators.button_for_signin).click() 
        
    def is_stay_signed_in_present(self):
        element_present = self.is_element_present(By.XPATH, MicrosoftLoginPageLocators.div_for_stay_signed_in_question)
        return element_present
    
    def stay_signed_in(self, decision):
        if decision == 'yes':
            self.driver.find_element(By.XPATH, MicrosoftLoginPageLocators.button_for_agreeing_on_stay_signed_in).click()
        elif decision == 'no':
            self.driver.find_element(By.XPATH, MicrosoftLoginPageLocators.button_for_declining_stay_signed_in).click()
    
    def check_error_message(self):
        errorMessageXPATH = "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[1]/div"
        if self.is_element_present(By.XPATH, errorMessageXPATH):
            return True
        else:
            return False