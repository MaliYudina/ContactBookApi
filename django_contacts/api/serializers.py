from rest_framework import serializers
from .models import Contact, Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name', 'id_db_group', 'category')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('name', 'phone', 'email', 'id_db_contact', 'comment', 'group_id')
