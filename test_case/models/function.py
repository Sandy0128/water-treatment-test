from selenium import webdriver
import os
import ConfigParser

def insert_img(driver, file_name):
	base_dir = os.path.dirname(os.path.dirname(__file__))
	base_dir = str(base_dir)
	base_dir = base_dir.replace("\\", "/")
	base = base_dir.split("/test_case")[0]
	file_path = base + "/report/image/" + file_name
	driver.get_screenshot_as_file(file_path)


def get_base_url():
	config = ConfigParser.ConfigParser()
	current_path = os.path.dirname(os.path.dirname(__file__))
	current_path = str(current_path)
	current_path = current_path.replace("\\", "/")
	base_path = current_path.split("/test_case")[0]
	file_path = base_path + "/config.ini"
	config.read(file_path)
	BASEURL = config.get("testServer", "BASEURL")
	return BASEURL