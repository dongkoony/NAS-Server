# ./nas_app/models.py

from django.db import models

class NASFile(models.Model):
    file = models.FileField(upload_to='', storage=None)  # `upload_to` 속성을 비워 두면 기본적으로 MEDIA_ROOT에 저장됩니다.
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.file.name
