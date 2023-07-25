from selenium.webdriver.common.by import By
import time

link =' http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_busket_button(browser):
    browser.get(link)
    time.sleep(10)
    add_basket=browser.find_element(By.CSS_SELECTOR,".btn-add-to-basket")
    assert add_basket, 'No add button on page'