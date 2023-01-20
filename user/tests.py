from django.test import TestCase
from django.db.utils import DataError, IntegrityError
from django.contrib.auth.models import User


class UserTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            pk=1,
            username='username',
            password='password',
            first_name='first_name',
            last_name='last_name',
            email='email@email.com'
        )

    def test_user_attr_pk_equals(self):
        self.assertEqual(self.user.pk, 1)

    def test_user_attr_username_equals(self):
        self.assertEqual(self.user.username, 'username')

    def test_user_attr_password_equals(self):
        self.assertEqual(self.user.password, 'password')

    def test_user_attr_first_name_equals(self):
        self.assertEqual(self.user.first_name, 'first_name')

    def test_user_attr_last_name_equals(self):
        self.assertEqual(self.user.last_name, 'last_name')

    def test_user_attr_email_equals(self):
        self.assertEqual(self.user.email, 'email@email.com')

    def test_user_attr_username_must_be_string(self):
        self.assertIsInstance(self.user.username, str)

    def test_user_attr_password_must_be_string(self):
        self.assertIsInstance(self.user.password, str)

    def test_user_attr_first_name_must_be_string(self):
        self.assertIsInstance(self.user.first_name, str)

    def test_user_attr_last_name_must_be_string(self):
        self.assertIsInstance(self.user.last_name, str)

    def test_user_attr_email_must_be_string(self):
        self.assertIsInstance(self.user.email, str)

    def test_user_attr_username_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.user.username = None
            self.user.save()

    def test_user_attr_password_cannot_be_null(self):
        with self.assertRaises(IntegrityError):
            self.user.password = None
            self.user.save()

    def test_user_attr_username_must_be_max_size_150(self):
        with self.assertRaises(DataError):
            self.user.username = '1' * 151
            self.user.save()

    def test_user_attr_password_must_be_max_size_128(self):
        with self.assertRaises(DataError):
            self.user.password = '1' * 129
            self.user.save()

    def test_user_attr_first_name_must_be_max_size_150(self):
        with self.assertRaises(DataError):
            self.user.first_name = '1' * 151
            self.user.save()

    def test_user_attr_last_name_must_be_max_size_150(self):
        with self.assertRaises(DataError):
            self.user.last_name = '1' * 151
            self.user.save()

    def test_user_attr_email_must_be_max_size_254(self):
        with self.assertRaises(DataError):
            self.user.email = '1' * 255
            self.user.save()

    def test_user_attr_pk_already_exists(self):
        with self.assertRaises(IntegrityError):
            u = User.objects.create(
                pk=1,
                username='test',
                password='test',
                first_name='test',
                last_name='test',
                email='test@test.com'
            )
            u.save()
