# -*- coding:utf-8 -*-
# Author: zili

from django.db import models

# Create your models here.


class Data(models.Model):
    name = models.CharField(max_length=128,null=True, blank=True)
    brand = models.CharField(max_length=128,null=True, blank=True)
    brand_type = models.CharField(max_length=128,null=True, blank=True)
    run_env = models.CharField(max_length=128,null=True, blank=True)
    manager_ip = models.CharField(max_length=128,null=True, blank=True)
    device_ip = models.CharField(max_length=128,null=True, blank=True)
    description = models.CharField(max_length=128,null=True, blank=True)
    oper_member = models.CharField(max_length=128,null=True, blank=True)
    department = models.CharField(max_length=128,null=True, blank=True)
    team = models.CharField(max_length=128,null=True, blank=True)
    use_member = models.CharField(max_length=128,null=True, blank=True)
    position = models.CharField(max_length=128,null=True, blank=True)
    datacenter = models.CharField(max_length=128,null=True, blank=True)
    cabinet = models.CharField(max_length=128,null=True, blank=True)
    u_num = models.CharField(max_length=128,null=True, blank=True)
    u_start = models.CharField(max_length=128,null=True, blank=True)
    u_end = models.CharField(max_length=128,null=True, blank=True)
    asset_num = models.CharField(max_length=128,null=True, blank=True)
    asset_sn = models.CharField(max_length=128,null=True, blank=True)
    support_start = models.CharField(max_length=128,null=True, blank=True)
    support_end = models.CharField(max_length=128,null=True, blank=True)
    hd_cost = models.CharField(max_length=128,null=True, blank=True)
    supplier = models.CharField(max_length=128,null=True, blank=True)

    def __str__(self):
        return self.name

class Cert(models.Model):
    hd_name=models.CharField(max_length=128,null=True, blank=True)
    ip = models.CharField(max_length=128,null=True, blank=True)
    way = models.CharField(max_length=128,null=True, blank=True)
    username = models.CharField(max_length=128,null=True, blank=True)
    password = models.CharField(max_length=128,null=True, blank=True)
    sync = models.CharField(max_length=128,null=True, blank=True)

    def __str__(self):
        return self.ip

class IpmiData(models.Model):
    cert_ip=models.CharField(max_length=128,null=True, blank=True)
    brand=models.CharField(max_length=128,null=True, blank=True)
    product_name=models.CharField(max_length=128,null=True, blank=True)
    uuid=models.CharField(max_length=128,null=True, blank=True)
    fw = models.CharField(max_length=128,null=True, blank=True)
    way = models.CharField(max_length=128,null=True, blank=True)
    ip = models.CharField(max_length=128,null=True, blank=True)
    mac=models.CharField(max_length=128,null=True, blank=True)
    sn=models.CharField(max_length=128,null=True, blank=True)
    update_time=models.CharField(max_length=128,null=True, blank=True)

    def __str__(self):
        return self.ip

class IloData(models.Model):
    cert_ip=models.CharField(max_length=128,null=True, blank=True)
    product_name=models.CharField(max_length=128,null=True, blank=True)
    uuid=models.CharField(max_length=128,null=True, blank=True)
    fw = models.CharField(max_length=128,null=True, blank=True)
    way = models.CharField(max_length=128,null=True, blank=True)
    ip = models.CharField(max_length=128,null=True, blank=True)
    mac=models.CharField(max_length=128,null=True, blank=True)
    sn=models.CharField(max_length=128,null=True, blank=True)
    license=models.CharField(max_length=128,null=True, blank=True)
    cpu=models.TextField(null=True, blank=True)
    disk=models.TextField(null=True, blank=True)
    memory=models.TextField(null=True, blank=True)
    raid=models.TextField(null=True, blank=True)
    log=models.TextField(null=True, blank=True)
    update_time=models.CharField(max_length=128,null=True, blank=True)

    def __str__(self):
        return self.ip
#models.TextField(null=True, blank=True)
