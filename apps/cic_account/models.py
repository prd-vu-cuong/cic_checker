from django.db import models


class CicAccount(models.Model):
    user_name = models.CharField(blank=False, max_length=255, db_index=True)
    password = models.CharField(blank=False, max_length=255)
    is_active = models.BooleanField(default=False)
    is_live = models.BooleanField(default=False, unique=True)

    def __str__(self):
        return f"{self.user_name} - {'live' if self.is_live else 'die'}"

    class Meta:
        db_table = "cic_accounts"
        unique_together = ("user_name", "password")
