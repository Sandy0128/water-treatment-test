# -*- coding:utf-8 -*-

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from base import Page
from time import sleep


class homePage(Page):
	
	url = "/"

	companyList_loc = (By.XPATH, "//*[@id='root']/div/div/div[1]/div[1]/div/ul/li[1]")
	userList_loc = (By.XPATH, "//*[@id='root']/div/div/div[1]/div[1]/div/ul/li[2]")
	inspectors_loc = (By.XPATH, "//*[@id='root']/div/div/div[1]/div[1]/div/ul/li[3]")
	data_loc = (By.XPATH, "//*[@id='root']/div/div/div[1]/div[1]/div/ul/li[4]")


