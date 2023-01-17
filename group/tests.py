from django.test import TestCase
from django.db.utils import DataError, IntegrityError

from .models import Group


class TestGroup(TestCase):
    def setUp(self) -> None:
        self.group = Group.objects.create(pk=1, code='001', name='name001', description='description001')

    def test_attr_pk_equals(self):
        self.assertEqual(self.group.pk, 1)

    def test_attr_code_equals(self):
        self.assertEqual(self.group.code, '001')

    def test_attr_name_equals(self):
        self.assertEqual(self.group.name, 'name001')

    def test_attr_description_equals(self):
        self.assertEqual(self.group.description, 'description001')

    def test_attr_code_must_be_string(self):
        self.assertIsInstance(self.group.code, str)

    def test_attr_name_must_be_string(self):
        self.assertIsInstance(self.group.name, str)

    def test_attr_description_must_be_string(self):
        self.assertIsInstance(self.group.description, str)

    def test_attr_code_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.group.code = None
            self.group.save()

    def test_attr_name_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.group.name = None
            self.group.save()

    def test_attr_description_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.group.description = None
            self.group.save()

    def test_attr_code_must_be_max_size_10(self):
        with self.assertRaises(DataError):
            self.group.code = '1' * 11
            self.group.save()

    def test_attr_name_must_be_max_size_100(self):
        with self.assertRaises(DataError):
            self.group.name = '1' * 101
            self.group.save()

    def test_attr_description_must_be_max_size_255(self):
        with self.assertRaises(DataError):
            self.group.description = '1' * 256
            self.group.save()

    def test_attr_pk_already_exists(self):
        with self.assertRaises(IntegrityError):
            g = Group.objects.create(pk=1, code='test', name='test', description='test')
            g.save()
