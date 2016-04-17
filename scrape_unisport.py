from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from selenium import webdriver
import datetime, sys


def main():
    args = sys.argv[1:]
    gym_class = 'Zumba'
    if args:
        gym_class = args[0].capitalize()
        try:
            day = args[1]
        except:
            pass
    driver = webdriver.PhantomJS() # or add to your PATH
    driver.set_window_size(1024, 768) # optional
    driver.implicitly_wait(3)
    # print(datetime.date.today()-datetime.timedelta(days=1))
    this_day = datetime.date.today() - datetime.timedelta(days=1)
    driver.get('https://unisport.fi/?page=varaapalveluita&subpage=ryhmaliikunta#campuses=o&date=%s' % (this_day))
    # driver.save_screenshot('screen.png') # save a screenshot to disk
    # print(driver.page_source)

    elems = driver.find_elements_by_xpath('//span[contains(text(), "%s")]' % (gym_class, ) )
    # print(elems[0].text, elems[1])
    # print(gym_class)
    for elem in elems:
        father = elem.find_element_by_xpath('..')
        granddad = father.find_element_by_xpath('..')
        class_status = granddad.get_attribute('class')
        # print(father.tag_name, father.text)
        # print(elem.tag_name, elem.text)
        location = father.find_element_by_xpath(".//span[@class='venue']").text
        if location == 'Otahalli':
            if 'fullBooked' in class_status:
                print("Still booked")
            else:
                print("Go book it!")

    driver.close()

if __name__ == '__main__':
    main()