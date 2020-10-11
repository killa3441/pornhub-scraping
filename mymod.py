from bs4 import BeautifulSoup
from urllib import request
import gspread
import json

#ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。
from oauth2client.service_account import ServiceAccountCredentials 

#2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('python-pornhub-47b8b4f92c97.json', scope)

#OAuth2の資格情報を使用してGoogle APIにログインします。
gc = gspread.authorize(credentials)

SPREADSHEET_KEY = '16VpdI8ABHYbh7lRjoawaQODarMcVc4B7kohr1_ckags'

#共有設定したスプレッドシートのシート1を開く
worksheet = gc.open_by_key(SPREADSHEET_KEY).worksheet('Python-Pornhub')

url = 'https://jp.pornhub.com/video/search?search=%E5%B7%A8%E4%B9%B3'
response = request.urlopen(url)
soup = BeautifulSoup(response)
response.close()

Pornhub_href = ('https://jp.pornhub.com' + soup.find('div',class_='phimage').a.get('href'))
Pornhub_title = (soup.find('div',class_='thumbnail-info-wrapper').a.get('title'))
Pornhub_image = (soup.find('div',class_='phimage').img.get('data-mediabook'))

print('https://jp.pornhub.com' + soup.find_all('div',class_='phimage').a.get('href')[1])
#worksheet.update_cell(2,1, Pornhub_title)
#worksheet.update_cell(2,2, Pornhub_href)
#worksheet.update_cell(2,3, Pornhub_image)