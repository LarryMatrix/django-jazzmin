"""DjangoJazzmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin, messages
from django.urls import path, reverse, include
from django.http import HttpResponseRedirect
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


def make_messages(request):
    messages.add_message(request, messages.INFO, "Info message")
    messages.add_message(request, messages.ERROR, "Error message")
    messages.add_message(request, messages.WARNING, "Warning message")
    messages.add_message(request, messages.SUCCESS, "Success message")

    return HttpResponseRedirect(reverse("admin:index"))

prefix = 'hprs/api/v1'


urlpatterns = [
    path('admin/', admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),

    # path(f'{prefix}/auth/', include('djoser.urls')),
    # path(f'{prefix}/auth/', include('djoser.urls.authtoken')),
    path(f'{prefix}/facility/',
         include('facility.urls', namespace='facility')),
]

urlpatterns += i18n_patterns(path("admin/", admin.site.urls))

urlpatterns += staticfiles_urlpatterns()

# if settings.DEBUG:
#     urlpatterns.append(
#         re_path(
#             r"^static/(?P<path>.*)$",
#             serve,
#             kwargs={"document_root": settings.STATIC_ROOT},
#         )
#     )


# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL,
#                           document_root=settings.STATIC_ROOT)


