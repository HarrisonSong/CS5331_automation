import json
import sys
from attack_category_detector import AttackCategoryDetector

if len(sys.argv) > 2:
  input_path = sys.argv[1]
  output_path = sys.argv[2]
  attacks = open(input_path)
  json_string = attacks.read().decode("utf-8-sig")
  data = json.loads(json_string)
  detector = AttackCategoryDetector(data)

  for index, attack in enumerate(detector.get_attacks_list()):
    attack.perform(output_path)

  detector.process_output(output_path)
else:
  print "not enough arguments"

