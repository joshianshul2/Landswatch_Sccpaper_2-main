from __future__ import unicode_literals
from django.db import models
# import django_tables2 as tables

class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Journal(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    publish_date = models.DateTimeField()
    views = models.IntegerField(default=0)
    reviewed = models.BooleanField(default=False)

    def __str__(self):
        return self.title









class StatusMaster(models.Model):
    status = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class PropertyMaster(models.Model):
    accountId = models.BigIntegerField()
    acres = models.FloatField()
    adTargetingCountyId = models.BigIntegerField()
    address = models.CharField(max_length=255)
    baths = models.BigIntegerField()
    beds = models.BigIntegerField()
    brokerCompany= models.CharField(max_length=255)
    brokerName = models.CharField(max_length=255)
    Url = models.URLField(max_length=255)
    city = models.CharField(max_length=255)
    cityID= models.BigIntegerField()
    companyLogoDocumentId = models.BigIntegerField()
    county= models.CharField(max_length=255)
    countyId = models.BigIntegerField()
    description = models.TextField(max_length=255)
    hasHouse = models.BooleanField()
    hasVideo = models.BooleanField()
    hasVirtualTour = models.BooleanField()
    hasVirtualTour = models.BigIntegerField()
    imageCount = models.BigIntegerField()
    imageAltTextDisplay = models.CharField(max_length=255)
    # PK_id = models.BigIntegerField(default=0)
    isHeadlineAd = models.BooleanField()
    lwPropertyId = models.BigIntegerField()
    isALC = models.BigIntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    price = models.FloatField()
    types = models.TextField(max_length=255)
    state = models.CharField(max_length=255)
    status = models.CharField(max_length=20)
   #status1 = models.CharField(max_length=255)
    zip = models.BigIntegerField()
    Rate = models.FloatField()
    #NetPrAr = models.FloatField(default=0.00)
    Descrpt = models.CharField(max_length=255,null = True)
    created_at = models.CharField(max_length=255)
    updated_at = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)   

class AvgMaster(models.Model):
    # acres = models.FloatField()
    county = models.CharField(max_length=255)
    # price = models.FloatField()
    state = models.CharField(max_length=255)
    NetPrAr = models.FloatField(default=0.00)
    Rate = models.FloatField()
    UserPercentage = models.FloatField(default=0.00)
    FinaleValue = models.FloatField(default=0.00)
    accountId = models.BigIntegerField()
    acres = models.FloatField()
    adTargetingCountyId = models.BigIntegerField()
    address = models.CharField(max_length=255)
    baths = models.BigIntegerField()
    beds = models.BigIntegerField()
    brokerCompany = models.CharField(max_length=255)
    brokerName = models.CharField(max_length=255)
    Url = models.URLField(max_length=255)
    city = models.CharField(max_length=255)
    cityID = models.BigIntegerField()
    companyLogoDocumentId = models.BigIntegerField()
    countyId = models.BigIntegerField()
    description = models.TextField(max_length=255)
    hasHouse = models.BooleanField()
    hasVideo = models.BooleanField()
    hasVirtualTour = models.BooleanField()
    hasVirtualTour = models.BigIntegerField()
    imageCount = models.BigIntegerField()
    imageAltTextDisplay = models.CharField(max_length=255)
    # PK_id = models.BigIntegerField(default=0)
    isHeadlineAd = models.BooleanField()
    lwPropertyId = models.BigIntegerField()
    isALC = models.BigIntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    price = models.FloatField()
    types = models.TextField(max_length=255)
    status = models.CharField(max_length=20)
    status1 = models.CharField(max_length=255)
    zip = models.BigIntegerField()
    Descrpt = models.TextField(max_length=255, default="!")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    # MY_CHOICES = (
    #     ('a', 'Hola'),
    #     ('b', 'Hello'),
    #     ('c', 'Bonjour'),
    #     ('d', 'Boas'),
    # )
    # my_field = models.CharField(max_length=1, choices=MY_CHOICES)

class TypeMaster(models.Model):
    class Meta:
                app_label = "socialcustom"
                managed = True
    TypeId = models.IntegerField()
    TypeName = models.CharField(max_length=255)

class Property_TypeMaster(models.Model):
        class Meta:
                app_label = "socialcustom"
                managed = True
                # unique_together = (('lwPropertyId', 'TypeId'),)
        Prop_Id2 = models.IntegerField(default=0)
        Type_Id2 = models.IntegerField(default=0)
        # Prop_Id = models.ManyToManyField(PropertyMaster)
        # Type_Id = models.ManyToManyField(TypeMaster)
        # TypeId = models.ForeignKey(TypeMaster, on_delete=models.CASCADE)
        # lwPropertyId = models.ForeignKey(PropertyMaster, on_delete=models.CASCADE)
        #

class RatioDetails(models.Model):
    state = models.CharField(max_length=255)
    percentage = models.IntegerField()


class Description(models.Model):
    # Descrpt = models.IntegerField(primary_key=True)
    Descrpt = models.CharField(max_length=255,null=True)
    def __str__(self):
        return self.Descrpt

class Remark(models.Model) :
    lwPropertyId = models.BigIntegerField()
    Descrpt = models.CharField(max_length=255, null=True)