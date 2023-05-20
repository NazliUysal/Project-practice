from django.urls import path
from artwork.views import home, timeline, upload, postDetail

urlpatterns = [
    path('home/', home, name="home"),
    path('timeline/', timeline, name="timeline"),
    path('upload/', upload, name="upload"),
    path('<uuid:post_id>/', postDetail, name='post-detail'),
]
