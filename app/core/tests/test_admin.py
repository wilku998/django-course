from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTest(TestCase):
  def setUp(self):
    self.client = Client()
    self.admin_user = get_user_model().objects.create_superuser('super@test.com', '123')
    self.client.force_login(self.admin_user)
    self.user = get_user_model().objects.create_user(
        email='regular@test.com', password='123', name="Emmeme")

  def test_user_listed(self):
    # generate url for get users list page (this functionality comes from django)
    url = reverse('admin:core_user_changelist')
    res = self.client.get(url)

    # assertContain check if response contain certain item
    # and if response status equals 200
    self.assertContains(res, self.user.name)
    self.assertContains(res, self.user.email)

  def test_user_change_page(self):
    url = reverse('admin:core_user_change', args=[self.user.id])
    res = self.client.get(url)

    self.assertEqual(res.status_code, 200)

  def test_user_add_page(self):
    url = reverse('admin:core_user_add')
    res = self.client.get(url)

    self.assertEqual(res.status_code, 200)