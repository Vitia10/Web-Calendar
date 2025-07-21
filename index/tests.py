from django.test import TestCase
from .models import Data
class DataTest(TestCase):
    def test_object_add(self):
        obj = Data.objects.create(name='Kids',money=34)
        #assert
        self.assertEqual(Data.objects.count(),1)
        self.assertEqual(obj.name,'Kids')
        self.assertEqual(obj.money,34)
