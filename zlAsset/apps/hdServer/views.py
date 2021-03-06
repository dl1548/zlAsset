# -*- coding:utf-8 -*-
# Author: zili

from django.shortcuts import render,HttpResponse
from urllib.parse import quote, unquote
from django.http import JsonResponse,HttpResponseRedirect

# FBV(function base views) 登录校验
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
#from django.db.models import Q
# Create your views here.
import time,datetime
import json
import base64
from .sync_hddata import SyncHdInfo
from .models import *

@login_required(login_url='/login/')
def index(request):
    hdServer_data =Data.objects.all()
    return render(request,'hdServer/index.html',{'hdServer_data':hdServer_data})

# def task_add_test(request):
#     x = request.GET['x']
#     y = request.GET['y']

#     from .tasks import add
#     #delay函数实现异步
#     result = add.delay(x,y)
#     res = {'code':200, 'message':'ok', 'data':[{'x':x, 'y':y}]}
#     return render(request, 'hdServer/return_value.html', {'return_value': json.dumps(res)})
# #     #result.ready()     #判断任务是否完成处理 True 或 False
# #     #result.get(timeout=1)  # 可以重新抛出异常
# #     #result.traceback   #可以获取原始的回溯信息

#添加服务器
def add_hd(request):
    return render(request, 'hdServer/add_hd.html')
def add_hd_action(request):
    if request.method == 'POST':
        name=request.POST.get('name','未填写')
        brand=request.POST['brand']
        brand_type=request.POST['brand_type']
        run_env=request.POST['run_env']
        manager_ip=request.POST['manager_ip']
        device_ip=request.POST['device_ip']
        description=request.POST['description']
        oper_member=request.POST['oper_member']
        department=request.POST['department']
        team=request.POST['team']
        use_member=request.POST['use_member']
        position=request.POST['position']
        datacenter=request.POST['datacenter']
        cabinet=request.POST['cabinet']
        u_num=request.POST['u_num']
        u_start=request.POST['u_start']
        u_end=request.POST['u_end']
        asset_num=request.POST['asset_num']
        asset_sn=request.POST['asset_sn']
        support_start=request.POST['support_start']
        support_end=request.POST['support_end']
        hd_cost=request.POST['hd_cost']
        supplier=request.POST['supplier']

        val = Data.objects.filter(name=name)
        if not val:
            Data.objects.create(
                name=name,
                brand=brand,
                brand_type=brand_type,
                run_env=run_env,
                manager_ip=manager_ip,
                device_ip=device_ip,
                description=description,
                oper_member=oper_member,
                department=department,
                team=team,
                use_member=use_member,
                position=position,
                datacenter=datacenter,
                cabinet=cabinet,
                u_num=u_num,
                u_start=u_start,
                u_end=u_end,
                asset_num=asset_num,
                asset_sn=asset_sn,
                support_start=support_start,
                support_end=support_end,
                hd_cost=hd_cost,
                supplier=supplier,
                )
            hdServer_data =Data.objects.all()
            return render(request,'hdServer/index.html',{'hdServer_data':hdServer_data })
        else:
            error_data = name+'已存在'
            hdServer_data =Data.objects.all()
            return render(request,'hdServer/index.html',{'hdServer_data':hdServer_data,'error_data':error_data})
    else:
        return HttpResponseRedirect ('/hdServer/index/')

def modify_hd(request,id):
    hdServer_data =Data.objects.get(id=id)
    return render(request,'hdServer/modify_hd.html',{'hdServer_data':hdServer_data})
