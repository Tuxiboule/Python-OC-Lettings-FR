from django.test import TestCase
from django.urls import reverse
from lettings.models import Letting, Address


class LettingIndexDetailViewTest(TestCase):

    def setUp(self):
        """
        Create a test letting
        """
        self.adress = Address.objects.create(number=10,
                                             street='testing_street',
                                             city='test_city',
                                             state='state of test',
                                             zip_code='1000',
                                             country_iso_code='123')
        self.adress.save()
        self.letting = Letting.objects.create(address=self.adress,
                                              title='test letting',
                                              id=1)
        self.letting.save()

    def test_index_view(self):

        """
        Ensures that the index view returns a response with a status code of 200 (OK).
        """
        response = self.client.get(reverse('lettings'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_context(self):
        """
        Checks that the context returned by the index view contains a 'profiles_list' key,
        and the list should contain the expected profiles.
        """
        response = self.client.get(reverse('lettings'))
        self.assertIn('lettings_list', response.context)
        lettings_list = response.context['lettings_list']
        print(lettings_list)
        self.assertIn(self.letting, lettings_list)
        self.assertEqual(len(lettings_list), 1)

    def test_index_view_template(self):
        """
        Ensures that the index view uses the correct template ('index.html').
        """
        response = self.client.get(reverse('index'))
        self.assertTrue(any(
            'index.html' in template.name for template in response.templates))

    def test_detail_view(self):
        """
        """
        response = self.client.get(reverse('letting', args=[self.letting.id]))
        decoded_content = response.content.decode('utf-8')
        self.assertIn(self.letting.title, decoded_content)
        self.assertIn(self.letting.address.city, decoded_content)
