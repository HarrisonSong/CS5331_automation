from attack import Attack
class SessionHijackingAttack(Attack):
  def __init__(self, link, form_parameter, button, cookie):
    super(SessionHijackingAttack, self).__init__(link, form_parameter, button, cookie, "session_hijacking")

  def perform(self):
    from selenium import webdriver
    print "start session_hijacking_attack."
    # url = "http://app1.com"
    # wd = webdriver.Chrome()

    # wd.get(url)

    # # enable input and submit button
    # wd.execute_script("document.getElementsByTagName('input')[0].disabled = false")
    # wd.execute_script("document.getElementsByTagName('input')[1].disabled = false")

    # # fill in -1 value in input and submit
    # wd.find_element_by_css_selector("input[type='text']").send_keys(-1)
    # wd.find_element_by_css_selector("form").submit()
