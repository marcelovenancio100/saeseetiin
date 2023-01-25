from django.test import TestCase
from django.db.utils import DataError, IntegrityError

from .models import Model


class ModelTest(TestCase):
    def setUp(self) -> None:
        self.model = Model.objects.create(
            pk=1,
            code='001',
            name='name001',
            description='description001',
            specifications='specifications001'
        )

    def test_model_attr_pk_equals(self):
        self.assertEqual(self.model.pk, 1)

    def test_model_attr_code_equals(self):
        self.assertEqual(self.model.code, '001')

    def test_model_attr_name_equals(self):
        self.assertEqual(self.model.name, 'name001')

    def test_model_attr_description_equals(self):
        self.assertEqual(self.model.description, 'description001')

    def test_model_attr_specifications_equals(self):
        self.assertEqual(self.model.specifications, 'specifications001')

    def test_model_attr_code_must_be_string(self):
        self.assertIsInstance(self.model.code, str)

    def test_model_attr_name_must_be_string(self):
        self.assertIsInstance(self.model.name, str)

    def test_model_attr_description_must_be_string(self):
        self.assertIsInstance(self.model.description, str)

    def test_model_attr_specifications_must_be_string(self):
        self.assertIsInstance(self.model.specifications, str)

    def test_model_attr_code_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.model.code = None
            self.model.save()

    def test_model_attr_name_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.model.name = None
            self.model.save()

    def test_model_attr_description_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.model.description = None
            self.model.save()

    def test_model_attr_code_must_be_max_size_10(self):
        with self.assertRaises(DataError):
            self.model.code = '1' * 11
            self.model.save()

    def test_model_attr_name_must_be_max_size_100(self):
        with self.assertRaises(DataError):
            self.model.name = '1' * 101
            self.model.save()

    def test_model_attr_pk_already_exists(self):
        with self.assertRaises(IntegrityError):
            m = Model.objects.create(
                pk=1,
                code='test',
                name='test',
                description='test',
                specifications='test'
            )
            m.save()
