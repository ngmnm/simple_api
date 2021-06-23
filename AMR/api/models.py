from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Vender(models.Model):

    Vender_ID = models.IntegerField(validators=[MinValueValidator(1),
                                                MaxValueValidator(99999)], primary_key=True, null=False)
    VENDOR_NAME = models.CharField(max_length=100, null=False)
    IS_ACTIVE = models.IntegerField(validators=[MinValueValidator(1),
                                                MaxValueValidator(99999)], default=1, null=False)
    COMMENTS = models.CharField(max_length=2000, null=True, blank=True)
    DELETE_STATUS = models.IntegerField(
        validators=[MinValueValidator(0),
                    MaxValueValidator(1)], default=0, null=False)
    CREATED_USER_ID = models.IntegerField(validators=[MinValueValidator(1),
                                                      MaxValueValidator(99999)])
    CREATED_DATE = models.DateTimeField(auto_now_add=True)
    UPDATED_USER_ID = models.IntegerField(validators=[MinValueValidator(1),
                                                      MaxValueValidator(99999)], null=True, blank=True)
    UPDATED_DATE = models.DateField(null=True, blank=True)


class DeviceModel(models.Model):

    MODEL_ID = models.IntegerField(validators=[MinValueValidator(1),
                                               MaxValueValidator(99999)], primary_key=True, null=False)
    MODEL_NAME = models.CharField(max_length=100, null=False)
    Vender_ID = models.IntegerField(validators=[MinValueValidator(1),
                                                MaxValueValidator(99999)],  null=False)
    DEVICE_TYPE_ID = DELETE_STATUS = models.IntegerField(
        validators=[MinValueValidator(0),
                    MaxValueValidator(99)])
    IS_ACTIVE = models.IntegerField(validators=[MinValueValidator(1),
                                                MaxValueValidator(99999)], default=1, null=False)
    COMMENTS = models.CharField(max_length=2000, null=True, blank=True)
    DELETE_STATUS = models.IntegerField(
        validators=[MinValueValidator(0),
                    MaxValueValidator(1)], default=0, null=False)
    CREATED_USER_ID = models.IntegerField(validators=[MinValueValidator(1),
                                                      MaxValueValidator(99999)])
    CREATED_DATE = models.DateTimeField(auto_now_add=True)
    UPDATED_USER_ID = models.IntegerField(validators=[MinValueValidator(1),
                                                      MaxValueValidator(99999)], null=True, blank=True)
    UPDATED_DATE = models.DateField(null=True, blank=True)
    MAX_ACCEPTED_READING = models.IntegerField(null=True, blank=True)
    ONNECTION_TYPE = models.CharField(max_length=20, null=True, blank=True)
