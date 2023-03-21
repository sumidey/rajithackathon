"""MenstruGuide URL Configuration

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
from DiscussionForum import views
from PCOS_Prediction import views as pview
from Awareness import views as vi
from Trackers import views as vt
from home import views as vh

urlpatterns = [
    path('',vh.homePg),
    path('discussionForum', views.DiscussionForm),
    path('discussionForum/data/my_func',views.DiscussionData),
    path('pcosHome', pview.home),
    path('pcosPredict/', pview.predict),
    path('pcosPredict/result',pview.result),
    path('pcosPredict/nextPeriod', vt.nextPeriod),
    path('ovulation', vt.ovulation),
    path('pregnancyTracker', vt.pregnancyTracker),
    path('login',vh.login),
    path('MenstrualAwareness',vi.MenstrualAwareness),
    path('absenceOfPeriods',vi.absenceOfPeriods),
    path('acneBreakout',vi.acneBreakout),
    path('adaptgoodskin',vi.adaptgoodskin),
    path('anemia',vi.anemia),
    path('bodyBreakouts',vi.bodyBreakouts),
    path('contact',vi.contact),
    path('doDont',vi.doDont),
    path('dryness',vi.dryness),
    path('hairchange',vi.hairchange),
    path('healthyHair',vi.healthyHair),
    path('homeRemedies',vi.homeRemedies),
    path('hygiene',vi.hygiene),
    path('irregularPeriods',vi.irregularPeriods),
    path('lightPeriods',vi.lightPeriods),
    path('menopause',vi.menopause),
    path('menstrualPainHR',vi.menstrualPainHR),
    path('oilyhair',vi.oilyhair),
    path('overcomeDarkSpot',vi.overcomeDarkSpot),
    path('overcomeDryness',vi.overcomeDryness),
    path('premenstrual',vi.premenstrual),
    path('protectSkin',vi.protectSkin),
    path('rashes',vi.rashes),
    path('sheddingOfHairs',vi.sheddingOfHairs),
    path('skinChange',vi.skinChange),
    path('skinProblems',vi.skinProblems),
    path('vaginalInfectionsHR',vi.vaginalInfectionsHR),
    path('vaginalItching',vi.vaginalItching),
    path('whyacne',vi.whyacne),
    path('whyacneoccurs',vi.whyacneoccurs),
    path('whylate',vi.whylate),
    path('yoga',vi.yoga),
     path('quiz',vi.quiz),
    path('admin/', admin.site.urls)
]

