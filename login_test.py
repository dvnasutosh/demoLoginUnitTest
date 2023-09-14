
import chromedriver_autoinstaller
import pandas as pd
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
        self.option.add_argument('--headless') if headless else ''
        
        # Initiating the driver
        self.driver = webdriver.Chrome(options=self.option,keep_alive=True)
        
    def login(self,username:str, password:str) -> webdriver.Chrome:
        self.driver.get('https://www.saucedemo.com/')
        # if self.driver.current_url!='https://www.saucedemo.com/' or not stay else None
        

        wait = WebDriverWait(self.driver, 10)

        # Wait till the the elements are present

        uEl = wait.until(EC.presence_of_element_located((By.ID, 'user-name')))
        pEl = wait.until(EC.presence_of_element_located((By.ID, 'password')))
        
        uEl.send_keys(username)
        pEl.send_keys(password)

        self.driver.set_page_load_timeout(60)
        self.driver.find_element(value='login-button').click()
        
        self.driver.implicitly_wait(10)
        try:
            E:webdriver.Remote._web_element_cls=wait.until(
                EC.any_of(
                    EC.url_to_be('https://www.saucedemo.com/inventory.html'),
                    EC.visibility_of_element_located((By.CSS_SELECTOR,'#login_button_container > div > form > div.error-message-container.error > h3')))
                    )
        except TimeoutError:
            return None
        
        if E==True:
            return True
        elif E.get_attribute('data-test'):
            
            return False
        else:
            
            return None
    

def LoginTest(**data):
    log=autoLogin(headless=False)
    result=pd.DataFrame(columns=['name','password','success'])
    
    for username,password in data.items():
        result.loc[result.__len__()] = [username,password,log.login(username,password)]
        # sleep(1)
        # {'name':username,
        # 'password': password,
        # 'success': }
    return result
# r=autoLogin(headless=False).login('standard_user','secret_sauce')

# a SMALL SAMPLE TEST HERE
print(LoginTest(usern='asu',xyz='asuuu',standard_user='secret_sauce',dui='sdfgc'))