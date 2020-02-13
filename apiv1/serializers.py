from rest_framework import serializers

from blacklist.models import BlackUrl


class BlackUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlackUrl
        fields = ['id', 'name', 'url', 'comment']
