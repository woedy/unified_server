from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class AdminPrivilegeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdminPrivilege
        fields = ['id',
                  'create_user',
                  'edit_user',
                  'delete_user',

                  'generate_reports',

                  'email_notification_settings',
                  'customer_support',
                  'logs_access',


                  ]

