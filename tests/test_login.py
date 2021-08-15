from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboar_page import DashboardPage

class TestLogin():

    def test_valid_login(self, browser):
        login_page = LoginPage(browser)
        dashboard = DashboardPage(browser)
        login_page.load()
        login_page.set_email("misteraladinqa@gmail.com")
        login_page.click_next_button()
        login_page.set_password("@MisterA1")
        login_page.click_sign_button()
        # dashboard.wait_toast_login()
        assert dashboard.get_toast_login() == "Logging in"

    def test_email_empty(self, browser):
        login_page = LoginPage(browser)
        login_page.load()
        login_page.set_email("")
        login_page.click_next_button()
        assert login_page.get_email_incorrect() == "Enter your email address to continue"

    def test_email_invalid(self,browser):
        login_page = LoginPage(browser)
        login_page.load()
        login_page.set_email("misteraladin_gmail.com")
        login_page.click_next_button()
        assert login_page.get_email_incorrect() == "That email address isn't correct"

    def test_password_empty(self, browser):
        login_page = LoginPage(browser)
        login_page.load()
        login_page.set_email("misteraladinqa@gmail.com")
        login_page.click_next_button()
        login_page.set_password("")
        login_page.click_sign_button()
        assert login_page.get_password_invalid() == "Enter your password"

    #wip
    def test_password_invalid(self, browser):
        login_page = LoginPage(browser)
        login_page.load()
        login_page.set_email("adminqa1@gmail.com")
        login_page.click_next_button()
        login_page.set_password("asdfasdfasdf;ljdf")
        login_page.click_sign_button()
        assert login_page.get_password_invalid() == "The email and password you entered don't match"

    def test_entered_invalid_password_to_many_times(self, browser):
        login_page = LoginPage(browser)
        login_page.load()
        login_page.set_email("misteraladinqa@gmail.com")
        login_page.click_next_button()
        login_page.set_password("djfhbjdbfgujsb")
        login_page.set_password_clear("")


        # login_page.click_sign_button()
        # assert login_page.get_password_invalid_repeat() == "The email and password you entered don't match"









