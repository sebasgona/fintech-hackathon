from django.db import models

# Create your models here.
class UserModel(models.Model):

    gender_choices = (('M','Male'),('F','Female'))

    user_name = models.CharField(max_length=30)
    user_last_name = models.CharField(max_length=30)
    user_email = models.CharField(max_length=50, unique=True)
    user_tel = models.CharField(max_length=15)
    user_birthday = models.DateField()
    user_rfc = models.CharField(max_length=60)
    user_address = models.CharField(max_length=300)
    user_gender = models.CharField(
        choices=gender_choices,
        default='F',
        max_length=7
    )
    user_ine_id = models.IntegerField()
    user_passport_id = models.IntegerField()
    user_creation_date = models.DateField()
    user_profile_picture = models.ImageField()

class INEModel(models.Model):

    ine_curp = models.CharField(max_length=35)
    ine_local_id = models.CharField(max_length=6)
    ine_municipality = models.CharField(max_length=4)
    ine_section = models.CharField(max_length=6)
    ine_emision = models.CharField(max_length=5)
    ine_validity = models.CharField(max_length=5)
    ine_state = models.IntegerField()
    ine_elector_code = models.CharField(max_length=20)

class PassportModel(models.Model):

    passport_emision_date = models.DateField()
    passport_validity_date = models.DateField()
    passport_number = models.CharField(max_length=40)

class Bucketlist(models.Model):
    """This class represents the bucketlist model."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)