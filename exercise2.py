#!/usr/bin/python
#-*- coding: utf-8 -*-
#encoding=utf-8

import urllib2
import urllib
import os

def getAllImageLink():

	url = 'http://www.dbmeizi.com'
	respone = urllib2.urlopen(url).read()
	print respone + 'jjaj'



