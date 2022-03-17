from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from rest_framework.validators import UniqueValidator

from commons.serializers import GenderSerializer
from postulant.models import Curriculum, Postulant
from users.models import User

class CurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculum
        fields = (
            'pk',
            'name',
            'name_original',
            'format',
            'url'
        )

class SignUpPostulantSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(
        required=True,
        max_length=254,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        required=True,
        validators=[validate_password],
        write_only=True,
        max_length=128, )
    name = serializers.CharField(required=True, max_length=254)
    last_name = serializers.CharField(required=True, max_length=254)

    def to_representation(self, instance):
        # HACK: Overwrite User fields into the client instance to represent
        instance.email = instance.user.email
        instance.name = instance.user.first_name
        instance.last_name = instance.user.last_name
        return super(SignUpPostulantSerializer, self).to_representation(instance)

    class Meta:
        model = Postulant
        fields = ('id', 'email', 'password', 'name', 'last_name',)


class PostulantSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='user.email')
    name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    curriculum = CurriculumSerializer(read_only=True)
    curriculum_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Postulant
        fields = ('pk','gender', 'document_type', 'document', 'created_at', 'email',
                  'date_of_birth', 'phone', 'is_active', 'avatar', 'name', 'last_name','curriculum','curriculum_id')
