from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC


class LoginPage():
    #Locator
    EMAIL = (By.ID, "ui-sign-in-email-input")
    BUTTON_NEXT = (By.CSS_SELECTOR, ".firebaseui-id-submit")
    PASSWORD = (By.ID,"ui-sign-in-password-input")
    Button_SIGN_IN = (By.XPATH, "//button[contains(text(),'Sign In')]")
    ALERT_ERROR = (By.CSS_SELECTOR, ".firebaseui-error")
    EMAIL_INVALID = (By.CSS_SELECTOR, ".firebaseui-id-email-error")
    # PASSWORD_INVALID = (By.CSS_SELECTOR,".firebaseui-id-password-error")
    PASSWORD_INVALID = (By.XPATH,"//p[contains(text(),'You have entered an incorrect password too many ti')]")

    #method constructor
    def __init__(self, browser:webdriver.Remote):
        self.driver = browser
    #open
    def load(self):
        self.driver.get("https://staging-partner-explore.misterb2b.com/login")

    #Method
    def set_email(self, email):
        email_field = self.driver.find_element(*self.EMAIL)
        email_field.send_keys(email)

    def click_next_button(self):
        next_button = self.driver.find_element(*self.BUTTON_NEXT)
        next_button.click()

    def set_password(self, password):
        # password_field = self.driver.find_element(*self.PASSWORD)
        password_field = WebDriverWait(self.driver, 3000).until(EC.presence_of_element_located(self.PASSWORD))
        password_field.send_keys(password)

    def set_password_validate(self, password):
        password_field = self.driver.find_element(*self.PASSWORD)
        password_field.send_keys(password)

    def click_sign_button(self):
        sign_button = self.driver.find_element(*self.Button_SIGN_IN)
        sign_button.click()

    def get_alert(self):
        text_input_error = self.driver.find_element(*self.ALERT_ERROR)
        return text_input_error.text

    def get_alert_password(self):
        text_input_error = self.driver.find_element(*self.PASSWORD_INVALID)
        return text_input_error.text

    # def get_email_incorrect(self):
    #     get_email_incorrect = self.driver.find_element(*self.EMAIL_INVALID)
    #     return get_email_incorrect.text




