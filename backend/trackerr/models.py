from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from globals import DEFAULT_MAX_LENGTH, SMALL_MAX_LENGTH
from backend.trackerr.choices import ApplicationStatusChoices, CompanyDetailTypeChoices
from backend.trackerr import managers


class User(AbstractBaseUser, PermissionsMixin):
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"

    objects = managers.UserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.id} - {self.full_name()}"

    def full_name(self):
        return f"{self.id} - {self.email}"


class Company(models.Model):
    name = models.CharField(max_length=DEFAULT_MAX_LENGTH)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return f"{self.id} - {self.name}"


class CompanyDetail(models.Model):
    type = models.CharField(max_length=1, choices=CompanyDetailTypeChoices.choices)
    value = models.CharField(max_length=DEFAULT_MAX_LENGTH)

    # Foreign Fields
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Company Detail"
        verbose_name_plural = "Company Details"

    def __str__(self):
        return f"{self.id} - {self.user} - {self.company.name} - {self.value}"


class JobApplication(models.Model):
    applying_date = models.DateField()
    status = models.CharField(max_length=1, choices=ApplicationStatusChoices.choices)

    # Foreign Fields
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Application"
        verbose_name_plural = "Applications"

    def __str__(self):
        return f"{self.id} - {self.user} - {self.company.name} - {self.status}"


class Event(models.Model):
    title = models.CharField(max_length=DEFAULT_MAX_LENGTH)
    date = models.DateField()
    remarks = models.TextField(blank=True, null=True)
    tags = models.CharField(max_length=DEFAULT_MAX_LENGTH, blank=True, null=True)

    # Foreign Fields
    job_application = models.ForeignKey(JobApplication, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return f"{self.id} - {self.title} - {self.user} - {self.job_application}"