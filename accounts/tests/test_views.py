from django.contrib.auth import get_user_model
from django.test import TestCase
from django.shortcuts import reverse
from accounts.tests.common.mixins import ColumnTestDataMixin

User = get_user_model()


class ColumnListViewTest(ColumnTestDataMixin, TestCase):
    def test_get_column_list(self):
        response = self.client.get(reverse("columns:column-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Column")


# class DemoCase(TestCase):
#     """
#     setUp method
#     setUpClass
#     """

#     def setUp(self):
#         """Once per test"""
#         pass

#     def setUpClass(cls):
#         """Once per TestCase class"""
#         pass

#     def setUpTestData(cls):
#         """Once per TestCase class"""
#         pass

#     def tearDown(self):
#         """Once per test"""
#         pass

#     def tearDownClass(cls):
#         """Once per TestCase class"""
#         pass
