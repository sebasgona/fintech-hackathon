from rest_framework import serializers
from .models import Bucketlist,UserModel,INEModel,PassportModel

class BucketlistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Bucketlist
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = UserModel
        fields = ('user_name', 'user_last_name', 'user_email', 'user_tel','user_birthday','user_rfc',
                  'user_address','user_gender','user_ine_id','user_passport_id','user_creation_date',
                  'user_profile_picture')

class INEModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = INEModel
        fields = ('ine_curp','ine_local_id','ine_municipality','ine_section','ine_emision','ine_validity',
                  'ine_state','ine_elector_code')

class PassportModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassportModel
        fields = ('passport_emision_date','passport_validity_date','passport_number')