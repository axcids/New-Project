# Import Tools 
from selenium.webdriver.support import expected_conditions as EC
import time
# Import modules
from Pages.HomePage import HomePage

class Test_Login_Options (): 

    def test_case_1_positive_login_by_madrasati(self, setup):
        # Open URL 
        self.driver.get("https://exam-stg-web.moe.gov.sa/")
        # Create instances of the pages 
        homePage = HomePage(self.driver)
        
        # Home Page Steps
        homePage.click_on_login_button()
        loginByMadrasati = homePage.click_to_open_microsoft_login_page()
        
        # Microsoft Login Steps
        loginByMadrasati.enter_email("T4eduTestStud139@nthb.moe.gov.sa")
        loginByMadrasati.click_next_to_password_page()
        loginByMadrasati.enter_password("TPwd@9090%#!@")
        loginByMadrasati.click_login_button()
        # Check if the stay signed in option presented or not
        if loginByMadrasati.is_stay_signed_in_present :
            # Click yes to pass the page 
            loginByMadrasati.stay_signed_in('no')
    
    def test_case_2_negative_login_by_madrasati(self, setup):
        # Open URL 
        self.driver.get("https://exam-stg-web.moe.gov.sa/")
        # Create instances of the pages 
        homePage = HomePage(self.driver)
        
        # Home Page Steps
        homePage.click_on_login_button()
        loginByMadrasati = homePage.click_to_open_microsoft_login_page()
        
        # Microsoft Login Steps
        loginByMadrasati.enter_email("T4eduTestStud139@nthb.moe.gov.sa")
        loginByMadrasati.click_next_to_password_page()
        loginByMadrasati.enter_password("TPwd@9090%#!@1")
        loginByMadrasati.click_login_button()
        time.sleep(3)
        assert loginByMadrasati.check_error_message(), "Error message did not appear to the user."        
        