import json
from attack_category_detector import AttackCategoryDetector

attacks = open('App1/phase3output.json')
json_string = attacks.read().decode("utf-8-sig")
data = json.loads(json_string)
detector = AttackCategoryDetector(data)

for index, attack in enumerate(detector.get_attacks_list()):
  if attack.type == "session_fixation" or attack.type == "session_hijacking":
    attack.perform()