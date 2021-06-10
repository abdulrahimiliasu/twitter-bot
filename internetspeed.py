from selenium import webdriver
import time


class InternetSpeed:

    def __init__(self):

        try:
            driver_path = ''
            driver = webdriver.Chrome(executable_path=driver_path)
            driver.get('https://www.speedtest.net')
            time.sleep(2)
            go = driver.find_element_by_class_name('start-text')
            go.click()
            time.sleep(60)
            self.ping = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
            self.download = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
            self.upload = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        except:
            driver.quit()

    def get_pings(self):
        return self.ping.text

    def get_download_speed(self):
        return self.download.text

    def get_upload_speed(self):
        return self.upload.text
