import os
import urllib.request
import json
import uuid

dir = os.path.dirname(__file__)
with open(os.path.join(dir, 'result.json')) as data_file:    
  data = json.load(data_file)
  print('開啟了原始檔')

# print(data["movies"][0])
for movieIdx, movieVal in enumerate(data["movies"]):
  print('進入第 '+ str(movieIdx + 1) + ' 個電影')
  for posterIdx, posterVal in enumerate(movieVal["poster"]):
    print('-- 第 '+ str(posterIdx + 1) + ' 張海報')
    filename = uuid.uuid4().hex
    urllib.request.urlretrieve(posterVal, os.path.join(dir, 'poster/' + filename + '.jpg'))

    data["movies"][movieIdx]["poster"][posterIdx] = 'poster/' + filename + '.jpg'


resultFilePath = os.path.join(dir, 'resultUpdatedImageUrl.json')
resultFile = open(resultFilePath, 'w', encoding = 'UTF-8')
resultFile.write(json.dumps(data, ensure_ascii=False))
resultFile.close()
print('檔案儲存完畢')
# for movie in data["movies"]:
#   for poster in movie["poster"]:
#     filename = uuid.uuid4().hex



