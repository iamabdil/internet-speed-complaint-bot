from selenium import webdriver
import time
import os

PROMISED_DOWN = 150.00
PROMISED_UP = 10.00
CHROME_DRIVER_PATH = "/Users/iamabdil/Development/chromedriver"
TWITTER_EMAIL = os.environ['TWITTER_EMAIL']
TWITTER_PASSWORD = os.environ['TWITTER_PASSWORD']


class InternetSpeedTwitterBot():
    def __init__(self, driver_path,):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        consent = self.driver.find_element_by_xpath('//*[@id="_evidon-banner-acceptbutton"]')
        consent.click()

        time.sleep(3)

        go_button = self.driver.\
            find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')

        go_button.click()

        time.sleep(60)

        self.down = float(self.driver\
            .find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)

        self.up = float(self.driver\
            .find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)

        print(self.down)
        print(self.up)

    def tweet_at_provider(self):
        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            self.driver.get('https://twitter.com/login')
            time.sleep(2)
            username_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
            password_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
            login = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div')

            username_input.send_keys(TWITTER_EMAIL)
            password_input.send_keys(TWITTER_PASSWORD)
            login.click()

            time.sleep(5)

            tweet_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
            tweet_input.send_keys(f'hello service provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up')

            tweet_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span')
            tweet_btn.click()

bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)

bot.get_internet_speed()
bot.tweet_at_provider()

