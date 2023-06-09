from django.contrib.auth.validators import UnicodeUsernameValidator
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from rest_framework import serializers

from reviews.models import Category, Comment, Genre, GenreTitle, Review, Title
from users.models import User
from users.validators import validate_username


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'slug')


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name', 'slug')


class TitleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)
    genre = GenreSerializer(many=True)
    rating = serializers.IntegerField(
        source='reviews__score__avg', read_only=True)

    class Meta:
        model = Title
        fields = '__all__'


class TitleCreateUpdateSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug',
        required=True
    )
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True,
        required=True
    )
    description = serializers.CharField(required=False)

    class Meta:
        model = Title
        fields = '__all__'
        read_only_fields = ('rating',)

    def create(self, validated_data):
        genres = validated_data.pop('genre')
        title = Title.objects.create(**validated_data)

        for genre in genres:
            genre = get_object_or_404(Genre, slug=genre.slug)
            GenreTitle.objects.create(genre=genre, title=title)
        return title

    def validate_year(self, value):
        if value > now().year:
            raise serializers.ValidationError('Неверный год выпуска')
        return value


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        model = Review

    def validate(self, data):
        if self.context['request'].method != 'POST':
            return data
        user = self.context['request'].user
        title_id = (
            self.context['request'].parser_context['kwargs']['title_id']
        )
        if Review.objects.filter(author=user, title__id=title_id).exists():
            raise serializers.ValidationError(
                'Вы уже оставили отзыв на данное произведение'
            )
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Comment


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        )
        model = User


class ProfileSerializer(UserSerializer):
    role = serializers.CharField(read_only=True)


class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=150, required=True,
        validators=[UnicodeUsernameValidator(), validate_username],
    )
    email = serializers.EmailField(max_length=254, required=True)

    def validate(self, data):
        if User.objects.filter(
            username=data['username'], email=data['email']
        ).exists():
            return data

        if User.objects.filter(username=data['username'].lower()).exists():
            raise serializers.ValidationError(
                'Пользователь с таким `username` уже существует'
            )

        if User.objects.filter(email=data['email'].lower()).exists():
            raise serializers.ValidationError(
                'Пользователь с таким `email` уже существует'
            )

        return data


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=150, required=True,
        validators=[UnicodeUsernameValidator(), ],
    )
    confirmation_code = serializers.CharField(max_length=36, required=True)
