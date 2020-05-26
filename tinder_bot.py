from selenium import webdriver
from time import sleep
from cred import username,password
class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com/')
        cookies = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button');
        cookies.click();
        sleep(2)
        #more_opt_btn = bot.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/button')
#more_opt_btn.click();
#fb_btn = bot.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/div[3]/button')
        fb_btn = bot.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        fb_btn.click()
        #swicth to login popup
        base_window = self.driver.window_handles[0];
        self.driver.switch_to.window(self.driver.window_handles[1])
        username_input = self.driver.find_element_by_xpath('//*[@id="email"]')        
        password_input = self.driver.find_element_by_xpath('//*[@id="pass"]')
        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_btn.click()
        #go back to the main window
        self.driver.switch_to.window(base_window)
        #get through popups
        sleep(20)
        location = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]');
        location.click();
        sleep(5)
        notifications = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]');
        notifications.click();
       #add //*[@id="modal-manager"]/div/div/div[2]/button[2]
        
    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()
    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()
    def auto_swip(self):
        while True:
            sleep(1)
            self.like()
            #sleep(0.5)
            #self.dislike()


bot = TinderBot();
bot.login();