import datetime
import random
from django.core.management.base import BaseCommand
from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Sum, Avg
from core.views import Alert2 ,testemail
from core.models import  UserManager, PropertyMaster, Property_TypeMaster, TypeMaster, AvgMaster,RatioDetails
import requests

from django.core import mail
from django.template.loader import render_to_string

from django.utils.html import strip_tags
from django.db.models import F

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        self.MailTester()

    def MailTester(self):
            a = RatioDetails.objects.all()
            for i in a:
                print("Hello from Mail Maker", i.state, i.percentage)
                print("Percentage", type(i.percentage))
                df1 = Alert2(i.state, i.percentage)
                file_name = i.state + "_" + str(i.percentage) + ".csv"
                testemail(df1, file_name,i.state,i.percentage)
            print("QUIT MAIL")
