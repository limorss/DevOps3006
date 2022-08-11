from selenium import webdriver

my_driver = webdriver.Chrome()
print("Run Selenium test on Google site ....")
my_driver.get('http://www.google.com')
actual_result = my_driver.title
expected_result = 'Google'
my_driver.close()
assert actual_result == expected_result
print('Test passed!')
