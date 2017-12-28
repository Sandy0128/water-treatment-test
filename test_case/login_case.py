# -*- coding:utf-8 -*-

from time import sleep
import unittest
from models import classCase, function
from page_obj.loginPage import login
from page_obj.homePage import homePage

class loginTest(classCase.Mytest):
	"""
	User login case
	"""
	
	def verify_login(self, username = "", password = ""):
		login(self.driver).user_login(username, password)


	"""
	def test_username_password_empty(self):
		self.verify_login(username = "", password = "")
		sleep(1)
		loginpage = login(self.driver)
		#loginpage.user_hint_error()
		self.assertEqual(loginpage.user_hint_error(), u"请输入您的用户名!")
		self.assertEqual(loginpage.pwd_hint_error(), u"请输入您的密码!")
		function.insert_img(self.driver, "user_pwd_empty.png")

	def test_login_successfully(self):
		
		User login successfully
		
		homepage = homePage(self.driver)
		self.verify_login(username="sandy", password="Welcome2")
		homepage.element_exist(homepage.companyList_loc)
		function.insert_img(self.driver, "user_login_successfully.png")

	
	"""
	def test_username_empty(self):
		self.verify_login(username = "", password = "Welcome2")
		sleep(2)
		loginpage = login(self.driver)
		self.assertEqual(loginpage.user_hint_error(), u"请输入您的用户名!")
		function.insert_img(self.driver, "user_empty.png")

	def test_wrong_password(self):
		self.verify_login(username = "sandy", password = "124")
		loginpage = login(self.driver)
		self.assertEqual(loginpage.user_pwd_hint_error, u"账户或密码错误")
		function.insert_img(self.driver, "pasword_incorrect.png")

	def test_wrong_username(self):
		self.verify_login(username= "sandytest", password = "Welcome2")
		loginpage =  login(self.driver)
		self.assertEqual(loginpage.user_pwd_hint_error, u"账户或密码错误")
		function.insert_img(self.driver, "username_incorrect.png")

	def test_wrong_username_password(self):
		self.verify_login(username = "test1111", password = "test122")
		loginpage = login(self.driver)
		self.assertEqual(loginpage.user_pwd_hint_error, u"账户或密码错误")
		function.insert_img(self.driver, "username_password_incorrect.png")


if __name__ == "__main__":
	unittest.main()