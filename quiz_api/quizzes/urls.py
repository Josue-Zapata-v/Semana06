from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet

# 🤖 Router automatically creates RESTful URLs
router = DefaultRouter()
router.register(r'quizzes', QuizViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),  # 🆕 Version 1 prefix
]