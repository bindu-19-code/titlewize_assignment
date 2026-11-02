from rest_framework import serializers
from .models import Bookmark

class BookmarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bookmark
        fields = '__all__'
        read_only_fields = ['user', 'created_at']

    def validate_url(self, value):
        if not value.startswith(('http://', 'https://')):
            raise serializers.ValidationError(
                "URL must start with http:// or https://"
            )

        return value

    def validate(self, attrs):
        request = self.context.get('request')

        if request and request.user.is_authenticated:

            existing_bookmark = Bookmark.objects.filter(
                user=request.user,
                url=attrs.get('url')
            )

            if self.instance:
                existing_bookmark = existing_bookmark.exclude(
                    pk=self.instance.pk
                )

            if existing_bookmark.exists():
                raise serializers.ValidationError({
                    'url': 'You have already saved this URL.'
                })

        return attrs