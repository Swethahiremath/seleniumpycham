from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
class MyListeners(AbstractEventListener) :
    def before_navigate_to(self, url, driver):
        print("before navigate to")

    def after_navigate_to(self, url, driver) :
        print("after_navigate_to")

    def before_change_value_of(self, element, driver):
        print("before changing the values ")

    def after_change_value_of(self, element, driver):
        print("after changing the values")

    def before_click(self, element, driver):
        print("Before click ")

    def after_click(self, element, driver):
        print("After click")

    def before_find(self, by, value, driver):
        print("Before_find_")

    def after_find(self, by, value, driver):
        print("After find")

    def before_navigate_back(self, driver):
        print("before_navigate_back")

    def after_navigate_back(self, driver):
        print("After_navigate_back")

    def before_execute_script(self, script, driver):
        print("before_execute_script")

    def after_execute_script(self, script, driver):
        print("after_execute_script")

    def before_close(self, driver):
        print("before_close")

    def after_close(self, driver):
        print("after_close")

    def before_quit(self, driver):
        print("before_quit")

    def after_quit(self, driver):
        print("after_quite")

    def before_navigate_forward(self, driver):
        print("before_navigate_forward")

    def after_navigate_forward(self, driver):
        print("after_navigate_forward")

    def before_on_exception(self,exception,driver):
        print("Before execuption")

    def after_on_exception(self,exception,driver):
        print("After_exception")
        driver.save_screeshot("error.png")
