import re, urllib
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

link = 'https://l3com.taleo.net/careersection/l3_ext_us/jobsearch.ftl'

class SomeScraper(object):
    def __init__(self):
        self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(1120, 550)

    def scrape(self):
        jobs = self.scrape_job_links()
        for job in jobs:
          print(job.title, job.location)
        self.driver.quit()

    def scrape_job_links(self):
        self.driver.get(link)
        self.driver.implicitly_wait(10)
        self.driver.save_screenshot('screen.png')
        jobs = []

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
            location = td[2].text
            title = a.text
            job['location'] = location
            job['title'] = title
            jobs.append(job)
            # print(job)
        return jobs

def main():
    scraper = SomeScraper()
    scraper.scrape()


if __name__ == '__main__':
    main()


