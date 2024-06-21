from django.test import TestCase
from django.contrib.auth.models import User
from .forms import CustomUserChangeForm, CustomPasswordChangeForm


class TestCustomUserChangeForm(TestCase):
    """
    Test cases for CustomUserChangeForm.
    """

    def setUp(self):
        """
        Set up test data.

        Create a test user.
        """
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpassword"
        )
        self.form_data = {
            "username": "newusername",
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
        }

    def test_form_with_valid_data(self):
        """
        Test form with valid data.
        """
        form = CustomUserChangeForm(data=self.form_data, instance=self.user)
        self.assertTrue(form.is_valid())

    def test_form_with_blank_data(self):
        """
        Test form with blank data.
        """
        form = CustomUserChangeForm(data={}, instance=self.user)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["username"], ["This field is required."])

    def test_form_username_readonly(self):
        """
        Test username field readonly attribute.
        """
        form = CustomUserChangeForm(instance=self.user)
        self.assertTrue(form.fields["username"].widget.attrs.get("readonly"))
