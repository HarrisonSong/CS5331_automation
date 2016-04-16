from selenium import webdriver
url = "http://app1.com"
wd = webdriver.Chrome()

wd.get(url)

# enable input and submit button
wd.execute_script("document.getElementsByTagName('input')[0].disabled = false")
wd.execute_script("document.getElementsByTagName('input')[1].disabled = false")

# fill in -1 value in input and submit
wd.find_element_by_css_selector("input[type='text']").send_keys(-1)
wd.find_element_by_css_selector("form").submit()
