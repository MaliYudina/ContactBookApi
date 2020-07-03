from rest_framework.generics import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


from .models import Contact, Group
from .serializers import ContactSerializer, GroupSerializer


class ContactView(ListCreateAPIView):
    """
    Displays all objects of model Contact
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        """
        Checks the group relevance
        """
        group = get_object_or_404(Group, id_db_group=self.request.data.get('group_id'))
        return serializer.save(group_id=group)


class SingleContactView(RetrieveUpdateDestroyAPIView):
    """
    Displays an individual model Contact
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class GroupView(ListCreateAPIView):
    """
    Displays all objects of model Group
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class SingleGroupView(RetrieveUpdateDestroyAPIView):
    """
    Displays an individual model Group
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
