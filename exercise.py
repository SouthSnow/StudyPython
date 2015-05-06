
#!/usr/bin/python
#-*- coding: utf-8 -*-
#encoding=utf-8

import urllib
import urllib2
import os
import re

def url_open(url):
	req = urllib2.Request(url)
	#req.add_header('User-Agent','Mozilla/5.0 (X11;Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0')
	response = urllib2.urlopen(req)
	return response.read()

def get_page(url):
	html = url_open(url)
	pattern = r'<span class="current-comment-page">\[(\d{4})\]</span>'
	page = int(re.findall(pattern,html)[0])
	return page

def find_imgs(page_url):
	pattern = r'<img src="(.*?\.jpg)"'
	html = url_open(page_url)
	img_addrs = re.findall(pattern,html)
	return img_addrs

def save_imgs(img_addrs,page_num,folder):
	os.mkdir(str(page_num))
	os.chdir(str(page_num))
	for i in img_addrs:
		pattern = r'sinaimg.cn/mw600/(.*?).jpg'
		filename = i.split('/')[-1]
		image = url_open(i)
		with open(filename,'wb') as f:
			f.write(image)
			f.close()

def download_mm(folder='ooxx',pages = 10):
	os.mkdir(folder)
	os.chdir(folder)
	folder_top = os.getcwd()
	url = 'http://jandan.net/ooxx/'
	page_num = get_page(url)
	for i in range(pages):
		page_num -= i
		page_url = url + 'page-' + str(page_num) + '#comments'
		img_addrs = find_imgs(page_url)
		save_imgs(img_addrs,page_num,folder)
		os.chdir(folder_top)

if __name__ == '__main__':
	folder = input("please enter a folder(default is 'ooxx'):")
	pages = input("How many pages do you wan to dowm(default is 10):")
	download_mm(str(folder),int(pages))


