from twitterUserInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class Twitter:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://twitter.com/i/flow/login")
        time.sleep(2)

        self.browser.find_element(By.XPATH, '//input[@name="text"]').send_keys(self.username)
        time.sleep(2)
        self.browser.find_element(By.XPATH,'//span[contains(text(),"İleri")]').click()
        time.sleep(2)
        self.browser.find_element(By.NAME, 'password').send_keys(self.password)
        self.browser.find_element(By.XPATH,'//span[contains(text(),"Giriş yap")]').click()
        time.sleep(2)

    def searchInput(self,hashtag):
        search = self.browser.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')
        search.send_keys(hashtag)
        time.sleep(2)
        search.send_keys(Keys.ENTER)
        time.sleep(2)

        results = []

        tweets = self.browser.find_elements(By.XPATH,'//div[@data-testid="tweetText"]')
        time.sleep(2)
        print(str(len(tweets)))

        for i in tweets:
            results.append(i.text)

        loop_counter  = 0
        last_height = self.browser.execute_script('return document.documentElement.scrollHeight')
        
        while True:
            if loop_counter > 3:
                break
            self.browser.execute_script('window.scrollTo(0,document.documentElement.scrollHeight);')
            time.sleep(2)
            new_height = self.browser.execute_script('return document.documentElement.scrollHeight')
            if last_height == new_height:
                break
            last_height = new_height
            loop_counter += 1

            tweets = self.browser.find_elements(By.XPATH,'//div[@data-testid="tweetText"]')
            time.sleep(2)
            print(str(len(tweets)))

            for i in tweets:
                results.append(i.text)

        count = 1
        with open ("tweets.txt","w") as file:
            for item in results:
                file.write(item+"\n")
                count +=1
        # count = 1
        # for item in results:
        #     print("*******")
        #     print(tweet)

twt = Twitter(username,password)
twt.signIn()
twt.searchInput('Beşiktaş')