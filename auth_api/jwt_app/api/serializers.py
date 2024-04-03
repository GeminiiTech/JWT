from rest_framework.serializers import ModelSerializer
from jwt_app.models import Notes

class NotesSerializer(ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'