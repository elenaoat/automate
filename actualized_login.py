from selenium import webdriver
import requests
from bs4 import BeautifulSoup

def main():
    # html = requests.url('actualized.org/forum')
    driver = webdriver.PhantomJS()
    driver.set_window_size(1125, 550)
    driver.get('http://www.actualized.org/forum/')
    driver.implicitly_wait(5)
    driver.save_screenshot('screen.png')
    soup = BeautifulSoup(driver.page_source, "html.parser")
    # print(soup.prettify())
    a = soup.find_all('a', id="elUserSignIn")
    for i in a:
        print(a)


if __name__ == '__main__':
    main()