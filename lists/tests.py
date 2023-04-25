from django.test import TestCase
from lists.models import Item



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
	def test_use_home_template(self):
		response = self.client.get('/') # 不在手动创建httprequest对象，不直接调用视图函数
		self.assertTemplateUsed(response, 'home.html') # assertTemplateUsed是TestCase类方法，检查相应使用的是哪个模版渲染的

class ListViewTest(TestCase):

	def test_uses_list_template(self):
		response = self.client.get('/lists/the-only-list-in-the-world/')
		self.assertTemplateUsed(response, 'list.html')

	def test_displays_all_list_items(self):
		Item.objects.create(text='itemey 1')
		Item.objects.create(text='itemey 2')
		response = self.client.get('/lists/the-only-list-in-the-world/')
		self.assertContains(response, 'itemey 1')
		self.assertContains(response, 'itemey 2')


class NewListTest(TestCase):

	def test_can_save_a_POST_request(self):
		response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
		# 检查是否把一个新item对象存入数据库
		self.assertEqual(Item.objects.count(), 1)
		news_item = Item.objects.first()
		self.assertEqual(news_item.text, 'A new list item')

	def test_redirects_after_POST(self):
		response = self.client.post('/lists/new', data={'item_text':'A new list item'})
		self.assertRedirects(response, '/lists/the-only-list-in-the-world/')


