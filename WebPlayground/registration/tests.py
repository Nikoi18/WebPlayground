from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User



class ProfileTestClass(TestCase):
    def setUp(self):
        User.objects.create_user('test', 'email@email.com', 'test1234')

    def test_profile_exists(self):
        exist = Profile.objects.filter(user__username='test').exists()
        self.assertEqual(exist, True)


