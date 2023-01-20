from django.test import TestCase
from django.db.utils import DataError, IntegrityError
from datetime import date
from decimal import Decimal

from .models import Item
from collection.models import Collection
from group.models import Group
from situation.models import Situation


class ItemTest(TestCase):
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

        self.group = Group.objects.create(pk=1, code='001', name='name001', description='description001')
        self.situation = Situation.objects.create(pk=1, code='001', name='name001', description='description001')

        self.item = Item.objects.create(
            pk=1,
            collection=self.collection,
            code='001',
            name='name001',
            brand='brand001',
            model='model001',
            release_year=1111,
            manufacture_year=1111,
            group=self.group,
            situation=self.situation,
            market_value=Decimal(111.1),
            sale_value=Decimal(111.1),
            original=True,
            box=True,
            original_box=True,
            negotiable=True,
            registration_date=date.today(),
            specifications='specifications001',
            damages='damages001',
            comments='comments001'
        )

    def test_item_attr_pk_equals(self):
        self.assertEqual(self.item.pk, 1)

    def test_item_attr_collection_equals(self):
        self.assertEqual(self.item.collection, self.collection)

    def test_item_attr_code_equals(self):
        self.assertEqual(self.item.code, '001')

    def test_item_attr_name_equals(self):
        self.assertEqual(self.item.name, 'name001')

    def test_item_attr_brand_equals(self):
        self.assertEqual(self.item.brand, 'brand001')

    def test_item_attr_model_equals(self):
        self.assertEqual(self.item.model, 'model001')

    def test_item_attr_release_year_equals(self):
        self.assertEqual(self.item.release_year, 1111)

    def test_item_attr_manufacture_year_equals(self):
        self.assertEqual(self.item.manufacture_year, 1111)

    def test_item_attr_group_equals(self):
        self.assertEqual(self.item.group, self.group)

    def test_item_attr_situation_equals(self):
        self.assertEqual(self.item.situation, self.situation)

    def test_item_attr_market_value_equals(self):
        self.assertEqual(self.item.market_value, Decimal(111.1))

    def test_item_attr_sale_value_equals(self):
        self.assertEqual(self.item.sale_value, Decimal(111.1))

    def test_item_attr_original_equals(self):
        self.assertEqual(self.item.original, True)

    def test_item_attr_box_equals(self):
        self.assertEqual(self.item.box, True)

    def test_item_attr_original_box_equals(self):
        self.assertEqual(self.item.original_box, True)

    def test_item_attr_negotiable_equals(self):
        self.assertEqual(self.item.negotiable, True)

    def test_item_attr_registration_date_equals(self):
        self.assertEqual(self.item.registration_date, date.today())

    def test_item_attr_specifications_equals(self):
        self.assertEqual(self.item.specifications, 'specifications001')

    def test_item_attr_damages_equals(self):
        self.assertEqual(self.item.damages, 'damages001')

    def test_item_attr_comments_equals(self):
        self.assertEqual(self.item.comments, 'comments001')

    def test_item_attr_collection_must_be_object(self):
        self.assertIsInstance(self.item.collection, object)

    def test_item_attr_code_must_be_string(self):
        self.assertIsInstance(self.item.code, str)

    def test_item_attr_name_must_be_string(self):
        self.assertIsInstance(self.item.name, str)

    def test_item_attr_brand_must_be_string(self):
        self.assertIsInstance(self.item.brand, str)

    def test_item_attr_model_must_be_string(self):
        self.assertIsInstance(self.item.model, str)

    def test_item_attr_release_year_must_be_int(self):
        self.assertIsInstance(self.item.release_year, int)

    def test_item_attr_manufacture_year_must_be_int(self):
        self.assertIsInstance(self.item.manufacture_year, int)

    def test_item_attr_group_must_be_object(self):
        self.assertIsInstance(self.item.group, object)

    def test_item_attr_situation_must_be_object(self):
        self.assertIsInstance(self.item.situation, object)

    def test_item_attr_market_value_must_be_decimal(self):
        self.assertIsInstance(self.item.market_value, Decimal)

    def test_item_attr_sale_value_must_be_decimal(self):
        self.assertIsInstance(self.item.sale_value, Decimal)

    def test_item_attr_original_must_be_boolean(self):
        self.assertIsInstance(self.item.original, bool)

    def test_item_attr_box_must_be_boolean(self):
        self.assertIsInstance(self.item.box, bool)

    def test_item_attr_original_box_must_be_boolean(self):
        self.assertIsInstance(self.item.original_box, bool)

    def test_item_attr_negotiable_must_be_boolean(self):
        self.assertIsInstance(self.item.negotiable, bool)

    def test_item_attr_registration_date_must_be_date(self):
        self.assertIsInstance(self.item.registration_date, date)

    def test_item_attr_specifications_must_be_string(self):
        self.assertIsInstance(self.item.specifications, str)

    def test_item_attr_damages_must_be_string(self):
        self.assertIsInstance(self.item.damages, str)

    def test_item_attr_comments_must_be_string(self):
        self.assertIsInstance(self.item.comments, str)

    def test_item_attr_collection_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.item.collection = None
            self.item.save()

    def test_item_attr_code_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.item.code = None
            self.item.save()

    def test_item_attr_name_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.item.name = None
            self.item.save()

    def test_item_attr_brand_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.item.brand = None
            self.item.save()

    def test_item_attr_model_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.item.model = None
            self.item.save()

    def test_item_attr_group_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.item.group = None
            self.item.save()

    def test_item_attr_situation_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.item.situation = None
            self.item.save()

    def test_item_attr_market_value_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.item.market_value = None
            self.item.save()

    def test_item_attr_sale_value_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.item.sale_value = None
            self.item.save()

    def test_item_attr_original_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.item.original = None
            self.item.save()

    def test_item_attr_box_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.item.box = None
            self.item.save()

    def test_item_attr_original_box_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.item.original_box = None
            self.item.save()

    def test_item_attr_negotiable_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.item.negotiable = None
            self.item.save()

    def test_item_attr_registration_date_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.item.registration_date = None
            self.item.save()

    def test_item_attr_code_must_be_max_size_10(self):
        with self.assertRaises(DataError):
            self.item.code = '1' * 11
            self.item.save()

    def test_item_attr_name_must_be_max_size_100(self):
        with self.assertRaises(DataError):
            self.item.name = '1' * 101
            self.item.save()

    def test_item_attr_brand_must_be_max_size_100(self):
        with self.assertRaises(DataError):
            self.item.brand = '1' * 101
            self.item.save()

    def test_item_attr_model_must_be_max_size_100(self):
        with self.assertRaises(DataError):
            self.item.model = '1' * 101
            self.item.save()

    def test_item_attr_market_value_must_be_max_size_10_2(self):
        with self.assertRaises(DataError):
            self.item.market_value = 1111111111.111
            self.item.save()

    def test_item_attr_sale_value_must_be_max_size_10_2(self):
        with self.assertRaises(DataError):
            self.item.sale_value = 1111111111.111
            self.item.save()

    def test_item_attr_pk_already_exists(self):
        with self.assertRaises(IntegrityError):
            i = Item.objects.create(
                pk=1,
                collection=self.collection,
                code='test',
                name='test',
                brand='test',
                model='test',
                release_year=1111,
                manufacture_year=1111,
                group=self.group,
                situation=self.situation,
                market_value=Decimal(111.1),
                sale_value=Decimal(111.1),
                original=True,
                box=True,
                original_box=True,
                negotiable=True,
                registration_date=date.today(),
                specifications='test',
                damages='test',
                comments='test'
            )
            i.save()
