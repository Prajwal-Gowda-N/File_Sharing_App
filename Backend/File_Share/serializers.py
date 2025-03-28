from rest_framework import serializers
from .models import UploadedFile

class FileSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = UploadedFile
        fields = ('id', 'file_name', 'file', 'file_url')

    def get_file_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f"/media/download/{obj.file.name.split('/')[-1]}/")  # Download URL
