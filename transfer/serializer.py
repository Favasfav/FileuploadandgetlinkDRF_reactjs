from rest_framework import serializers
from .models import Folder, Files
import shutil

class FilelistSerializer(serializers.Serializer):
    files = serializers.ListField(child=serializers.FileField(max_length=10000, allow_empty_file=False, use_url=False))
    folder = serializers.CharField(max_length = 150,required=False)
    def zip_folder(self,folder):
        shutil.make_archive(f'public/static/zip/{folder}','zip',f'public/static/{folder}')
    def create(self, validated_data):
        try:
            folder = Folder.objects.create()
            files = validated_data.get('files', [])
            file_objs = []
            for file in files:
                file_obj = Files.objects.create(folder=folder, files=file)
                file_objs.append(file_obj)
            self.zip_folder(folder.uid)
            return {'files': {} , 'folder': folder.uid}
        except Exception as e:
            print(e)
            raise serializers.ValidationError(str(e))
