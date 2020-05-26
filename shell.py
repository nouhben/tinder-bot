bot.driver.get('https://tinder.com/')
sleep(2)
#more_opt_btn = bot.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/button')
#more_opt_btn.click();
#fb_btn = bot.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/div[3]/button')
fb_btn = bot.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
fb_btn.click()
#swicth to login popup
base_window = bot.driver.window_handles[0];
bot.driver.switch_to.window(bot.driver.window_handles[1])

username_input = bot.driver.find_element_by_xpath('//*[@id="email"]')
password_input = bot.driver.find_element_by_xpath('//*[@id="pass"]')
login_btn = bot.driver.find_element_by_xpath('//*[@id="u_0_0"]')
username_input.send_keys(username)
password_input.send_keys(password)
#go back to the main window
bot.driver.switch_to.window(base_window)
cookies = bot.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button');
cookies.click();
#sleep(10)
location = bot.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
location.click()
sleep(4)
login_btn.click()
