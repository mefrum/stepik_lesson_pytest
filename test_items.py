from selenium.webdriver.support import expected_conditions as EC
link = "http://selenium1py.pythonanywhere.com/{}/catalogue/coders-at-work_207/"


class TestOscarSandBox:

    def test_add_to_basket_should_be_present(self, browser, language):
        browser.get(link.format(language))
        #time.sleep(10)
        add_to_basket = browser.find_elements_by_css_selector("button.btn-add-to-basket")

        assert EC.visibility_of(add_to_basket), "Button add to basket not found"