def modify_hd_action(request):
    if request.method == 'POST':
        id=request.POST['id']
        name=request.POST['name']
        brand=request.POST['brand']
        brand_type=request.POST['brand_type']
        run_env=request.POST['run_env']
        manager_ip=request.POST['manager_ip']
        device_ip=request.POST['device_ip']
        description=request.POST['description']
        oper_member=request.POST['oper_member']
        department=request.POST['department']
        team=request.POST['team']
        use_member=request.POST['use_member']
        position=request.POST['position']
        datacenter=request.POST['datacenter']
        cabinet=request.POST['cabinet']
        u_num=request.POST['u_num']
        u_start=request.POST['u_start']
        u_end=request.POST['u_end']
        asset_num=request.POST['asset_num']
        asset_sn=request.POST['asset_sn']
        support_start=request.POST['support_start']
        support_end=request.POST['support_end']
        hd_cost=request.POST['hd_cost']
        supplier=request.POST['supplier']

        hd_data=Data.objects.get(id=id)
        cert = Cert.objects.filter(hd_name=hd_data.name)
        if cert:
            Cert.objects.filter(hd_name=hd_data.name).update(hd_name=name)

        Data.objects.filter(id=id).update(
            name=name,
            brand=brand,
            brand_type=brand_type,
            run_env=run_env,
            manager_ip=manager_ip,
            device_ip=device_ip,
            description=description,
            oper_member=oper_member,
            department=department,
            team=team,
            use_member=use_member,
            position=position,
            datacenter=datacenter,
            cabinet=cabinet,
            u_num=u_num,
            u_start=u_start,
            u_end=u_end,
            asset_num=asset_num,
            asset_sn=asset_sn,
            support_start=support_start,
            support_end=support_end,
            hd_cost=hd_cost,
            supplier=supplier,
            )


        hdServer_data =Data.objects.all()
        return render(request,'hdServer/index.html',{'hdServer_data':hdServer_data })
    else:
        return HttpResponseRedirect ('/hdServer/index/')

# 删除服务器
def delete_hd(request,id):
    hd_data=Data.objects.get(id=id)
    cert=Cert.objects.filter(hd_name=hd_data.name)
    if cert:
        cert_data=Cert.objects.get(hd_name=hd_data.name)
        if cert_data.way=='ipmi':
            IpmiData.objects.filter(cert_ip=cert_data.ip).delete()
        if cert_data.way=='ilo':
            IloData.objects.filter(cert_ip=cert_data.ip).delete()
        Cert.objects.filter(hd_name=hd_data.name).delete()
    Data.objects.filter(id=id).delete()
    hdServer_data =Data.objects.all()
    return render(request,'hdServer/index.html',{'hdServer_data':hdServer_data})


def base_detail(request,id):
    hdServer_data =Data.objects.get(id=id)
    return render(request,'hdServer/base_detail.html',{'hdServer_data':hdServer_data})

def hd_detail(request,id):
    hdServer_data =Data.objects.get(id=id)

    cert = Cert.objects.filter(hd_name=hdServer_data.name)
    if cert:
        Cert_data = Cert.objects.get(hd_name=hdServer_data.name)
        if Cert_data.way=='ipmi':
            if IpmiData.objects.filter(cert_ip=Cert_data.ip):
                synchd_data = IpmiData.objects.get(cert_ip=Cert_data.ip)
            else:
                synchd_data=None
        if Cert_data.way=='ilo':
            if IloData.objects.filter(cert_ip=Cert_data.ip):
                synchd_data = IloData.objects.get(cert_ip=Cert_data.ip)
            else:
                synchd_data=None
    else:
        Cert_data = None
        synchd_data = None
    return render(request,'hdServer/hd_detail.html', \
        {'hdServer_data':hdServer_data,'Cert_data':Cert_data,'synchd_data':synchd_data})

def set_cert(request,id):
     if request.method == 'POST':
        ip=request.POST['ip']
        way=request.POST['way']
        username=request.POST['username']
        password_b=request.POST['password']
        password=bytes.decode(base64.b64encode(bytes(password_b,encoding='utf-8')))
        hdServer_data =Data.objects.get(id=id)
        val = Cert.objects.filter(hd_name=hdServer_data.name)
        if not val:
            Cert.objects.create(
                hd_name=hdServer_data.name,
                ip=ip,
                way=way,
                username=username,
                password=password,
                sync='on'
                )
        else:
            Cert.objects.filter(hd_name=hdServer_data.name).update(
                hd_name=hdServer_data.name,
                ip=ip,
                way=way,
                username=username,
                password=password,
                sync='on'
            )

        return HttpResponseRedirect ("/hdServer/hd_detail/"+str(id))

