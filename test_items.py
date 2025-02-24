import time

def test_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)  # Для визуальной проверки языка
    add_to_basket_button = browser.find_element_by_css_selector("button.btn-add-to-basket")
    assert add_to_basket_button is not None, "Add to basket button is not found"
