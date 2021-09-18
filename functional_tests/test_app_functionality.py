from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

# Own
from setup_docker import create_tasks, create_super_user, create_blank_user_solution_file

sleep(5)


class TestStartingPageFunctionality(StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Remote("http://education-platform-for-pythoneers-tests:4444/wd/hub",
                          desired_capabilities=DesiredCapabilities.CHROME)
        self.browser.get('http://education-platform-for-pythoneers-app:8000')

    def tearDown(self) -> None:
        self.browser.close()

    def test_if_first_word_in_welcome_page_is_display_correctly(self) -> None:
        welcome_text_first_word: str = self.browser.find_element_by_tag_name("div").text
        self.assertEquals(welcome_text_first_word, "Tasks")

    def test_if_href_on_starting_page_in_main_text_redirects_to_main_page(self) -> None:
        main_page_url = self.browser.current_url + "main-page/"
        self.browser.find_element_by_tag_name("a").click()
        self.assertEquals(self.browser.current_url, main_page_url)


class TestMainPageFunctionality(StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Remote("http://education-platform-for-pythoneers-tests:4444/wd/hub",
                          desired_capabilities=DesiredCapabilities.CHROME)
        self.browser.get('http://education-platform-for-pythoneers-app:8000/main-page/')

    def tearDown(self) -> None:
        self.browser.close()

    def test_if_main_header_content_display_correctly(self) -> None:
        main_header_content: str = self.browser.find_element_by_tag_name("div").text
        self.assertEquals(main_header_content, "Ranking\nRegister\nLog In")

    def test_if_href_in_main_header_with_text_name_ranking_redirect_to_ranking_page(self) -> None:
        ranking_page_url = "http://education-platform-for-pythoneers-app:8000/ranking/"
        self.browser.find_element_by_link_text("Ranking").click()
        self.assertEquals(self.browser.current_url, ranking_page_url)

    def test_if_href_in_main_header_with_text_name_register_redirect_to_registration_page(
            self,
    ) -> None:
        registration_page_url = "http://education-platform-for-pythoneers-app:8000/accounts/register/"
        self.browser.find_element_by_link_text("Register").click()
        self.assertEquals(self.browser.current_url, registration_page_url)

    def test_if_href_in_main_header_with_text_name_log_in_redirect_to_log_in_page(self) -> None:
        log_in_page_url = "http://education-platform-for-pythoneers-app:8000/accounts/login/"
        self.browser.find_element_by_link_text("Log In").click()
        self.assertEquals(self.browser.current_url, log_in_page_url)


class TestLogInPageFunctionality(StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Remote("http://education-platform-for-pythoneers-tests:4444/wd/hub",
                          desired_capabilities=DesiredCapabilities.CHROME)
        self.browser.get('http://education-platform-for-pythoneers-app:8000/accounts/login/')
        self.user_name = self.browser.find_element_by_name("username")
        self.password = self.browser.find_element_by_name("password")
        self.log_in_button = self.browser.find_element_by_tag_name("button")

    def tearDown(self) -> None:
        self.browser.close()

    def test_log_in_form_unknown_user(self) -> None:
        self.user_name.send_keys("tester")
        self.password.send_keys("test123456")
        self.log_in_button.send_keys(Keys.RETURN)
        self.assertEquals(self.browser.title, "Login Page")

    def test_log_in_form_already_register_user(self) -> None:
        create_super_user()
        self.user_name.send_keys("root")
        self.password.send_keys("toor123456")
        self.log_in_button.send_keys(Keys.RETURN)
        self.assertEquals(self.browser.title, "All Challenges")


class TestRegisterPageFunctionality(StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Remote("http://education-platform-for-pythoneers-tests:4444/wd/hub",
                          desired_capabilities=DesiredCapabilities.CHROME)
        self.browser.get('http://education-platform-for-pythoneers-app:8000/accounts/register/')
        self.user_name = self.browser.find_element_by_name("username")
        self.password1 = self.browser.find_element_by_name("password1")
        self.password2 = self.browser.find_element_by_name("password2")
        self.register_button = self.browser.find_element_by_tag_name("button")

    def tearDown(self) -> None:
        self.browser.close()

    def test_if_user_without_user_name_can_register(self) -> None:
        self.user_name.send_keys("")
        self.password1.send_keys("test1234567")
        self.password2.send_keys("test1234567")
        self.register_button.send_keys(Keys.RETURN)
        self.assertEquals(self.browser.title, "Register Page")

    def test_if_user_with_user_name_but_without_password1_password2_can_register(self) -> None:
        self.user_name.send_keys("tester")
        self.password1.send_keys("")
        self.password2.send_keys("")
        self.register_button.send_keys(Keys.RETURN)
        self.assertEquals(self.browser.title, "Register Page")

    def test_if_user_with_user_name_but_without_password1_can_register(self) -> None:
        self.user_name.send_keys("tester")
        self.password1.send_keys("")
        self.password2.send_keys("test1234567")
        self.register_button.send_keys(Keys.RETURN)
        self.assertEquals(self.browser.title, "Register Page")

    def test_if_user_with_user_name_but_without_password2_can_register(self) -> None:
        self.user_name.send_keys("tester")
        self.password1.send_keys("test1234567")
        self.password2.send_keys("")
        self.register_button.send_keys(Keys.RETURN)
        self.assertEquals(self.browser.title, "Register Page")

    def test_if_user_with_different_passwords_can_register(self) -> None:
        self.user_name.send_keys("tester")
        self.password1.send_keys("test123456")
        self.password2.send_keys("test1234567")
        self.register_button.send_keys(Keys.RETURN)
        self.assertEquals(self.browser.title, "Register Page")

    def test_if_user_with_too_short_password_can_register(self) -> None:
        self.user_name.send_keys("tester")
        self.password1.send_keys("qwe")
        self.password2.send_keys("qwe")
        self.register_button.send_keys(Keys.RETURN)
        self.assertEquals(self.browser.title, "Register Page")

    def test_if_user_with_all_correct_credentials_can_register(self) -> None:
        self.user_name.send_keys("tester")
        self.password1.send_keys("test1234567")
        self.password2.send_keys("test1234567")
        self.register_button.send_keys(Keys.RETURN)
        self.assertEquals(self.browser.title, "Login Page")


class TestCodeEditorPagePalindromeTaskFunctionality(StaticLiveServerTestCase):
    def setUp(self) -> None:
        create_tasks()
        create_super_user()
        create_blank_user_solution_file()
        self.browser = webdriver.Remote("http://education-platform-for-pythoneers-tests:4444/wd/hub",
                                        desired_capabilities=DesiredCapabilities.CHROME)
        self.browser.get('http://education-platform-for-pythoneers-app:8000/tasks/2')
        user_name = self.browser.find_element_by_name("username")
        password = self.browser.find_element_by_name("password")
        log_in_button = self.browser.find_element_by_tag_name("button")
        user_name.send_keys("root")
        password.send_keys("toor123456")
        log_in_button.send_keys(Keys.RETURN)

    def tearDown(self) -> None:
        self.browser.close()

    def test_user_submit_different_answers_for_task(self) -> None:
        """
        The most important test cases are stored in this function.
        First assert was created to only to make sure if selenium is in right place on site.
        Second assert was created to check what result user get if doesn't change anything is
        solution. Third assert was created to check what result user get if solution will only
        return True. Fourth assert was created to check what result user get if deliver correct
        solution.
        """
        code_area_field = self.browser.find_element_by_id("code_editor")
        self.assertEquals(
            self.browser.title,
            "Palindrome Checker",
            msg="To make sure if selenium" "is in right place on site.",
        )

        code_area_field.clear()
        code_area_field.send_keys("def palindrome(string: str) -> bool:\n\tpass" "")
        check_solution_button = self.browser.find_element_by_id("check-button")
        check_solution_button.click()
        sleep(4)
        test_output: str = self.browser.find_element_by_id("output").text
        self.assertEquals(test_output[:17], "Test results: 0/8", msg="Expected test results: 0/8")

        code_area_field.clear()
        code_area_field.send_keys("def palindrome(string: str) -> bool:\n\treturn True")
        check_solution_button = self.browser.find_element_by_id("check-button")
        check_solution_button.click()
        sleep(4)
        test_output: str = self.browser.find_element_by_id("output").text
        self.assertEquals(test_output[:17], "Test results: 4/8", msg="Expected test results: 4/8")

        code_area_field.clear()
        code_area_field.send_keys(
            "def palindrome(string: str) -> bool:\n\treturn string == string[" "::-1]"
        )
        check_solution_button = self.browser.find_element_by_id("check-button")
        check_solution_button.click()
        sleep(4)
        test_output: str = self.browser.find_element_by_id("output").text
        self.assertEquals(test_output[:17], "Test results: 8/8", msg="Expected test results: 8/8")
