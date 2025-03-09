from django.contrib import admin
from django.urls import path, include
import tasks.views as views


 # Import your app views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls'))  # Include your app's URLs
]
