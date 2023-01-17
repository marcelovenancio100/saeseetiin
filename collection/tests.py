from django.test import TestCase
from django.db.utils import DataError, IntegrityError

from .models import Collection


class CollectionTest(TestCase):
    def setUp(self) -> None:
        self.collection = Collection.objects.create(
            pk=1,
            code='001',
            name='name001',
            description='description001',
            owner='owner001',
            responsible='responsible001',
            comments="comments001"
        )

    def test_collection_attr_pk_equals(self):
        self.assertEqual(self.collection.pk, 1)

    def test_collection_attr_code_equals(self):
        self.assertEqual(self.collection.code, '001')

    def test_collection_attr_name_equals(self):
        self.assertEqual(self.collection.name, 'name001')

    def test_collection_attr_description_equals(self):
        self.assertEqual(self.collection.description, 'description001')

    def test_collection_attr_owner_equals(self):
        self.assertEqual(self.collection.owner, 'owner001')

    def test_collection_attr_responsible_equals(self):
        self.assertEqual(self.collection.responsible, 'responsible001')

    def test_collection_attr_comments_equals(self):
        self.assertEqual(self.collection.comments, 'comments001')

    def test_collection_attr_code_must_be_string(self):
        self.assertIsInstance(self.collection.code, str)

    def test_collection_attr_name_must_be_string(self):
        self.assertIsInstance(self.collection.name, str)

    def test_collection_attr_description_must_be_string(self):
        self.assertIsInstance(self.collection.description, str)

    def test_collection_attr_owner_must_be_string(self):
        self.assertIsInstance(self.collection.owner, str)

    def test_collection_attr_responsible_must_be_string(self):
        self.assertIsInstance(self.collection.responsible, str)

    def test_collection_attr_comments_must_be_string(self):
        self.assertIsInstance(self.collection.comments, str)

    def test_collection_attr_code_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.collection.code = None
            self.collection.save()

    def test_collection_attr_name_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.collection.name = None
            self.collection.save()

    def test_collection_attr_description_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.collection.description = None
            self.collection.save()

    def test_collection_attr_owner_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.collection.owner = None
            self.collection.save()

    def test_collection_attr_responsible_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.collection.responsible = None
            self.collection.save()

    def test_collection_attr_code_must_be_max_size_30(self):
        with self.assertRaises(DataError):
            self.collection.code = '1' * 31
            self.collection.save()

    def test_collection_attr_name_must_be_max_size_100(self):
        with self.assertRaises(DataError):
            self.collection.name = '1' * 101
            self.collection.save()

    def test_collection_attr_description_must_be_max_size_255(self):
        with self.assertRaises(DataError):
            self.collection.description = '1' * 256
            self.collection.save()

    def test_collection_attr_owner_must_be_max_size_100(self):
        with self.assertRaises(DataError):
            self.collection.owner = '1' * 101
            self.collection.save()

    def test_collection_attr_responsible_must_be_max_size_100(self):
        with self.assertRaises(DataError):
            self.collection.responsible = '1' * 101
            self.collection.save()

    def test_collection_attr_pk_already_exists(self):
        with self.assertRaises(IntegrityError):
            c = Collection.objects.create(
                pk=1,
                code='test',
                name='test',
                description='test',
                owner='test',
                responsible='test',
                comments="test"
            )
            c.save()
