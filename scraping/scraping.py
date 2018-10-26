import os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import json

# =================================================================================
# Global Variable
# =================================================================================

browser = webdriver.Chrome()
browser.set_page_load_timeout(30)

possibleValue = {
  '中文片名': 'title',
  '英文片名': 'titleEn',
  '影片時間': 'length',
  '影片類型': 'genre',
  '分級級數': 'ratingSystems',
  '出品年份': 'year',
  '出品公司': 'productionCompany',
  '出品國家': 'productionCountry',
  '發行公司': 'distributionCorporation',
  '故事大綱（本事）': 'description',
  '導演': 'director',
  '編劇': 'screenwriter',
  '製片人': 'producer',
  '演員': 'cast',
  '劇照': 'poster',
  '預告片': 'ytTrailer'
}

resultObj = {
  "movies": []
}

failedUrlObj = {
  "failedUrl": []
}

# =================================================================================
# function
# =================================================================================

def save():
  dir = os.path.dirname(__file__)
  resultFilePath = os.path.join(dir, 'result.json')
  failedUrlFilePath = os.path.join(dir, 'failedUrl.json')

  resultFile = open(resultFilePath, 'w', encoding = 'UTF-8')
  resultFile.write(json.dumps(resultObj, ensure_ascii=False))
  resultFile.close()

  failedUrlFilePath = open(failedUrlFilePath, 'w', encoding = 'UTF-8')
  failedUrlFilePath.write(json.dumps(failedUrlObj, ensure_ascii=False))
  failedUrlFilePath.close()

def scrapeMovieData( url ):

  movieObj = {}

  def fn():
    key = browser.find_elements_by_css_selector(".Metadata tr th")
    key_text = [k.text.strip() for k in key]

    value = browser.find_elements_by_css_selector(".Metadata tr td")
    value_text = [v.text.strip() for v in value]

    posters = browser.find_elements_by_css_selector(".Still ul li a img")
    posters_link = [i.get_attribute("src") for i in posters]

    ytTrailer = ''

    try:
      ytTrailer = browser.find_element_by_css_selector(".Metadata iframe").get_attribute("src")
    except:
      try:
        ytTrailer = browser.find_element_by_css_selector("#url3").get_attribute("value")
      except:
        ytTrailer = ''

    # idx start at 0
    # 塞數值

    for keyIdx, keyVal in enumerate(key_text):
      for jsonIdx, jsonVal in enumerate(possibleValue):
        if keyVal == jsonVal:
          movieObj[possibleValue[jsonVal]] = value_text[keyIdx]
          break

    movieObj[possibleValue['劇照']] = posters_link
    movieObj[possibleValue['預告片']] = ytTrailer

    # 名稱什麼的變成 Array

    if possibleValue['影片類型'] in movieObj:
      movieObj[possibleValue['影片類型']] = movieObj[possibleValue['影片類型']].split('，')

    if possibleValue['出品公司'] in movieObj:
      movieObj[possibleValue['出品公司']] = movieObj[possibleValue['出品公司']].split('，')

    if possibleValue['出品國家'] in movieObj:
      movieObj[possibleValue['出品國家']] = movieObj[possibleValue['出品國家']].split('，')

    if possibleValue['發行公司'] in movieObj:
      movieObj[possibleValue['發行公司']] = movieObj[possibleValue['發行公司']].split('，')

    if possibleValue['導演'] in movieObj:
      movieObj[possibleValue['導演']] = movieObj[possibleValue['導演']].split('， ')

    if possibleValue['編劇'] in movieObj:
      movieObj[possibleValue['編劇']] = movieObj[possibleValue['編劇']].split('， ')

    if possibleValue['製片人'] in movieObj:
      movieObj[possibleValue['製片人']] = movieObj[possibleValue['製片人']].split('， ')

    if possibleValue['演員'] in movieObj:
      movieObj[possibleValue['演員']] = movieObj[possibleValue['演員']].split('， ')

    # debug

    if 'title' in movieObj:
      print('-- 增加了: ' + movieObj['title'])


  try:
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[2])

    browser.get( url )
    fn()

  except TimeoutException as ex:
    failedUrlObj["failedUrl"].append( url )
    print( '-- 本頁 timeout' )
    print( failedUrlObj )

    print( '-- 關閉分頁' )
    # browser.execute_script("window.stop();")
    # fn()
    # browser.quit()
    # browser = webdriver.Chrome()

  browser.close()
  browser.switch_to.window(browser.window_handles[1])

  return movieObj




def runPage( url ):
  def fn():
    browser.get( url )
    links = browser.find_elements_by_css_selector(".ListTable tr td.ALeft a") # 現在頁面標題
    links_url = [l.get_attribute("href") for l in links]

    for link_url in links_url:
      movieObj = scrapeMovieData( link_url )
      if 'title' in movieObj:
        resultObj["movies"].append( movieObj )

  try:
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[1])

    fn()

    browser.close()
    browser.switch_to.window(browser.window_handles[0])

  except TimeoutException as ex:
    browser.close()
    browser.switch_to.window(browser.window_handles[0])

    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[1])
    fn()

# =================================================================================
# main
# =================================================================================


# browser.refresh()

# browser.get('http://www.taiwancinema.com/ct_12000_249') # 電影查詢瀏覽 ─ 電影檔案 by 年份
# browser.quit()
# browser = webdriver.Chrome()
# browser.get('http://www.google.com')
# movieObj = scrapeMovieData( 'http://www.taiwancinema.com/ct_67142_38' )
# resultObj["movies"].append( movieObj )
# browser.get('http://www.taiwancinema.com/ct_12000_249') # 電影查詢瀏覽 ─ 電影檔案 by 年份

# save()

# browser.get('http://stackoverflow.com/')

# browser.get('http://www.google.com/')

# exit()





browser.get('http://www.taiwancinema.com/ct_12000_249') # 電影查詢瀏覽 ─ 電影檔案 by 年份

years = browser.find_elements_by_css_selector(".BrowseItem ul:nth-child(2) li a") # 所有年份
years_text = [l.text for l in years]

# 進入各個年份資料庫
for year_text in years_text:

  print('現在是 ' + year_text + ' 年')
  # 先去第一頁才能得到 total 頁數
  browser.get('http://www.taiwancinema.com/lp_38_htx_ProductYearS_' + year_text + '_htx_ProductYearE_' + year_text + '_nowPage_1_pagesize_20')
  totalPage = browser.find_element_by_css_selector(".Page .Number:nth-child(1)").text
  print('總共 ' + totalPage + ' 頁')

  print('現在在跑第 1 頁')
  runPage( 'http://www.taiwancinema.com/lp_38_htx_ProductYearS_' + year_text + '_htx_ProductYearE_' + year_text + '_nowPage_1_pagesize_20' )

  # 跑除了第一頁以外的其他頁
  for page in range(int(totalPage) - 1):
    print('現在在跑第 ' + str(page + 2) + ' 頁')
    runPage( 'http://www.taiwancinema.com/lp_38_htx_ProductYearS_' + year_text + '_htx_ProductYearE_' + year_text + '_nowPage_' + str(page + 2) + '_pagesize_20' )


save()

# print(titles)
# browser.execute_script("console.log('test')")

# for i in range(3):
#   titles = browser.find_elements_by_css_selector(".Metadata tr th")
#   titles_text = [t.text for t in titles]
#   print(titles_text) 


# browser.execute_script("window.history.go(-1)") # 上一頁