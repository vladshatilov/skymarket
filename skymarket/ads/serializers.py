from rest_framework import serializers

# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою
from ads.models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    class Meta:
        model = Comment
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    class Meta:
        model = Ad
        fields = ["pk", "title", "price", "author", "created_at", "image"]


class AdDetailSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    class Meta:
        model = Ad
        # fields = '__all__'
        fields = ["pk", "title", "price", "author", "created_at", "image"]
