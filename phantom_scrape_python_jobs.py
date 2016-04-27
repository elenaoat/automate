import re, urllib
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
link = 'https://l3com.taleo.net/careersection/l3_ext_us/jobsearch.ftl'

class SomeScraper(object):
    def __init__(self):
        self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(1120, 550)

    def scrape(self):
        jobs = self.scrape_python_job_links()
        for job in jobs:
          print(job['title'], job['location'])
        self.driver.close()
        self.driver.quit()

    def scrape_python_job_links(self):
        self.driver.get(link)
        self.driver.implicitly_wait(5)
        jobs = []
        self.driver.find_element_by_id('KEYWORD').send_keys('python')
        self.driver.find_element_by_id('search').click()
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'jobs'))
            )
        finally:
            pass
        # self.driver.implicitly_wait(20)
        self.driver.save_screenshot('screen.png')
        # print(dir(self.driver))
        html = self.driver.page_source
        s = BeautifulSoup(html, "html.parser")
        # print(s.prettify())
        # /careersection/l3_ext_us/jobdetail.ftl?job=080695
        r = re.compile(r'\/careersection\/l3_ext_us\/jobdetail\.ftl\?job=\d+$')
        # print(r, type(r))
        # print(s.find_all('a'))
        # print(s.find_all('a', href=r))
        for a in s.find_all('a', href=r):
            job = {}
            tr = a.find_parent('tr')
            td = tr.find_all('td')
            location = td[1].text
            title = a.text
            job['location'] = location
            job['title'] = title
            jobs.append(job)
            # print(location)
        return jobs

def main():
    scraper = SomeScraper()
    scraper.scrape()


if __name__ == '__main__':
    main()


