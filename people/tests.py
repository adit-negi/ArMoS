from django.test import TestCase

from people.models import Person


class AnimalTestCase(TestCase):
    def setUp(self):
        Person.objects.create(title="lion", email="roar@gmail.co",
                              problem_descrition="dsfads", location="Pitampura")
        Person.objects.create(title="cat", email="meow@adit.co",
                              problem_descrition="dsfa", location="Pitampura")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Person.objects.get(title="lion")
        cat = Person.objects.get(title="cat")
        self.assertEqual(lion.title, 'lion')
        self.assertEqual(cat.email, "meow@adit.co")
