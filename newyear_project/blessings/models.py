from django.db import models

class PresetBlessing(models.Model):
    content = models.TextField()
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:30]


class UserBlessing(models.Model):
    from_email = models.EmailField(blank=True, null=True)  # 메일 받은 사람(내 이메일)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f"from={self.from_email} {self.created_at:%Y-%m-%d}"
