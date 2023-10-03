from django.contrib.auth import get_user_model
from accounts.models import Column


User = get_user_model()


class ColumnTestDataMixin(object):
    @classmethod
    def setUpTestData(self):
        coordinator = User.objects.create(
            username="coordinaror",
            email="coordinatortest@gmail.com",
            password="test123",
        )
        moderator = User.objects.create(
            username="moderator",
            email="moderatortest@gmail.com",
            password="test123",
        )
        writer = User.objects.create(
            username="writer", email="writertest@gmail.com", password="test123"
        )

        column = Column.objects.create(
            name="Test Column", coordinator=coordinator
        )
        column.moderators.add(moderator)
        column.writers.add(writer)
