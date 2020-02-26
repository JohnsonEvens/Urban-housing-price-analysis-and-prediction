from django.test import TestCase


class SimpleTest(TestCase):

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_r1(self):
        response = self.client.get('/result1.html/')
        self.assertEqual(response.status_code,200)

    def test_r2(self):
        response = self.client.get('/result2.html/')
        self.assertEqual(response.status_code,200)

    def test_r3(self):
        response = self.client.get('/result3.html/')
        self.assertEqual(response.status_code,200)