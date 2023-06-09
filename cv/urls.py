"""cv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

import pdf.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", pdf.views.home, name="home"),
    path("formulaire", pdf.views.formulaire, name="formulaire"),
    path("verification",  pdf.views.verification, name="verification"),
    path("<int:id>", pdf.views.generer, name="generer"),
    path("download", pdf.views.download, name="download"),
    path("retour", pdf.views.retour, name="retour"),
]
