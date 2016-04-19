from attack import Attack
from session_fixation_attack import SessionFixationAttack
from session_hijacking_attack import SessionHijackingAttack
from predictable_cookie_attack import PredictableCookieAttack

class AttackCategoryDetector(object):
  def __init__(self, attack_specs):
    """Return a Attack_category_detector object."""
    self.attacks_list = []
    for index, attack in enumerate(attack_specs):
      if attack["cookie"]["attack"][0].strip() == "sessionFixation":
        self.attacks_list.append(SessionFixationAttack(attack["link"], attack["form_parameter"], attack["button"], attack["cookie"]))
      elif attack["cookie"]["attack"][0].strip() == "sessionHijacking":
        self.attacks_list.append(SessionHijackingAttack(attack["link"], attack["form_parameter"], attack["button"], attack["cookie"]))
      elif attack["cookie"]["attack"][0].strip() == "predictableCookie":
        self.attacks_list.append(PredictableCookieAttack(attack["link"], attack["form_parameter"], attack["button"], attack["cookie"], "predictableCookies"))

  def get_attacks_list(self):
    return self.attacks_list
