from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class LoginPage():
    #Locator
    EMAIL = (By.ID, "ui-sign-in-email-input")
    EMAIL_EMPTY_ALERT = (By.CSS_SELECTOR, ".firebaseui-id-email-error")
    EMAIL_INVALID = (By.CSS_SELECTOR, ".firebaseui-id-email-error")
    NEXT_BUTTON = (By.CSS_SELECTOR, ".firebaseui-id-submit")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, ".mdl-button--colored")
    BUTTON_SIGN = (By.XPATH, "//button[contains(text(),'Sign In')]")
    PASSWORD = (By.ID,"ui-sign-in-password-input")
    # PASSWORD_ALERT = (By.CSS_SELECTOR,".firebaseui-error.firebaseui-text-input-error.firebaseui-id-password-error")
    # PASSWORD_ALERT = (By.CSS_SELECTOR,"p.firebaseui-id-password-error")
    PASSWORD_ALERT = (By.CSS_SELECTOR,  "//p[contains(text(),'The email and password you entered don't match')]")

    PASSWORD_TO_MANY = (By.XPATH, "//p[contains(text(),'You have entered an incorrect password too many ti')]")

    ALERT_ERROR = (By.CSS_SELECTOR, ".firebaseui-error")

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

    def get_email_incorrect(self):
        get_email_incorrect = self.driver.find_element(*self.EMAIL_INVALID)
        return get_email_incorrect.text

    def click_next_button(self):
        next_button = self.driver.find_element(*self.NEXT_BUTTON)
        next_button.click()

    def set_password(self, password):
        # password_field = self.driver.find_element(*self.PASSWORD)
        password_field = WebDriverWait(self.driver, 3000).until(EC.presence_of_element_located(self.PASSWORD))
        password_field.send_keys(password)

    #clear password
    def set_password_clear(self, password):
        # password_field = self.driver.find_element(*self.PASSWORD)
        password_field = WebDriverWait(self.driver, 3000).until(EC.presence_of_element_located(self.PASSWORD))
        password_field.send_keys(password)
        password_field.clear()


    def set_password_validate(self, password):
        password_field = self.driver.find_element(*self.PASSWORD)
        password_field.send_keys(password)

    def click_sign_button(self):
        sign_button = self.driver.find_element(*self.SIGN_IN_BUTTON)
        sign_button.click()

    def get_email_empty(self):
        email_empty_alert = WebDriverWait(self.driver, 3000).until(EC.presence_of_element_located(self.EMAIL_EMPTY_ALERT))
        return email_empty_alert.text

    def get_password_alert(self):
        text_input_error = self.driver.find_element(*self.PASSWORD_ALERT)
        return text_input_error.text

    def get_password_invalid(self):
        # txt_password_invalid = WebDriverWait(self.driver, 3000).until(EC.presence_of_element_located(self.PASSWORD_ALERT))
        txt_password_invalid = self.driver.find_element(*self.PASSWORD_ALERT)
        return txt_password_invalid.text

    def get_password_invalid_repeat(self):
        txt_password_invalid = self.driver.find_element(*self.PASSWORD_TO_MANY)
        return txt_password_invalid.text











