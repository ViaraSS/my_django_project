from django.test import TestCase


class AboutPageTest(TestCase):
    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        print(response.content.decode())  # Печата съдържанието на страницата
        self.assertEqual(response.status_code, 200)
