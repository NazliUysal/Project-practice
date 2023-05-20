from django.urls import path
from artwork.views import home, timeline, upload, postDetail

urlpatterns = [
    path('home/', home, name="home"),
    path('timeline/', timeline, name="timeline"),
    path('upload/', upload, name="upload"),
    #Heres the new url for the post-detail here we pass the post id as requested by the id in this way:
    #In timeline template we can see how we call this url and pass the id.
    path('<uuid:post_id>/', postDetail, name='post-detail'),
]
