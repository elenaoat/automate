from selenium import webdriver
from bs4 import BeautifulSoup


def main():
    driver = webdriver.PhantomJS()
    driver.get('http://www.american-steel.com/wp/')
    driver.set_window_size(1120, 550)
    s = BeautifulSoup(driver.page_source, 'html.parser')
    addresses = s.find_all('address')
    for i, a in enumerate(addresses):
        f = a.text.split('\n')
        # print(f)
        print('Address', f[0])
        print('City', f[1])
        print('Phone', f[2])

    driver.close()
    driver.quit()

if __name__ == '__main__':
    main()