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

                  'create_practitioner',
                  'edit_practitioner',
                  'delete_practitioner',

                  'view_appointments',
                  'create_appointments',
                  'modify_appointments',
                  'cancel_appointments',

                  'access_calender',
                  'modify_calender',

                  'generate_reports',

                  'view_transactions',
                  'modify_transaction_status',

                  'email_notification_settings',
                  'customer_support',
                  'logs_access',


                  ]

