#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2022/01/16 15:03:04.624874
#+ Editado:	2022/01/22 16:11:44.652235
# ------------------------------------------------------------------------------
from django.urls import path
from . import views
# ------------------------------------------------------------------------------
app_name = 'polls'
urlpatterns = [
        # /polls
        path('', views.IndexView.as_view(), name='index'),

        # /pools/{id}
        path('<int:pk>', views.DetailView.as_view(), name='detail'),

        # /pools/{id}/results
        path('<int:pk>/results', views.ResultsView.as_view(), name='results'),

        # /pools/{id}/vote
        path('<int:question_id>/vote', views.vote, name='vote'),
        ]
# ------------------------------------------------------------------------------

