from django.urls import reverse
from django.test import TestCase

class RegexAppTests(TestCase):
    
    def test_reverse_string_logic_missing_string(self):
        response = self.client.post(reverse('reverse_string_logic'), {})
        self.assertEqual(response.status_code, 400)
    
    def test_regex_generator_missing_string(self):
        response = self.client.post(reverse('regex_generator'), {})
        self.assertEqual(response.status_code, 400)
    
    def test_regex_generator_valid(self):
        response = self.client.post(reverse('regex_generator'), {'string': 'abc'})
        self.assertEqual(response.status_code, 200)
    
    def test_regex_normal_invalid_pattern(self):
        response = self.client.post(reverse('regex_normal'), {'pattern': '[a-z', 'string': 'hello'})
        self.assertEqual(response.status_code, 400)
    
    def test_regex_normal_match(self):
        response = self.client.post(reverse('regex_normal'), {'pattern': '^hello$', 'string': 'hello'})
        self.assertEqual(response.status_code, 200)
    
    def test_regex_normal_no_match(self):
        response = self.client.post(reverse('regex_normal'), {'pattern': '^hello$', 'string': 'world'})
        self.assertEqual(response.status_code, 200)
    
    def test_regex_testing_invalid_pattern(self):
        response = self.client.post(reverse('regex_testing'), {'pattern': '[a-z'})
        self.assertEqual(response.status_code, 400)
    
    def test_regex_testing_valid_pattern(self):
        response = self.client.post(reverse('regex_testing'), {'pattern': '^hello$'})
        self.assertEqual(response.status_code, 200)

