from django.test import TestCase
from .models import Item

# Create your tests here.


class TestModels(TestCase):

    def test_done_default_false(self):
        item = Item.objects.create(name="Test Done")
        self.assertFalse(item.done)

    
    def test_item_string_method(self):
        item = Item.objects.create(name="String Name")
        self.assertEqual(str(item), "String Name")