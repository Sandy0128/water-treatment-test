from HTMLTestRunner import HTMLTestRunner
import unittest
import time
import os


test_dir = "./test_case/"
discover = unittest.defaultTestLoader.discover(test_dir, pattern = "*_case.py")


if __name__ == "__main__":

	
	now = time.strftime("%Y-%m-%d-%H_%M_%S")
	filename = "./report/" + now + "_result.html"
	fp = open(filename, "wb")
	runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="water login", description="login successfully")
	test_dir = "./test_case/"
	discover = unittest.defaultTestLoader.discover(test_dir, pattern = "*_case.py")
	runner.run(discover)
	fp.close()

	"""
	runner = unittest.TextTestRunner()
	runner.run(discover)
	"""
	