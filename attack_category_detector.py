from attack import Attack
from session_fixation_attack import SessionFixationAttack
from session_hijacking_attack import SessionHijackingAttack
from predictable_cookie_attack import PredictableCookieAttack
import json
import os

class AttackCategoryDetector(object):
  def __init__(self, attack_specs):
    """Return a Attack_category_detector object."""
    self.attacks_list = []
    for index, attack in enumerate(attack_specs):
      if not "button" in attack:
        attack["button"] = '//form//a[@class="button"]'
      if attack["cookie"]["attack"].strip() == "sessionFixation":
        self.attacks_list.append(SessionFixationAttack(attack["link"], attack["form_parameter"], attack["button"], attack["cookie"]))
      elif attack["cookie"]["attack"].strip() == "sessionHijacking":
        self.attacks_list.append(SessionHijackingAttack(attack["link"], attack["form_parameter"], attack["button"], attack["cookie"]))
      elif attack["cookie"]["attack"].strip() == "predictableCookie":
        self.attacks_list.append(PredictableCookieAttack(attack["link"], attack["form_parameter"], attack["button"], attack["cookie"]))

  def get_attacks_list(self):
    return self.attacks_list

  def process_output(self, output_path):
    if os.path.isfile(output_path):
      with open(output_path) as f:
        original = json.load(f)
      updated = []
      for item in original:
        found_page = False
        for updated_item in updated:
          if updated_item["page"] == item["page"]:
            found_page = True
            found_cookie = False
            for cookie in updated_item["cookie"]:
              if cookie["name"] == item["cookie"][0]["name"]:
                found_cookie = True
                cookie["attack"] = cookie["attack"] + list(set(item["cookie"][0]["attack"]) - set(cookie["attack"]))
                break
            if not found_cookie :
              updated_item["cookie"].append(item["cookie"][0])
            break
        if not found_page :
          updated.append(item)
      with open(output_path, "w") as f:
        json.dump(updated, f)


