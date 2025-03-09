from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
                path('',views.IndexView.as_view(), name='index'),
                path('admin/',admin.site.urls),
                path('<int:question_id>/',views.detail, name='detail'),
                path('<int:id>/results/', views.ResultsView.as_view(), name='results'),
                path('<int:question_id>/vote/',views.vote, name='vote'),
                
]