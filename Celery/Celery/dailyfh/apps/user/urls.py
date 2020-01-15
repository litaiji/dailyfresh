from django.conf.urls import url

from apps.user import views
from user.views import RegisterView
from user.views import ActiveView

urlpatterns = [
    # url(r'^register$',views.register, name='register'),
    # url(r'^register_handle$',views.register_handle, name='register_handle'),
    # url(r"^test$",views.test, name='test'),

    url(r'^register$',RegisterView.as_view(), name='register'),
    url(r'^active/(?P<token>.*)$',ActiveView.as_view(), name='active'),

]
