from selenium.webdriver import Remote
from selenium import webdriver

def browser():
	host = "127.0.0.1:5555"
	dc = {"browserName": "chrome"}
	driver = Remote(command_executor = "http://" + host + "/wd/hub", desired_capabilities = dc)
	return driver


if __name__ == "__main__":
	dr = browser()
	dr.get("http://baidu.com")
	dr.quit()