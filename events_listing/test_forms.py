from django.test import TestCase
from .forms import CommentForm
from django.contrib.auth.models import User
from .forms import CustomSignupForm


class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        comment_form = CommentForm({'body': 'This is a great post'})
        self.assertTrue(comment_form.is_valid())

    def test_form_save_method(self):
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
        # Define form data
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword123',
            'password2': 'mismatchedpassword',
            'first_name': 'John',
            'last_name': 'Doe',
        }
        # Create the form instance with the defined form data
        form = CustomSignupForm(data=form_data)
        # Assert that the form is not valid
        self.assertFalse(form.is_valid())
        # Assert that the specific error message for password mismatch is present in the form errors
        self.assertIn("You must type the same password each time.", form.errors['password2'])


