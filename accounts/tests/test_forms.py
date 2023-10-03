from django.test import TestCase
from accounts.tests.common.mixins import ColumnTestDataMixin
from accounts.forms import PostForm
from django.contrib.auth import get_user_model


User = get_user_model()


class PostFormTest(ColumnTestDataMixin, TestCase):
    def setUp(self):
        self.coordinator = User.objects.get(email="coordinatortest@gmail.com")
        self.moderator = User.objects.get(email="moderatortest@gmail.com")
        self.writer = User.objects.get(email="writertest@gmail.com")

    def test_post_form(self):
        invalid_data = {
            "title": "This is a test post",
            "column": 1
        }
        form = PostForm(invalid_data, user_id=self.coordinator.id)
        form.is_valid()
        self.assertTrue(form.errors)
