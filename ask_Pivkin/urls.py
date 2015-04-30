from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'ask_Pivkin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^helloworldapp/', 'ask_Pivkin.views.helloworldapp'),
    url(r'^$', 'ask_Pivkin.views.index'),
    url(r'^registration/', 'ask_Pivkin.views.signup'),
    url(r'^login', 'ask_Pivkin.views.login'),
    url(r'^newquestion/', 'ask_Pivkin.views.ask'),	
    url(r'^question/', 'ask_Pivkin.views.question'),
    url(r'^admin/', include(admin.site.urls)),
]
