from django.db import models
from django.core.validators import RegexValidator, URLValidator, EmailValidator, MinLengthValidator

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255, blank=False ,validators=[MinLengthValidator(5)])
    email_id = models.EmailField(blank=False, validators=[EmailValidator()])
    company_code = models.CharField(max_length=5, blank=True, unique=True, null=True, validators=[RegexValidator(r'^[A-Za-z]{2}\d{2}[EN]$')])
    strength = models.PositiveIntegerField(blank=True, null=True)
    website = models.URLField(null=True, blank=True, validators=[URLValidator()])
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name



