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
        assert dashboard.get_profile_name() == "Dashboard Explore"

    def test_email_empty(self, browser):
        login_page = LoginPage(browser)
        login_page.load()
        login_page.set_email("")
        login_page.click_next_button()
        assert login_page.get_alert() == "Enter your email address to continue"

    def test_email_invalid(self,browser):
        login_page = LoginPage(browser)
        login_page.load()
        login_page.set_email("misteraladin_gmail.com")
        login_page.click_next_button()
        assert login_page.get_alert() == "That email address isn't correct"

    def test_password_empty(self, browser):
        login_page = LoginPage(browser)
        login_page.load()
        login_page.set_email("misteraladinqa@gmail.com")
        login_page.click_next_button()
        login_page.click_sign_button()
        assert login_page.get_alert() == "Enter your password"

    def test_password_invalid(self, browser):
        login_page = LoginPage(browser)
        login_page.load()
        login_page.set_email("misteraladinqa@gmail.com")
        login_page.click_next_button()
        login_page.set_password("djfhbjdbfgujsb")
        login_page.click_sign_button()
        assert login_page.get_alert() == "The email and password you entered don't match"

    def test_copy(self, browser):
        login_page = LoginPage(browser)
        dashboard = DashboardPage(browser)
        login_page.load()
        login_page.set_email("misteraladinqa@gmail.com")
        login_page.click_next_button()
        login_page.click_sign_button()
        assert dashboard.get_profile_name() == "Dashboard Explore"




    # def test_unregistered_email(self, browser):
    #     login_page = LoginPage(browser)
    #     dashboard = DashboardPage(browser)
    #     login_page.load()
    #     login_page.set_email("mister@gmail.com")
    #     login_page.click_next_button()
    #     assert dashboard.get_profile_name() == "Dashboard Explore"


