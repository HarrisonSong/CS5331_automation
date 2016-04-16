from attack import Attack
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SessionHijackingAttack(Attack):
  def __init__(self, link, form_parameter, button, cookie):
    super(SessionHijackingAttack, self).__init__(link, form_parameter, button, cookie, "session_hijacking")

  def perform(self):
    print "start session_hijacking_attack."
    wd = webdriver.Chrome()

    wd.get(self.link[0])
    wd.find_element_by_css_selector("input[name=" + self.form_parameter[0]["account"] + "]").send_keys(self.form_parameter[0]["account_value"])
    wd.find_element_by_css_selector("input[name=" + self.form_parameter[0]["password"] + "]").send_keys(self.form_parameter[0]["password_value"])
    wd.find_element_by_css_selector("input[value=" + self.button[0] + "]").click()
    fixed_cookie = ""
    for cookie in wd.get_cookies():
        if cookie["name"] == self.cookie[0]["name"]:
            fixed_cookie = cookie["value"]
            break
    print fixed_cookie

    WebDriverWait(wd, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
