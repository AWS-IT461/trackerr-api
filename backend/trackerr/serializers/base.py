from rest_framework import serializers

from backend.trackerr import models


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"


class CompanyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = "__all__"


class JobApplicationModelSerializer(serializers.ModelSerializer):
    company = CompanyModelSerializer(read_only=True)
    company_id = serializers.PrimaryKeyRelatedField(
        source="company", queryset=models.Company.objects.all(), write_only=True
    )

    class Meta:
        model = models.JobApplication
        fields = "__all__"


class EventModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = "__all__"
