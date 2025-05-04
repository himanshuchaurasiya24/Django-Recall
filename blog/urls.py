


from django.urls import path, include
from blog import views
from blog.views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('blog', views.BlogModelViewSet, basename='Blog ModelViewSet')  # Registering the BlogModelViewSet with the router
router.register('comment', views.CommentModelViewSet, basename='Comment ModelViewSet')  # Registering the CommentModelViewSet with the router

urlpatterns = [
    # path('blog/', BlogListCreateView.as_view(), name='blog-list-create'),
    # path('blog/<int:pk>', BlogRetrieveUpdateDestroyView.as_view(), name='blog-list-create'), # URL for the blogs retrieve update delete view
    # path('comment/', CommentListCreateView.as_view(), name='comment-list-create'),  # URL for the comment list and create view
    # path('comment/<int:pk>', CommentRetrieveUpdateDestroyView.as_view(), name='comment-retrieve-update-delete'),  # URL for the comment retrieve update delete view
    path('', include(router.urls))
]
