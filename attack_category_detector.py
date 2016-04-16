from attack import Attack
from session_fixation_attack import SessionFixationAttack
from session_hijacking_attack import SessionHijackingAttack

class AttackCategoryDetector(object):
  def __init__(self, attack_specs):
    """Return a Attack_category_detector object."""
    self.attacks_list = []
    for index, attack in enumerate(attack_specs):
      if attack["cookie"][0]["attack"][0].strip() == "sessionFixation":
        self.attacks_list.append(SessionFixationAttack(attack["link"], attack["form_parameter"], attack["button"], attack["cookie"]))
      elif attack["cookie"][0]["attack"][0].strip() == "sessionHijacking":
        self.attacks_list.append(SessionHijackingAttack(attack["link"], attack["form_parameter"], attack["button"], attack["cookie"]))
      elif attack["cookie"][0]["attack"][0].strip() == "predictableCookies":
        self.attacks_list.append(Attack(attack["link"], attack["form_parameter"], attack["button"], attack["cookie"], "predictableCookies"))

  def get_attacks_list(self):
    return self.attacks_list


# from selenium import webdriver
# url = "http://app1.com"
# wd = webdriver.Chrome()

# wd.get(url)

# # enable input and submit button
# wd.execute_script("document.getElementsByTagName('input')[0].disabled = false")
# wd.execute_script("document.getElementsByTagName('input')[1].disabled = false")

# # fill in -1 value in input and submit
# wd.find_element_by_css_selector("input[type='text']").send_keys(-1)
# wd.find_element_by_css_selector("form").submit()
