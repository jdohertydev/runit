from django.test import TestCase
from .forms import CommentForm, CustomSignupForm
from django.contrib.auth.models import User

class TestCommentForm(TestCase):
    """
    Test cases for the CommentForm.
    """

    def test_form_is_valid(self):
        """
        Test if the CommentForm is valid with valid data.
        """
        comment_form = CommentForm({'body': 'This is a great post'})
        self.assertTrue(comment_form.is_valid())

    def test_form_save_method(self):
        """
        Test the save method of CustomSignupForm.
        """
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            'first_name': 'John',
            'last_name': 'Doe',
        }
        form = CustomSignupForm(data=form_data)
        self.assertTrue(form.is_valid())

        # Modify the request mock to have a user attribute
        class MockRequest:
            def __init__(self):
                self.user = None
                self.session = {}  # Add a session attribute to avoid AttributeError

        request = MockRequest()
        user = form.save(request)
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')

    def test_form_with_password_mismatch(self):
        """
        Test if CustomSignupForm fails validation with password mismatch.
        """
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword123',
            'password2': 'mismatchedpassword',
            'first_name': 'John',
            'last_name': 'Doe',
        }
        form = CustomSignupForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("You must type the same password each time.", form.errors['password2'])
