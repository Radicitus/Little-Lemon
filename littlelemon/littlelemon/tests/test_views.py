from django.test import TestCase

from restaurant.models import MenuItem


class MenuViewTest(TestCase):
    def setUp(self):
        item1 = MenuItem.objects.create(title="Vanilla Ice Cream", price=80, inventory=100)
        item2 = MenuItem.objects.create(title="Apple Pie", price=10, inventory=10)
        item3 = MenuItem.objects.create(title="Chocolate", price=5, inventory=1000)

    def test_get_all(self):
        item1 = MenuItem.objects.get(title='Vanilla Ice Cream')
        self.assertEqual(str(item1), "Vanilla Ice Cream: 80.00 x 100")
        item2 = MenuItem.objects.get(title='Apple Pie')
        self.assertEqual(str(item2), "Apple Pie: 10.00 x 10")
        item3 = MenuItem.objects.get(title='Chocolate')
        self.assertEqual(str(item3), "Chocolate: 5.00 x 1000")
