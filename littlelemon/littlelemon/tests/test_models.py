from django.test import TestCase

from restaurant.models import MenuItem


class MenuModelTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="Vanilla Ice Cream", price=80, inventory=100)
        self.assertEqual(str(item), "Vanilla Ice Cream: 80 x 100")
