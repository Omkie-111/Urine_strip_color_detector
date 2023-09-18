from django.db import models

class UrineStrip(models.Model):
    image = models.ImageField(upload_to='urine_strips/')
    colors_json = models.JSONField(blank=True, null=True)
