import json
import os

dir = os.path.dirname(__file__)

with open(os.path.join(dir, 'result.json')) as data_file:    
  data = json.load(data_file)

print(data["movies"][0])