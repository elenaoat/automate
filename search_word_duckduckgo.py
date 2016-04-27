from selenium import webdriver

driver = webdriver.PhantomJS()
# to solve the current bug
# driver.set_window_size(1120, 550)
driver.get("https://duckduckgo.com")
driver.find_element_by_id('search_form_input_homepage').send_keys('phantomjs')
driver.find_element_by_id('search_button_homepage').click()
print(driver.current_url)
driver.quit()