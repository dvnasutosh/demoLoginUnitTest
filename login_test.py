
import chromedriver_autoinstaller

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class autoLogin:
    def __init__(self,headless: bool = True) -> None:
        
        chromedriver_autoinstaller.install() 
        
        # Setting up options
        self.option=Options()
        self.option.headless=headless
        
        # Initiating the driver
        self.driver = webdriver.Chrome(options=self.Option)
        
    def login(self,username:str, password:str):
        self.driver.get