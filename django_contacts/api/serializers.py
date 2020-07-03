from rest_framework import serializers
from .models import Contact, Group


class GroupSerializer(serializers.ModelSerializer):
    """
    Serialize all the groups.
    """
    class Meta:
        model = Group
        fields = ('name', 'id_db_group', 'category')


class ContactSerializer(serializers.ModelSerializer):
    """
    Serialize all the contacts.
    """
    class Meta:
        model = Contact
        fields = ('name', 'phone', 'email', 'id_db_contact', 'comment', 'group_id')
