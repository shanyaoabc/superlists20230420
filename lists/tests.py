from django.test import TestCase
from lists.models import Item
# from django.urls import resolve
# from lists.views import home_page
# from django.http import HttpRequest
# from django.template.loader import render_to_string


# Create your tests here.

class ItemModelTest(TestCase):
	"""docstring for lists.models"""
	def test_saving_and_retrieving_items(self):
		frist_item = Item()
		frist_item.text = 'The first (ever) list item'
		frist_item.save()
		second_item = Item()
		second_item.text = 'Item the second'
		second_item.save()
		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(), 2)
		frist_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		self.assertEqual(frist_saved_item.text, 'The first (ever) list item')
		self.assertEqual(second_saved_item.text, 'Item the second')

class  HomePageTest(TestCase):
	"""docstring for  SmokeTest"""
	# def test_root_url_resolves(self):
		# found = resolve('/')
		# self.assertEqual(found.func, home_page)
	def test_use_home_template(self):
		# request = HttpRequest() # 创建一个httprequest对象，用户在浏览器中请求网页时，Djiango看到的就是htpprequest对象
		# response = home_page(request) # 把这个对象传给home-page视图，得到响应。响应对象是httpresponse对象
		response = self.client.get('/') # 不在手动创建httprequest对象，不直接调用视图函数
		# html = response.content.decode('utf-8') # 提取相应内容，得到响应原始字节，调用decode,把原始字节转换成字符串
		# self.assertTrue(html.startswith('<html>')) 
		# self.assertIn('<title>To-Do lists</title>', html) # 单元测试由功能测试驱动，而且更接近于真正的代码。编写单元测试时，按照程序员的方式思考。
		# self.assertTrue(html.endswith('</html>'))
		self.assertTemplateUsed(response, 'home.html') # assertTemplateUsed是TestCase类方法，检查相应使用的是哪个模版渲染的
	def test_can_save_a_POST_request(self):
		response = self.client.post('/', data={'item_text': 'A new list item'})
		self.assertIn('A new list item', response.content.decode())
		self.assertTemplateUsed(response, 'home.html')
