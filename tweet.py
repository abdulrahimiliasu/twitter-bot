from selenium import webdriver
import time


class TwitterBot:

    def __init__(self, tweet, username, passowrd):
        driver_path = ''
        driver = webdriver.Chrome(executable_path=driver_path)
        driver.get('https://twitter.com')

        time.sleep(1)
        log_in = driver.find_element_by_link_text('Log in')
        log_in.click()
        time.sleep(2)
        user = driver.find_element_by_name('session[username_or_email]')
        user.send_keys(username)
        pass_ = driver.find_element_by_name('session[password]')
        pass_.send_keys(passowrd)
        log_inn = driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div')
        log_inn.click()
        time.sleep(5)
        tweet_b = driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
        tweet_b.click()
        time.sleep(2)
        tweet_msg = driver.find_element_by_xpath(
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet_msg.send_keys(tweet)
        tweet_final = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[2]/div[4]/div/span/span')
        tweet_final.click()
        time.sleep(5)
        driver.quit()
