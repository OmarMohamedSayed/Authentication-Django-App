import imp
from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker

    
class TestSetUp(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.profile_url = reverse('profile-list')
        
        self.fake = Faker()
        self.user_data = {
            'username':"01011111111",
            'password':"example"
        }
        self.profile_data = {
            "first_name": self.fake.name(),
            "last_name": self.fake.name(),
            "country_code": "EG",
            "phone_number": "01111111111",
            "birthdate": "2000-01-10",
            "gender": "Male",
            "email": "",
            "avatar": "./media/images/Image_from_iOS_4.jpg"
        }
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()