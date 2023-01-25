from django.test import TestCase
from django.db.utils import DataError, IntegrityError
from datetime import date

from .models import Brand


class BrandTest(TestCase):
    def setUp(self) -> None:
        self.brand = Brand.objects.create(
            pk=1,
            code='001',
            name='name001',
            description='description001',
            foundation_local='foundation_local001',
            foundation_date=date(2001, 1, 1),
            founder='founder001',
            main='main001',
            billing='billing001'
        )

    def test_brand_attr_pk_equals(self):
        self.assertEqual(self.brand.pk, 1)

    def test_brand_attr_code_equals(self):
        self.assertEqual(self.brand.code, '001')

    def test_brand_attr_name_equals(self):
        self.assertEqual(self.brand.name, 'name001')

    def test_brand_attr_description_equals(self):
        self.assertEqual(self.brand.description, 'description001')

    def test_brand_attr_foundation_local_equals(self):
        self.assertEqual(self.brand.foundation_local, 'foundation_local001')

    def test_brand_attr_foundation_date_equals(self):
        self.assertEqual(self.brand.foundation_date, date(2001, 1, 1))

    def test_brand_attr_founder_equals(self):
        self.assertEqual(self.brand.founder, 'founder001')

    def test_brand_attr_main_equals(self):
        self.assertEqual(self.brand.main, 'main001')

    def test_brand_attr_billing_equals(self):
        self.assertEqual(self.brand.billing, 'billing001')

    def test_brand_attr_code_must_be_string(self):
        self.assertIsInstance(self.brand.code, str)

    def test_brand_attr_name_must_be_string(self):
        self.assertIsInstance(self.brand.name, str)

    def test_brand_attr_description_must_be_string(self):
        self.assertIsInstance(self.brand.description, str)

    def test_brand_attr_foundation_local_must_be_string(self):
        self.assertIsInstance(self.brand.foundation_local, str)

    def test_brand_attr_foundation_date_must_be_date(self):
        self.assertIsInstance(self.brand.foundation_date, date)

    def test_brand_attr_founder_must_be_string(self):
        self.assertIsInstance(self.brand.founder, str)

    def test_brand_attr_main_must_be_string(self):
        self.assertIsInstance(self.brand.main, str)

    def test_brand_attr_billing_must_be_string(self):
        self.assertIsInstance(self.brand.billing, str)

    def test_brand_attr_code_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.brand.code = None
            self.brand.save()

    def test_brand_attr_name_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.brand.name = None
            self.brand.save()

    def test_brand_attr_description_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.brand.description = None
            self.brand.save()

    def test_brand_attr_foundation_local_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.brand.foundation_local = None
            self.brand.save()

    def test_brand_attr_foundation_date_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.brand.foundation_date = None
            self.brand.save()

    def test_brand_attr_founder_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.brand.founder = None
            self.brand.save()

    def test_brand_attr_main_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.brand.main = None
            self.brand.save()

    def test_brand_attr_code_must_be_max_size_10(self):
        with self.assertRaises(DataError):
            self.brand.code = '1' * 11
            self.brand.save()

    def test_brand_attr_name_must_be_max_size_100(self):
        with self.assertRaises(DataError):
            self.brand.name = '1' * 101
            self.brand.save()

    def test_brand_attr_foundation_local_must_be_max_size_100(self):
        with self.assertRaises(DataError):
            self.brand.foundation_local = '1' * 101
            self.brand.save()

    def test_brand_attr_founder_must_be_max_size_100(self):
        with self.assertRaises(DataError):
            self.brand.founder = '1' * 101
            self.brand.save()

    def test_brand_attr_main_must_be_max_size_100(self):
        with self.assertRaises(DataError):
            self.brand.main = '1' * 101
            self.brand.save()

    def test_brand_attr_pk_already_exists(self):
        with self.assertRaises(IntegrityError):
            b = Brand.objects.create(
                pk=1,
                code='test',
                name='test',
                description='test',
                foundation_local='test',
                foundation_date=date(2001, 1, 1),
                founder='test',
                main='test',
                billing='test'
            )
            b.save()
