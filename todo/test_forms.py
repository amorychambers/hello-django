from django.test import TestCase
from .forms import ItemForm

# Create your tests here.


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        form = ItemForm({"name": "",})
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors.keys())


    def test_done_field_is_required(self):
        form = ItemForm({"name": "amory"})
        self.assertTrue(form.is_valid())

    
    def test_fields_are_explicit(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ["name", "done"])