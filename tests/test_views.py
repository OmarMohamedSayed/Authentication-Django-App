from .test_setup import TestSetUp
from app.models import *
class TestViews(TestSetUp):
    def test_user_can_register_with_no_data(self):
        res=self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)

    def test_user_can_register(self):
        res=self.client.post(self.register_url, self.user_data, format="json")
        self.assertEqual(res.data['username'], self.user_data['username'])
        self.assertEqual(res.status_code, 201)
    
    def test_user_can_login_with_no_data(self):
        res=self.client.post(self.login_url)
        self.assertEqual(res.status_code, 400)

    def test_user_can_login_with_data(self):
        
        response=self.client.post(self.register_url, self.user_data, format="json")
        username = response.data['username']
        user = User.objects.get(username=username)
        user.save()
        res=self.client.post(self.login_url, self.user_data, format="json")

        self.assertEqual(res.status_code, 200)

    def test_user_can_view_profile_without_token(self):
        res=self.client.post(self.profile_url)
        self.assertEqual(res.status_code, 403)
