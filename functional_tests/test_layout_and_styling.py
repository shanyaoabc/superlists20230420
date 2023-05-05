from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from .base import FunctionalTest

MAX_WAIT = 10


class LayouuAndStaylingTest(FunctionalTest):

	def test_layout_and_styling(self):
		# 伊迪斯访问首页
		self.browser.get(self.live_server_url)
		self.browser.set_window_size(1024, 768)
		# 她看到输入框完美地居中显示
		inputbox = self.get_item_input_box()
		inputbox.send_keys('testing')
		inputbox.send_keys(Keys.ENTER)
		
		self.wait_for_fow_in_list_table('1: testing')
		inputbox = self.get_item_input_box()

		self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width'] / 2, 512, delta=10)
