from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By


class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
	def teardown(self):
		self.browser.quit()
	def test_can_start(self):
		# 待办事项应用，去看这个应用的首页
		self.browser.get('http://localhost:8000')
		# 网页标题和头部都包含To-Do
		self.assertIn('To-Do', self.browser.title)
		# header_text = self.browser.find_element_by_tag_name('h1').text
		# 最新的版本的selenium已去除此函数
		header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
		self.assertIn('To-Do', header_text)
		# 应用邀请输入一个待办事项

		# inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox = self.browser.find_element(By.ID, 'id_new_item')

		self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
		# 在文本框输入”Buy Peacock feathers“(购买孔雀羽毛)

		inputbox.send_keys('Buy peacock feathers')
		# 回车更新页面
		# 待办事项显示了” 1：Buy peacock feathers"
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)
		table = self.browser.find_element(By.ID, 'id_list_table')
		rows = table.find_elements(By.NAME, 'tr')
		self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows), "New to-do item did not appear in table")
		#页面又显示文本框，输入其他待办事项
		#输入 “Use peacock feathers to make a fly"
		self.fail('Finished the test!')
		# 页面再次更新，清单有两个待办事项

if __name__ == '__main__':
	unittest.main()