import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")
def setup(request):
    # Get the path to the parent folder inside the project folder
    parent_folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    # Specify the relative path to the WebDriver inside the parent folder
    webdriver_path = os.path.join(parent_folder_path, "Drivers/chromedriver.exe")

    # Use the relative path to create the Service object
    service_obj = Service(webdriver_path)
    
    # Set up the WebDriver
    driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver

    yield driver  # This is the value that the test function receives
    
    # Code after 'yield' is the teardown code
    driver.close()
    driver.quit()

