from django.urls import path
from . import apis

urlpatterns = [
    # /api/members/auth-token/
    #  DRF Tutorial에서 했던 AuthTokenAPIView에 연결되도록 함
    # view:     members/apis.py
    # url:      members/urls_apis.py -> config.urls.urlpatterns_apis
    #  (config.urls에서 적절히 include)
    # serializer: members/serializers.py (UserSerializer)

    # INSTALLED_APPS
    #   poetry add
    #  rest_framework
    #  rest_framework.authtoken
    #   -> migrate

    # Postman Collection만들고 (Instagram)
    #  members폴더 내에 AuthTokenAPIView로 요청(항목) 추가
    path('auth-token/', apis.AuthTokenAPIView.as_view()),
]
