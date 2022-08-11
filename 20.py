from selenium import webdriver
from time import sleep
# my_driver = webdriver.Chrome(executable_path="D:/Do_not_delete/DevOpsExperts/Lesson4_21072022/selenium_for
# _chrome_103_major_ver/chromedriver.exe") #  This gives warning for deprecated unction


my_driver = webdriver.Chrome()  # if in system32 no need in path
#my_driver.get("https://github.com")
#for i in range(5):
#    sleep(5)
#    my_driver.refresh()
#my_driver.close()

# Test in selenium to check the web application
my_driver.get("file://D:/Do_not_delete/DevOpsExperts/Lesson4_21072022/tip_calc/tip_calc/index.html")
my_driver.find_element(by="id", value="billamt").send_keys("100")
my_driver.find_element(by="xpath", value='//*[@id="serviceQual"]/option[4]').click()
my_driver.find_element(by="id", value='peopleamt').send_keys("5")
my_driver.find_element(by="id", value='serviceMusic').send_keys("5")
my_driver.find_element(by="xpath", value='//*[@id="calculate"]').click()
expected = "8.00"
expected = "3"
actual = my_driver.find_element(by="id", value='tip').text


assert expected == actual
