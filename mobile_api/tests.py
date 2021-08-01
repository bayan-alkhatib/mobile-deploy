from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import MobileModel

# Create your tests here.
class MobileTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='testuser', password='password')
        test_user.save()

        test_mobile =  MobileModel.objects.create(
            name = 'nova 2i' ,
            desc = 'great phone',
            company = test_user
        )
        test_mobile.save()

    def test_blog_content(self):
        mobile =  MobileModel.objects.get(id=1)
        actual_name = str(mobile.name)
        actual_desc = str(mobile.desc)
        actual_company = str(mobile.company)
        self.assertEqual(actual_name, 'nova 2i')
        self.assertEqual(actual_desc, 'great phone')
        self.assertEqual(actual_company, 'testuser')