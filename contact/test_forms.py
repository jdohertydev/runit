from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):
    """
    Tests for the ContactForm class.
    """

    def test_form_with_valid_data(self):
        """
        Test submitting the form with valid data.
        """
        form_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "message": "This is a test message.",
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_with_blank_data(self):
        """
        Test submitting the form with blank data.
        """
        form = ContactForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["name"], ["This field is required."])
        self.assertEqual(form.errors["email"], ["This field is required."])
        self.assertEqual(form.errors["message"], ["This field is required."])

    def test_form_with_invalid_email(self):
        """
        Test submitting the form with an invalid email address.
        """
        form_data = {
            "name": "John Doe",
            "email": "invalidemail",
            "message": "This is a test message.",
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["email"], ["Enter a valid email address."])
