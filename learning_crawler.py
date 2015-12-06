import urllib
from selenium import webdriver


profile_link = 'https://www.instagram.com/gothamonfox/'


class InstagramScrapper(object):

    def __init__(self):
        self.driver = webdriver.PhantomJS(
            executable_path='/home/hassan/phantomjs/phantomjs')
        self.driver.set_window_size(1120, 550)

    def scrape_profile(self):
        """ Scrape Instagram prfile picture href link and than download it """
        self.driver.get(profile_link)
        print self.driver.title

        xpath_for_img_tag = "//div[@class='i38']/img"

        # quering using xpath and than getting first element of list
        src_url_to_dp = self.driver.find_elements_by_xpath(
            xpath_for_img_tag)[0]

        urllib.urlretrieve(src_url_to_dp.get_attribute(
            "src"), "profile-pic.jpg")

    def scrape(self):
        self.scrape_profile()


if __name__ == '__main__':
    scraper = InstagramScrapper()
    scraper.scrape()
