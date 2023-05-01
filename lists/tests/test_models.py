from django.test import TestCase
from lists.models import Item, List



# Create your tests here.

class ListAndItemModelTest(TestCase):
	"""docstring for lists.models"""
	def test_saving_and_retrieving_items(self):
		list_ = List()
		list_.save()

		frist_item = Item()

		frist_item.text = 'The first (ever) list item'
		frist_item.list = list_
		frist_item.save()
		second_item = Item()
		second_item.text = 'Item the second'
		second_item.list = list_
		second_item.save()
		save_list = List.objects.first()
		self.assertEqual(save_list, list_)
		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(), 2)
		frist_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		self.assertEqual(frist_saved_item.text, 'The first (ever) list item')
		self.assertEqual(frist_saved_item.list, list_)
		self.assertEqual(second_saved_item.text, 'Item the second')
		self.assertEqual(second_saved_item.list, list_)









