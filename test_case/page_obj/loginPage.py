# -*- coding:utf-8 -*-

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from base import Page
from time import sleep

class login(Page):

	url = "/login"

	username_loc = (By.ID, "username")
	password_loc = (By.ID, "password")
	submit_loc = (By.XPATH, "//*[@id='root']/div/div/div[2]/form/div[3]/div/div/button")


	def login_username(self, username):
		self.find_element(*self.username_loc).send_keys(username)

	def login_password(self, password):
		self.find_element(*self.password_loc).send_keys(password)

	def login_submit(self):
		self.find_element(*self.submit_loc).click()

	def user_login(self, username, password):
		self.open_url(self.url)
		self.login_username(username)
		self.login_password(password)
		self.login_submit()

	username_empty_loc = (By.CLASS_NAME, "ant-form-explain")
	password_empty_loc = (By.CLASS_NAME, "ant-form-explain")
	password_username_notmatch_loc = (By.CLASS_NAME, "ant-alert-message")

	def user_hint_error(self):
		return self.find_element(*self.username_empty_loc).text
		print self.find_element(*self.username_empty_loc).text

	def pwd_hint_error(self):
		return self.find_element(*self.password_empty_loc).text
		print self.find_element(*self.password_empty_loc).text

	def user_pwd_hint_error(self):
		return self.find_element(*self.password_username_notmatch_loc).text
		print self.find_element(*self.password_username_notmatch_loc).text