def set_sync(request,id):
    hdServer_data =Data.objects.get(id=id)
    hd_name=hdServer_data.name

    if request.method == 'POST':
        val = Cert.objects.get(hd_name=hd_name)
        sync = val.sync
        if sync == 'on':
            sync = 'off'
        else:
            sync = 'on'
            way = val.way

            if way=='ipmi':
                ipmi_login = SyncHdInfo(
                    username=val.username,
                    password=bytes.decode(base64.b64decode(bytes(val.password,encoding='utf-8'))),
                    server=val.ip
                    )
                ipmi_info = ipmi_login.get_hd_info_ipmi()
                if 'error' in ipmi_info:
                     sync_result[ip] = ipmi_info['error']
                else:
                    update_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    ipmi_data = IpmiData.objects.filter(cert_ip=val.ip)
                    if not ipmi_data:
                        IpmiData.objects.create(
                            cert_ip=val.ip,
                            brand=ipmi_info['hd']['brand'],
                            product_name=ipmi_info['hd']['product_name'],
                            uuid=ipmi_info['uuid'],
                            fw=ipmi_info['fw'],
                            way='ipmi',
                            ip=ipmi_info['net']['IPAddress'],
                            mac=ipmi_info['net']['MACAddress'],
                            sn=ipmi_info['hd']['sn'],
                            update_time=update_time
                        )
                    else:
                        IpmiData.objects.filter(cert_ip=val.ip).update(
                            cert_ip=val.ip,
                            brand=ipmi_info['hd']['brand'],
                            product_name=ipmi_info['hd']['product_name'],
                            uuid=ipmi_info['uuid'],
                            fw=ipmi_info['fw'],
                            way='ipmi',
                            ip=ipmi_info['net']['IPAddress'],
                            mac=ipmi_info['net']['MACAddress'],
                            sn=ipmi_info['hd']['sn'],
                            update_time=update_time
                        )
            if way=='ilo':
                ilo_login = SyncHdInfo(
                    username=val.username,
                    password=bytes.decode(base64.b64decode(bytes(val.password,encoding='utf-8'))),
                    server=val.ip
                    )
                ilo_info = ilo_login.get_hd_info_ilo()

                update_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                ilo_data = IloData.objects.filter(cert_ip=val.ip)
                if not ilo_data:
                    IloData.objects.create(
                        cert_ip=val.ip,
                        product_name=ilo_info['product_name'],
                        uuid=ilo_info['uuid'],
                        fw=ilo_info['fw_ver'],
                        way='ilo',
                        ip=val.ip,
                        mac=ilo_info['net_mac']['Embedded'],
                        sn=ilo_info['sn'],
                        license=ilo_info['license'],
                        update_time=update_time
                    )
                else:
                    IloData.objects.filter(cert_ip=val.ip).update(
                        cert_ip=val.ip,
                        product_name=ilo_info['product_name'],
                        uuid=ilo_info['uuid'],
                        fw=ilo_info['fw_ver'],
                        way='ilo',
                        ip=val.ip,
                        mac=ilo_info['net_mac']['Embedded'],
                        sn=ilo_info['sn'],
                        license=ilo_info['license'],
                        update_time=update_time
                    )

        Cert.objects.filter(hd_name=hd_name).update(sync=sync)
    else:
        pass
    return HttpResponseRedirect ("/hdServer/hd_detail/"+str(id))



