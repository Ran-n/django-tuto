#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2022/01/16 15:05:23.120443
#+ Editado:	2022/01/16 15:05:29.056149
# ------------------------------------------------------------------------------

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('Índice de enquisas')
