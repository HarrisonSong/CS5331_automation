import json
from attack_category_detector import AttackCategoryDetector

attacks = open('phase3output.json')
json_string = attacks.read().decode("utf-8-sig")
data = json.loads(json_string)
detector = AttackCategoryDetector(data)

for index, attack in enumerate(detector.get_attacks_list()):
  attack.perform()



# import json
# import codecs

# # just open the file...
# input_file  = file("input_file.json", "r")
# # need to use codecs for output to avoid error in json.dump
# output_file = codecs.open("output_file.json", "w", encoding="utf-8")

# # read the file and decode possible UTF-8 signature at the beginning
# # which can be the case in some files.
# j = json.loads(input_file.read().decode("utf-8-sig"))

# # then output it, indenting, sorting keys and ensuring representation as it was originally
# json.dump(j, output_file, indent=4, sort_keys=True, ensure_ascii=False)
