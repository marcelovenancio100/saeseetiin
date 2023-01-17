from django.test import TestCase
from django.db.utils import DataError, IntegrityError

from .models import Situation


class SituationTest(TestCase):
    def setUp(self) -> None:
        self.situation = Situation.objects.create(pk=1, code='001', name='name001', description='description001')

    def test_situation_attr_pk_equals(self):
        self.assertEqual(self.situation.pk, 1)

    def test_situation_attr_code_equals(self):
        self.assertEqual(self.situation.code, '001')

    def test_situation_attr_name_equals(self):
        self.assertEqual(self.situation.name, 'name001')

    def test_situation_attr_description_equals(self):
        self.assertEqual(self.situation.description, 'description001')

    def test_situation_attr_code_must_be_string(self):
        self.assertIsInstance(self.situation.code, str)

    def test_situation_attr_name_must_be_string(self):
        self.assertIsInstance(self.situation.name, str)

    def test_situation_attr_description_must_be_string(self):
        self.assertIsInstance(self.situation.description, str)

    def test_situation_attr_code_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.situation.code = None
            self.situation.save()

    def test_situation_attr_name_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.situation.name = None
            self.situation.save()

    def test_situation_attr_description_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.situation.description = None
            self.situation.save()

    def test_situation_attr_code_must_be_max_size_10(self):
        with self.assertRaises(DataError):
            self.situation.code = '1' * 11
            self.situation.save()

    def test_situation_attr_name_must_be_max_size_100(self):
        with self.assertRaises(DataError):
            self.situation.name = '1' * 101
            self.situation.save()

    def test_situation_attr_description_must_be_max_size_255(self):
        with self.assertRaises(DataError):
            self.situation.description = '1' * 256
            self.situation.save()

    def test_situation_attr_pk_already_exists(self):
        with self.assertRaises(IntegrityError):
            s = Situation.objects.create(pk=1, code='test', name='test', description='test')
            s.save()
