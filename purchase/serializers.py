from rest_framework import serializers

from .models import Request
from .services import send_email_admins


class PurchaseSerializer(serializers.ModelSerializer):
    """Сериализатор заявки на покупку, после заявки рассылает email всем администраторам системы"""
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Request
        fields = ('user', 'book', 'phone_number', 'comment', 'date')

    def save(self, **kwargs):
        kwargs["user"] = self.fields["user"].get_default()
        send_email_admins()
        return super().save(**kwargs)
