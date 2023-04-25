from django.test import  LiveServerTestCase
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
	def teardown(self):
		self.browser.quit()

	def wait_for_fow_in_list_table(self, row_text):
		start_time = time.time()
		while True:
			try:
				table = self.browser.find_element(By.ID, 'id_list_table')
				rows = table.find_elements(By.TAG_NAME, 'tr')
				self.assertIn(row_text, [row.text for row in rows])
				return
			except (AssertionError, WebDriverException) as e:
				if time.time() - start_time > MAX_WAIT:
					raise  e
					time.sleep(0.5)
	def test_layout_and_styling(self):
		# 伊迪斯访问首页
		self.browser.get(self.live_server_url)
		self.browser.set_window_size(1024, 768)
		# 她看到输入框完美地居中显示
		inputbox = self.browser.find_element(By.ID, 'id_new_item')
		inputbox.send_keys('testing')
		inputbox.send_keys(Keys.ENTER)
		
		self.wait_for_fow_in_list_table('1: testing')
		inputbox = self.browser.find_element(By.ID, 'id_new_item')

		self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width'] / 2, 512, delta=10)

	def test_can_start(self):
		# 待办事项应用，去看这个应用的首页
		# self.browser.get('http://localhost:8000') 不使用硬编码的本地地址，使用LiveServerTestCase提供的live_server_url属性
		self.browser.get(self.live_server_url)
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
		self.wait_for_fow_in_list_table('1: Buy peacock feathers')

		# table = self.browser.find_element(By.ID, 'id_list_table')
		# rows = table.find_elements(By.TAG_NAME, 'tr')
		# self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows), f"New to-do item did not appear in table. Contents were:\n{table.text}")
		# self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
		#页面又显示文本框，输入其他待办事项
		#输入 “Use peacock feathers to make a fly"
		inputbox = self.browser.find_element(By.ID, 'id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
		
		# 页面再次更新，她的清单中显示两个待办事项
		self.wait_for_fow_in_list_table('2: Use peacock feathers to make a fly')
		self.wait_for_fow_in_list_table('1: Buy peacock feathers')
		# 想知道网站会记住她的清单

		# self.fail('Finished the test!')
		# 页面再次更新，清单有两个待办事项

	def test_multiple_users_can_start_lists_at_different_urls(self):
		# 她新建了一个待办事项清单
		self.browser.get(self.live_server_url)
		inputbox = self.browser.find_element(By.ID, 'id_new_item')
		inputbox.send_keys('Buy peacock feathers')
		inputbox.send_keys(Keys.ENTER)
		self.wait_for_fow_in_list_table('1: Buy peacock feathers')
		# 她注意到清单有个唯一的URL
		edith_list_url = self.browser.current_url
		# assertRegex是unittest的辅助函数，用于检查字符串是否匹配正则表达式
		self.assertRegex(edith_list_url, '/lists/.+')
		# 有个弗朗西斯的新用户访问网站
		# 我们使用一个新浏览器会话
		# 确保伊迪斯的信息不回从cookie中泄漏出去
		self.browser.quit()
		self.browser =webdriver.Firefox()
		# 弗朗西斯访问首页
		# 页面中看不到伊迪斯的清单
		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element(By.TAG_NAME, 'body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertNotIn('make a fly', page_text)
		# 弗朗西斯输入一个新待办事项，新建一个清单
		# 他不像伊迪斯那样兴趣盎然
		inputbox = self.browser.find_element(By.ID, 'id_new_item')
		inputbox.send_keys('Buy milk')
		inputbox.send_keys(Keys.ENTER)
		self.wait_for_fow_in_list_table('1: Buy milk')
		# 弗朗西斯获得了他的唯一URL
		francis_list_url = self.browser.current_url
		self.assertRegex(francis_list_url, 'lists/.+')
		self.assertNotEqual(francis_list_url, edith_list_url)
		# 这个页面还是没有伊迪斯的清单
		page_text = self.browser.find_element(By.TAG_NAME, 'body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertIn('Buy milk', page_text)

		# 两个人都很满意





# if __name__ == '__main__':
#	unittest.main()