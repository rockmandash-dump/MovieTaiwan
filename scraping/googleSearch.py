import os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import json
import urllib.request
import uuid

dir = os.path.dirname(__file__)
with open(os.path.join(dir, 'resultUpdatedImageUrl.json')) as data_file:    
  data = json.load(data_file)
  print('開啟了原始檔')

print(len(data["movies"]))

count = 0

for movieIdx, movieVal in enumerate(data["movies"]):
  if len(movieVal["poster"]) == 0:
    count += 1

print(count)
# browser = webdriver.Chrome()
# browser.set_page_load_timeout(30)
# print('開啟了瀏覽器')


# for movieIdx, movieVal in enumerate(data["movies"]):
#   print('進入第 '+ str(movieIdx + 1) + ' 個電影')
#   if len(movieVal["poster"]) == 0:
#     print('-- ' + movieVal["title"] + ' 沒有 Poster')
#     searchTerm = movieVal["title"] + ' 台灣電影'
#     url = 'https://www.google.com.tw/search?q=' + searchTerm + '&tbm=isch'

#     try:
#       browser.execute_script("window.open('');")
#       browser.switch_to.window(browser.window_handles[1])

#       browser.get( url )
#       print('-- Google 搜尋圖片')
#       bigImagePageLink = browser.find_element_by_css_selector("#rg_s > div:first-child > a").get_attribute("href")
#       print('-- 大圖片網址')
#       browser.get( bigImagePageLink )

#       imgs = browser.find_elements_by_css_selector("img")
#       imgLinks = [i.get_attribute("src") for i in imgs]

#       for imgIdx, imgVal in enumerate(imgLinks):
#         if imgLinks[imgIdx] is not None:
#           if "img.mvmv.com.tw" in imgLinks[imgIdx]: 
#             filename = uuid.uuid4().hex
#             urllib.request.urlretrieve(imgLinks[imgIdx], os.path.join(dir, 'poster/' + filename + '.jpg'))
#             data["movies"][movieIdx]["poster"].append('poster/' + filename + '.jpg')

#       browser.close()
#       browser.switch_to.window(browser.window_handles[0])
#       print('-- 圖片儲存完畢')
#     except:
#       browser.close()
#       browser.switch_to.window(browser.window_handles[0])
#       print('-- 無法儲存圖片')
          

# resultFilePath = os.path.join(dir, 'resultUpdatedImageUrlAddGoogleImage.json')
# resultFile = open(resultFilePath, 'w', encoding = 'UTF-8')
# resultFile.write(json.dumps(data, ensure_ascii=False))
# resultFile.close()
# print('檔案儲存完畢')