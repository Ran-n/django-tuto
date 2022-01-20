#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2022/01/16 15:03:04.624874
#+ Editado:	2022/01/20 19:49:15.902412
# ------------------------------------------------------------------------------
from django.urls import path
from . import views
# ------------------------------------------------------------------------------
app_name = 'polls'
urlpatterns = [
        # /polls
        path('', views.index, name='index'),
        # /pools/{id}
        path('<int:question_id>/', views.detail, name='detail'),
        # /pools/{id}/results
        path('<int:question_id>/results', views.results, name='results'),
        # /pools/{id}/vote
        path('<int:question_id>/vote', views.vote, name='vote'),
        ]
# ------------------------------------------------------------------------------

