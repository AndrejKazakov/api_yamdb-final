from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import UserViewSet
from . import views

router = DefaultRouter()


router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    views.ReviewViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    views.CommentViewSet,
    basename='comments'
)
router.register('categories', views.CategoriesViewSet,
                basename='categories')
router.register('genres', views.GenresViewSet, basename='genres')
router.register('titles', views.TitlesViewSet, basename='titles')
router.register('users', UserViewSet)

app_name = 'api'
urlpatterns = [
    path('auth/', include(
        [
            path('signup/', views.SignUPView.as_view()),
            path('token/', views.TokenView.as_view()),
        ]
    )),
    path('', include(router.urls)),
]
