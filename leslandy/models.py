from django.db import models
from django.utils import timezone


class CompanyDetails (models.Model):
    company = models.ForeignKey('auth.User')
    company_name = models.CharField(max_length=200)
    company_summary = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.company_name
