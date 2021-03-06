# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestUntitled():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_untitled(self):
    self.driver.get("https://staging-partner-explore.misterb2b.com/login")
    self.driver.set_window_size(1260, 971)
    self.driver.find_element(By.ID, "ui-sign-in-email-input").click()
    self.driver.find_element(By.ID, "ui-sign-in-email-input").send_keys("misteraladinqa@gmail.com")
    self.driver.find_element(By.CSS_SELECTOR, ".firebaseui-id-submit").click()
    self.driver.find_element(By.ID, "ui-sign-in-password-input").send_keys("@MisterA1")
    self.driver.find_element(By.CSS_SELECTOR, ".firebaseui-id-submit").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".Vue-Toastification__toast-body").text == "Logging in"
  
