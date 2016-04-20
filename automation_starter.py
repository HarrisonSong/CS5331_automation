import json
import sys
from attack_category_detector import AttackCategoryDetector

if len(sys.argv) > 1:
  input_path = sys.argv[1]
else:
  input_path = "App1/phase3output1.json"
attacks = open(input_path)
json_string = attacks.read().decode("utf-8-sig")
data = json.loads(json_string)
detector = AttackCategoryDetector(data)

for index, attack in enumerate(detector.get_attacks_list()):
  attack.perform()

detector.process_output()

