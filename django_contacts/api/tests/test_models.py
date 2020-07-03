from django.test import TestCase
# from ..models import Group, Contact
# from django_contacts.api.models import Group, Contact
from ..models import Group, Contact
from django.test import TestCase


class GroupTest(TestCase):

    def setUp(self):
        Group.objects.create(name="Colleagues", category=3)
        Group.objects.create(name="Service", category=6)

    def test_saved_groups(self):
        groups = Group.objects.count()
        self.assertEqual(groups, 2)


# class ContactTest(TestCase):
#
#     def setUp(self):
#         Contact.objects.create(
#                 name="Peter Black",
#                 phone="908652456",
#                 email="email@ya.ru",
#                 comment="guy from business training",
#             )
#         self.contact = Group.objects.get(id=1)
#
#     def test_saved_contacts(self):
#         contacts = Contact.objects.count()
#         self.assertEqual(contacts, 1)
