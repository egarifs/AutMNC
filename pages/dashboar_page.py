from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

class DashboardPage():
    TOAST_LOGIN_SUCCES = (By.CSS_SELECTOR, "Vue-Toastification__toast-body")
    PROFILE_NAME = (By.CSS_SELECTOR,"h1.font-bold.text-3xl")
    TOAST_LOGIN_WAIT = (By.XPATH, "/html/body/div[3]/div[3]/div/div")
    TOAST_LOGIN = (By.XPATH, "/html/body/div[3]/div[3]/div/div/div[1]")



    def __init__(self, browser: webdriver.Remote):
        self.driver = browser

    def get_profile_name(self):
        # title_toast = WebDriverWait(self.driver, 3000).until(EC.presence_of_element_located(self.PROFILE_NAME))
        title_toast = self.driver.find_element(*self.PROFILE_NAME)
        return title_toast.text

    def get_toast_login(self):
        toast_login = self.driver.find_element(*self.TOAST_LOGIN)
        return  toast_login.get_attribute("innerHTML")

    def wait_toast_login(self):
        toast_login_wait = WebDriverWait(self.driver, 3000).until(EC.presence_of_element_located(*self.TOAST_LOGIN_WAIT))
        toast_login_wait
        return  toast_login_wait
