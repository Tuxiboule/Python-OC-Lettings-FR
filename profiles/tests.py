from django.test import TestCase
from django.urls import reverse
from profiles.models import Profile
from django.contrib.auth.models import User


class ProfileIndexDetailViewTest(TestCase):
    """
    This test case checks various aspects of the index view

    Attributes:
        user (User): A test user object.
        profile (Profile): A test profile object associated with the test user.
    """

    def setUp(self):
        """
        Creates a test user and a test profile.
        """
        self.user = User.objects.create(username='testuser')
        self.user.email = 'test@test.test'
        self.user.save()
        self.profile = Profile.objects.create(user=self.user)
        self.profile.save()

    def test_index_view(self):
        """
        Ensures that the index view returns a response with a status code of 200 (OK).
        """
        response = self.client.get(reverse('profiles'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_context(self):
        """
        Checks that the context returned by the index view contains a 'profiles_list' key,
        and the list should contain the expected profiles.
        """
        response = self.client.get(reverse('profiles'))
        self.assertIn('profiles_list', response.context)
        profiles_list = response.context['profiles_list']
        profiles_list = list(profiles_list.values_list('user__username', flat=True))
        self.assertIn(self.user.username, profiles_list)
        self.assertEqual(len(profiles_list), 1)

    def test_index_view_template(self):
        """
        Ensures that the index view uses the correct template ('index.html').
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.templates[0].name, 'index.html')
        self.assertTrue(any(
            'index.html' in template.name for template in response.templates))

    def test_detail_view(self):
        """
        """
        response = self.client.get(reverse('profile', args=[self.user.username]))
        decoded_content = response.content.decode('utf-8')
        self.assertIn(self.user.username, decoded_content)
        self.assertIn(self.user.email, decoded_content)
