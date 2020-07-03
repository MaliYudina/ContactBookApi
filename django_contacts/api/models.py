from django.db import models


class Group(models.Model):
    """
    Group class defines the attributes of a Group
    """
    name = models.CharField(verbose_name="Group name", max_length=60, unique=True)
    CATEGORY_CHOICES = ((1, "Family"),
                        (2, "Private"),
                        (3, "Business"),
                        (4, "Friends"),
                        (5, "Favourite"),
                        (6, "Service"),
                        (7, "Spam"),
                        )
    category = models.IntegerField(verbose_name="Category", choices=CATEGORY_CHOICES, default=1)
    id_db_group = models.AutoField(verbose_name="Uid", primary_key=True, db_index=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    """
    Contact class defines the attributes of a Contact
    """
    name = models.CharField(verbose_name="Name, Surname", max_length=255, unique=True)
    phone = models.IntegerField(verbose_name="Phone", unique=True)
    email = models.EmailField(verbose_name="Email")
    comment = models.TextField(verbose_name="Comment", max_length=255)
    group_id = models.ForeignKey('Group', related_name='contacts',
                                 on_delete=models.CASCADE,
                                 verbose_name="Related group"
                                 )
    id_db_contact = models.AutoField(primary_key=True, db_index=True, verbose_name="Uid")

    def __str__(self):
        return self.name
