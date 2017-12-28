# -*- coding:utf-8 -*-

from models import function
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page(object):

	baseurl = function.get_base_url()

	def __init__(self, driver, base_url=baseurl):
		self.driver = driver
		self.base_url = base_url

	def open_url(self, url):
		url = self.base_url + url
		self.driver.get(url)

	def find_element(self, *loc):
		return self.driver.find_element(*loc)	

	def element_exist(driver, *loc):
		 try:
		 	WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(*loc))
		 except Exception as e:
		 	print ("could not find this element", format(e))
