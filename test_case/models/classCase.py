from selenium import webdriver
import unittest

class Mytest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Chrome()

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()
