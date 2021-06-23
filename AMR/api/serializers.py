from rest_framework import serializers
from .models import Vender, DeviceModel


class VenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vender
        fields = (
            'Vender_ID', 'VENDOR_NAME', 'IS_ACTIVE', 'COMMENTS', 'DELETE_STATUS', 'CREATED_USER_ID', 'CREATED_DATE', "UPDATED_USER_ID", "UPDATED_DATE"
        )


class deviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceModel
        fields = (            'MODEL_ID',            'MODEL_NAME',            'Vender_ID',            'DEVICE_TYPE_ID',            'IS_ACTIVE',            'COMMENTS',            'DELETE_STATUS',            'CREATED_USER_ID',            'CREATED_DATE',            'UPDATED_USER_ID',            'UPDATED_DATE',
            'MAX_ACCEPTED_READING',
            'ONNECTION_TYPE'

        )
