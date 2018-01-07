from django.db import models
from django.core.exceptions import ValidationError


class Company(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    address = models.CharField(max_length=200, blank=False, null=False)
    phone_number = models.CharField(max_length=200, blank=False, null=False)
    email = models.CharField(max_length=200, blank=False, null=False)
    short_description = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    facebook_link = models.CharField(max_length=200, blank=True, null=True)
    twitter_link = models.CharField(max_length=200, blank=True, null=True)
    google_plus_link = models.CharField(max_length=200, blank=True, null=True)
    email_username = models.CharField(max_length=200, blank=True, null=True)
    email_password = models.CharField(max_length=200, blank=True, null=True)
    linkedin_link = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.name)

    def clean(self):
        """
        require username and password to contact if email
        """
        if self.email_username and not self.email_password:
            raise ValidationError("Email user name and password required together")
        elif self.email_password and not self.email_username:
            raise ValidationError("An ipv4 or ipv6 address is required")
        else:
            pass    


class Service(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    show = models.BooleanField(default=True)
    top_four = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)


class Job(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey('JobCategory', on_delete=models.CASCADE, null=True)
    show = models.BooleanField(default=True)
    before_image_link = models.URLField()
    after_image_link = models.URLField()

    def __str__(self):
        return str(self.name)


class JobCategory(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return str(self.name)


class TeamMember(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    profile_image = models.URLField()
    facebook_link = models.CharField(max_length=200, blank=True, null=True)
    twitter_link = models.CharField(max_length=200, blank=True, null=True)
    google_plus_link = models.CharField(max_length=200, blank=True, null=True)
    linkedin_link = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.name)