# task使用
def hd_data_sync():
    # ipmi_login = SyncHdInfo(username='lenovo',password='lenovo',server='192.168.1.231')
    # ipmi_info = ipmi_login.get_hd_info_ipmi()
    # return ipmi_info
    sync_result={}
    cert_data=Cert.objects.all()

    if cert_data:
        for c in cert_data:
            if c.sync=='on':
                if c.way=='ipmi':
                    ipmi_login = SyncHdInfo(
                        username=c.username,
                        password=bytes.decode(base64.b64decode(bytes(c.password,encoding='utf-8'))),
                        server=c.ip
                        )
                    ipmi_info = ipmi_login.get_hd_info_ipmi()

                    if 'error' in ipmi_info:
                         sync_result[c.ip] = ipmi_info['error']
                    else:
                        update_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        val = IpmiData.objects.filter(cert_ip=c.ip)
                        if not val:
                            IpmiData.objects.create(
                                cert_ip=c.ip,
                                brand=ipmi_info['hd']['brand'],
                                product_name=ipmi_info['hd']['product_name'],
                                uuid=ipmi_info['uuid'],
                                fw=ipmi_info['fw'],
                                way='ipmi',
                                ip=ipmi_info['net']['IPAddress'],
                                mac=ipmi_info['net']['MACAddress'],
                                sn=ipmi_info['hd']['sn'],
                                update_time=update_time
                            )
                            sync_result[c.ip] = 'ipmi sync success'
                        else:
                            IpmiData.objects.filter(cert_ip=c.ip).update(
                                cert_ip=c.ip,
                                brand=ipmi_info['hd']['brand'],
                                product_name=ipmi_info['hd']['product_name'],
                                uuid=ipmi_info['uuid'],
                                fw=ipmi_info['fw'],
                                way='ipmi',
                                ip=ipmi_info['net']['IPAddress'],
                                mac=ipmi_info['net']['MACAddress'],
                                sn=ipmi_info['hd']['sn'],
                                update_time=update_time
                            )
                            sync_result[c.ip] = 'ipmi sync update success'
                if c.way=='ilo':
                    ilo_login = SyncHdInfo(
                        username=c.username,
                        password=bytes.decode(base64.b64decode(bytes(c.password,encoding='utf-8'))),
                        server=c.ip
                        )
                    ilo_info = ilo_login.get_hd_info_ilo()

                    update_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    val = IloData.objects.filter(cert_ip=c.ip)
                    if not val:
                        IloData.objects.create(
                            cert_ip=c.ip,
                            product_name=ilo_info['product_name'],
                            uuid=ilo_info['uuid'],
                            fw=ilo_info['fw_ver'],
                            way='ilo',
                            ip=c.ip,
                            mac=ilo_info['net_mac']['Embedded'],
                            sn=ilo_info['sn'],
                            license=ilo_info['license'],
                            update_time=update_time
                        )
                        sync_result[c.ip] = 'ilo sync success'
                    else:
                        IloData.objects.filter(cert_ip=c.ip).update(
                            cert_ip=c.ip,
                            product_name=ilo_info['product_name'],
                            uuid=ilo_info['uuid'],
                            fw=ilo_info['fw_ver'],
                            way='ilo',
                            ip=c.ip,
                            mac=ilo_info['net_mac']['Embedded'],
                            sn=ilo_info['sn'],
                            license=ilo_info['license'],
                            update_time=update_time
                        )
                        sync_result[c.ip] = 'ilo sync update success'
            else:
                sync_result[c.ip] ='sync is disabled'
        return sync_result
    else:
        return 'Cert is null'


# @login_required(login_url='/login/')
def test(request):
    # t = make_password("123456")
    # test = check_password('123456',t)
    #test = hd_data_sync()

    login = SyncHdInfo(username='administrator',password='123qweASD',server='192.168.3.11')
    info = login.get_hd_info_ilo()
    # mac = info['net_mac']['Embedded']
    return render(request, 'hdServer/test.html', {'test': info})
