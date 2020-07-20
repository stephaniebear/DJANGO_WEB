from django.shortcuts import render, redirect
from .models import Post, Result, ResultDetails, Office, Files , Assettype, Location
from django.contrib.auth.models import User, auth
from django.contrib import messages

from django.http import JsonResponse, HttpResponse
from django.core import serializers
import json

from django.utils import timezone
import pytz

import csv, io #CSV Files

from django.core.files.storage import FileSystemStorage #BOOK FILES
import os

from django.contrib.auth.decorators import login_required #For login_required
# Create your views here.

def formAccount(request):
    first_name = request.user.first_name
    last_name = request.user.last_name
    username = request.user.username
    email = request.user.email
    print(first_name)
    print(last_name)
    print(username)
    print(email)
    return render(request,'formAccount.html',
    {
        'first_name' : first_name,
        'last_name' : last_name,
        'username' : username,
        'email' : email
    })

def Home(request):
    #Query Data From Model
    data = Post.objects.all()
    return render(request,'index.html',
    {
        'posts':data,
    })

def Page1(request):
    return render(request,'page1.html',
    {
        'tags':'เชียงใหม่',
    })

def formAddResult(request):

    print('formAddResult')

    # time_zone = pytz.timezone("Asia/Bangkok")
    # utc_dt = timezone.now()
    # loc_dt = utc_dt.astimezone(time_zone)

    # print('Zone : ', loc_dt.year+543)
    # #format_time = '%Y-%m-%d %H:%M:%S %Z (%z)'
    # format_time = '%B'
    # # time_stamp = str(loc_dt.strftime(format_time))
    # time_stamp = str(loc_dt.day) + ' ' + str(loc_dt.strftime(format_time)) + ' ' + str(loc_dt.year+543)

    # print('Time : ', time_stamp)

    if request.method == 'POST':
        def get_timestamp():
            time_zone = pytz.timezone("Asia/Bangkok")
            utc_dt = timezone.now()
            loc_dt = utc_dt.astimezone(time_zone)
            #format_time = '%Y-%m-%d %H:%M:%S %Z (%z)'
            format_time = '%Y%m%d%H%M%S'
            time_stamp = str(loc_dt.strftime(format_time))
            return time_stamp

        print('Time Stamp : ', get_timestamp())


        ##### GET Office Type #####

        name = request.POST['name']
        OfficeQuerys = Office.objects.filter(name__icontains=name)

        for OfficeQuery in OfficeQuerys:
            print('Type : ', OfficeQuery.types)
            type_office = str(OfficeQuery.types)

        ###########################

        ##########################################################################################
        number = request.POST['number']
        name = request.POST['name']
        #type_office = request.POST['type']
        specs_general = request.POST['specs_general']
        specs_elec_general = request.POST['specs_elec_general']
        specs_elec_techniques = request.POST['specs_elec_techniques']
        specs_network_general = request.POST['specs_network_general']
        specs_network_techniques = request.POST['specs_network_techniques']
        book_number = request.POST['book_number']
        book_date = request.POST['book_date']
        descriptions = request.POST['descriptions']
        username = request.user

        print('number : ', number)
        print('name : ', name)
        print('Type : ', type_office)
        print('specs_general : ', specs_general)
        print('specs_elec_general : ', specs_elec_general)
        print('specs_elec_techniques : ', specs_elec_techniques)
        print('specs_network_general : ', specs_network_general)
        print('specs_network_techniques : ', specs_network_techniques)
        print('book_number : ', book_number)
        print('book_date : ', book_date)
        print('descriptions : ', descriptions)
        print('username : ', username)

        #ผลรวมว่าผ่านหรือไม่ : 1 คือผ่าน, 0 คือไม่ผ่าน
        if specs_general == '1' and specs_elec_general == '1' and specs_elec_techniques == '1' and specs_network_general == '1' and specs_network_techniques == '1':
            result_flag = '1'
        else:
            result_flag = '0'

        print('Result flag : ',result_flag)

        ##########################################################################################
        
        ########## Get Remark ของ Improve Specification ##########
        general_remark = ''
        elec_general_remark = ''
        elec_techniques_remark = ''
        network_general_remark = ''
        network_techniques_remark = ''

        if specs_general == '0':
            print('General Remark : ', request.POST['general_remark'])
            general_remark = request.POST['general_remark']
            
        if specs_elec_general == '0':
            print('Electric General Remark : ', request.POST['elec_general_remark'])
            elec_general_remark = request.POST['elec_general_remark']

        if specs_elec_techniques == '0':
            print('Electric Techniques Remark : ', request.POST['elec_techniques_remark'])
            elec_techniques_remark = request.POST['elec_techniques_remark']
            
        if specs_network_general == '0':
            print('Network General Remark : ', request.POST['network_general_remark'])
            network_general_remark = request.POST['network_general_remark']

        if specs_network_techniques == '0':
            print('Network Techniques Remark : ', request.POST['network_techniques_remark'])
            network_techniques_remark = request.POST['network_techniques_remark']
        ##########################################################

        # if len(number) == 0:
        #     messages.info(request,'Please input your number !')
        #     print(messages)
        #     return redirect('/formAddResult')
        # elif len(name) == 0:
        #     messages.info(request,'Please input your name !')
        #     return redirect('/formAddResult')
        # elif len(type_office) == 0:
        #     messages.info(request,'Please input your type office !')
        #     return redirect('/formAddResult')
        # elif len(book_number) == 0:
        #     messages.info(request,'Please input your book number !')
        #     return redirect('/formAddResult')
        # else:
        #     #uploaded_file=request.FILES['book_file']
        #     book_file = ''
        #     #SC000_20200428_1600 ตัวอย่างที่จะแก้รอบต่อไป 2020 04 28
        #     print('FILE CHECKING')
        #     file_data = request.FILES.get('files', None)
        #     if file_data:
        #         print('Found')
        #         uploaded_file=request.FILES['files']
        #         print(uploaded_file.name)
        #         #book_file='/BOOK_FILES/' + str(uploaded_file.name)
        #         temp = str(uploaded_file.name).split('.')
        #         rename = get_timestamp() + '.' + temp[1]
        #         book_file='/BOOK_FILES/' + rename

        #         fs=FileSystemStorage()
        #         #fs.save(uploaded_file.name, uploaded_file)
        #         fs.save(rename, uploaded_file)
        #     else:
        #         print('Not Found')
        #         messages.info(request,'Please input your book file !')
        #         return redirect('/formAddResult')


        ##########################################################################################
        #ลำดับสำนักงาน + ผลการตรวจ + ลำดับไฟล์ + เวลา : F1_1_1_20200515132421.jpg

        # files = request.FILES.getlist('files')
        # time_stamp = get_timestamp()
        # paths = []
        # sizes = []
        # if files:
        #     print('Found files')
        #     for count, x in enumerate(files):
        #         def handle_uploaded_file(f):
        #             print('Size : ', f.size)
        #             sizes.append(f.size)
        #             file_extension = str(f).split('.') #หานามสกุลไฟล์
        #             print('File extension : ', file_extension[1])
        #             path = 'BOOK_FILES/F_' + number + '_' + result_flag + '_' + str(count + 1) + '_' + time_stamp + '.' + file_extension[1]
        #             paths.append(path)
        #             print('Path : ', path)
        #             print('Lenght : ', len(paths))
        #             # with open(path, 'wb+') as destination:
        #             #     for chunk in f.chunks():
        #             #         destination.write(chunk)
        #         handle_uploaded_file(x)
        # else:
        #     print('Can\'t found files')
        #     messages.info(request,'Please input your book file !')
        #     return redirect('/formAddResult')


        #ลำดับสำนักงาน + ผลการตรวจ + ลำดับไฟล์ + เวลา : F1_1_1_20200515132421.jpg

        result_files = request.FILES.getlist('result_files')
        checklist_files = request.FILES.getlist('checklist_files')
        memo_files = request.FILES.getlist('memo_files')
        atp_files = request.FILES.getlist('atp_files')

        paths = []
        sizes = []
        files_name = []

        def handle_uploaded_file(f, name):
            print('Size : ', f.size)
            sizes.append(f.size)
            file_extension = str(f).split('.') #หานามสกุลไฟล์
            print('File extension : ', file_extension[1])
            path = 'BOOK_FILES/' + name + '_' + number + '_' + result_flag + '_' + str(count + 1) + '_' + time_stamp + '.' + file_extension[1]
            paths.append(path)
            print('Path : ', path)
            print('Lenght : ', len(paths))
            files_name.append(name)
            # with open(path, 'wb+') as destination:
            #     for chunk in f.chunks():
            #         destination.write(chunk)

        time_stamp = get_timestamp()
        if result_files:
            print('Found files')
            for count, x in enumerate(result_files):
                handle_uploaded_file(x, 'Result')
        if checklist_files:
            print('Found files')
            for count, x in enumerate(checklist_files):
                handle_uploaded_file(x, 'Checklist')
        if memo_files:
            print('Found files')
            for count, x in enumerate(memo_files):
                handle_uploaded_file(x, 'Memo')
        if atp_files:
            print('Found files')
            for count, x in enumerate(atp_files):
                handle_uploaded_file(x, 'ATP')
            
            print(files_name)
        else:
            print('Can\'t found files')
            messages.info(request,'Please input your book file !')
            return redirect('/formAddResult')
        ##########################################################################################
        
        #บันทึกลง Database
        Result.objects.create(
            number=number,
            name=name,
            types=type_office,
            result_flag=result_flag,
            book_number=book_number + ' ลงวันที่ ' + book_date,
            descriptions=descriptions,
            create_by=username,
            update_by=username,
            status_flag='1'
        )

        #Get FK
        ResultQuerys = Result.objects.filter(name__icontains=name)
        print('ResultQuery : ', ResultQuerys)
        for ResultQuery in ResultQuerys:
            print('UUID : ', ResultQuery.result_id)
            result_id = str(ResultQuery.result_id)

        for i in range(0,len(paths)):
            Files.objects.get_or_create(
                result_id=Result(result_id=result_id),
                path=paths[i],
                size=sizes[i],
                name=files_name[i]
            )

        ResultDetails.objects.get_or_create(
            result_id=Result(result_id=result_id),
            specifications='General',
            result_flag=specs_general,
            remark=general_remark
        )

        ResultDetails.objects.get_or_create(
            result_id=Result(result_id=result_id),
            specifications='Electical General',
            result_flag=specs_elec_general,
            remark=elec_general_remark
        )

        ResultDetails.objects.get_or_create(
            result_id=Result(result_id=result_id),
            specifications='Electical Techniques',
            result_flag=specs_elec_techniques,
            remark=elec_techniques_remark
        )

        ResultDetails.objects.get_or_create(
            result_id=Result(result_id=result_id),
            specifications='Network General',
            result_flag=specs_network_general,
            remark=network_general_remark
        )

        ResultDetails.objects.get_or_create(
            result_id=Result(result_id=result_id),
            specifications='Network Techniques',
            result_flag=specs_network_techniques,
            remark=network_techniques_remark
        )
    else:
        if request.user.is_authenticated:
            print('Login already')

            provinces = Office.objects.values('province').distinct().order_by('province')
            #offices = Office.objects.values('office_name').distinct().order_by('office_name')

            print('Province : ', provinces)

            offices = Office.objects.all().order_by('number')
            
            #for office in offices:
            #    print(office.province)

            return render(request,'formAddResult.html',{'provinces':provinces, 'offices' : offices})
        else:
            return redirect('/loginForm')

    # if request.user.is_authenticated:
    #     print('Login already')

    #     provinces = Office.objects.values('province').distinct().order_by('province')
    #     #offices = Office.objects.values('office_name').distinct().order_by('office_name')

    #     offices = Office.objects.all().order_by('number')
        
    #     #for office in offices:
    #     #    print(office.province)

    #     return render(request,'formAddResult.html',{'provinces':provinces, 'offices' : offices})
    # else:
    #     return redirect('/loginForm')

    return render(request,'formAddResult.html')

def getProvinceName(request):
    if request.method == 'GET':
        print('getProvinceName')
        province = request.GET['province_name']
        query_set_office_name = Office.objects.filter(province__icontains=province).order_by('name')

        office_name = serializers.serialize("json", query_set_office_name)
        return HttpResponse(office_name, content_type="application/json")

def getOfficeType(request):
    if request.method == 'GET':
        print('getOfficeType')
        name = request.GET['office_name']
        query_set_office_name = Office.objects.filter(name=name).order_by('name')

        office_name = serializers.serialize("json", query_set_office_name)
        return HttpResponse(office_name, content_type="application/json")

def addResult(request):

    print('addResult')

    if request.method == 'POST':
        def get_timestamp():
            time_zone = pytz.timezone("Asia/Bangkok")
            utc_dt = timezone.now()
            loc_dt = utc_dt.astimezone(time_zone)
            #format_time = '%Y-%m-%d %H:%M:%S %Z (%z)'
            format_time = '%Y%m%d%H%M%S'
            time_stamp = str(loc_dt.strftime(format_time))
            return time_stamp

        print('Time Stamp : ', get_timestamp())




        ##########################################################################################
        number = request.POST['number']
        name = request.POST['name']
        type_office = request.POST['type']
        specs_general = request.POST['specs_general']
        specs_elec_general = request.POST['specs_elec_general']
        specs_elec_techniques = request.POST['specs_elec_techniques']
        specs_network_general = request.POST['specs_network_general']
        specs_network_techniques = request.POST['specs_network_techniques']
        book_number = request.POST['book_number']
        descriptions = request.POST['descriptions']
        username = request.user

        print('number : ',number)
        print('name : ',name)
        print('Type : ',type_office)
        print('specs_general : ',specs_general)
        print('specs_elec_general : ',specs_elec_general)
        print('specs_elec_techniques : ',specs_elec_techniques)
        print('specs_network_general : ',specs_network_general)
        print('specs_network_techniques : ',specs_network_techniques)
        print('book_number : ',book_number)
        print('descriptions : ',descriptions)
        print('username : ',username)

        #ผลรวมว่าผ่านหรือไม่ : 1 คือผ่าน, 0 คือไม่ผ่าน
        if specs_general == '1' and specs_elec_general == '1' and specs_elec_techniques == '1' and specs_network_general == '1' and specs_network_techniques == '1':
            result_flag = '1'
        else:
            result_flag = '0'

        ##########################################################################################
        
        ########## Get Remark ของ Improve Specification ##########
        general_remark = ''
        elec_general_remark = ''
        elec_techniques_remark = ''
        network_general_remark = ''
        network_techniques_remark = ''

        if specs_general == '0':
            print('General Remark : ', request.POST['general_remark'])
            general_remark = request.POST['general_remark']
            
        if specs_elec_general == '0':
            print('Electric General Remark : ', request.POST['elec_general_remark'])
            elec_general_remark = request.POST['elec_general_remark']

        if specs_elec_techniques == '0':
            print('Electric Techniques Remark : ', request.POST['elec_techniques_remark'])
            elec_techniques_remark = request.POST['elec_techniques_remark']
            
        if specs_network_general == '0':
            print('Network General Remark : ', request.POST['network_general_remark'])
            network_general_remark = request.POST['network_general_remark']

        if specs_network_techniques == '0':
            print('Network Techniques Remark : ', request.POST['network_techniques_remark'])
            network_techniques_remark = request.POST['network_techniques_remark']
        ##########################################################

        # if len(number) == 0:
        #     messages.info(request,'Please input your number !')
        #     print(messages)
        #     return redirect('/formAddResult')
        # elif len(name) == 0:
        #     messages.info(request,'Please input your name !')
        #     return redirect('/formAddResult')
        # elif len(type_office) == 0:
        #     messages.info(request,'Please input your type office !')
        #     return redirect('/formAddResult')
        # elif len(book_number) == 0:
        #     messages.info(request,'Please input your book number !')
        #     return redirect('/formAddResult')
        # else:
        #     #uploaded_file=request.FILES['book_file']
        #     book_file = ''
        #     #SC000_20200428_1600 ตัวอย่างที่จะแก้รอบต่อไป 2020 04 28
        #     print('FILE CHECKING')
        #     file_data = request.FILES.get('files', None)
        #     if file_data:
        #         print('Found')
        #         uploaded_file=request.FILES['files']
        #         print(uploaded_file.name)
        #         #book_file='/BOOK_FILES/' + str(uploaded_file.name)
        #         temp = str(uploaded_file.name).split('.')
        #         rename = get_timestamp() + '.' + temp[1]
        #         book_file='/BOOK_FILES/' + rename

        #         fs=FileSystemStorage()
        #         #fs.save(uploaded_file.name, uploaded_file)
        #         fs.save(rename, uploaded_file)
        #     else:
        #         print('Not Found')
        #         messages.info(request,'Please input your book file !')
        #         return redirect('/formAddResult')


        ##########################################################################################
        #ลำดับสำนักงาน + ผลการตรวจ + ลำดับไฟล์ + เวลา : F1_1_1_20200515132421.jpg
        files = request.FILES.getlist('files')
        time_stamp = get_timestamp()
        paths = []
        sizes = []
        if files:
            print('Found files')
            for count, x in enumerate(files):
                def handle_uploaded_file(f):
                    print('Size : ', f.size)
                    sizes.append(f.size)
                    file_extension = str(f).split('.') #หานามสกุลไฟล์
                    print('File extension : ', file_extension[1])
                    path = 'BOOK_FILES/F_' + number + '_' + result_flag + '_' + str(count + 1) + '_' + time_stamp + '.' + file_extension[1]
                    paths.append(path)
                    print('Path : ', path)
                    print('Lenght : ', len(paths))
                    # with open(path, 'wb+') as destination:
                    #     for chunk in f.chunks():
                    #         destination.write(chunk)
                handle_uploaded_file(x)
                
        else:
            print('Can\'t found files')
            messages.info(request,'Please input your book file !')
            return redirect('/formAddResult')
        ##########################################################################################
        
        #บันทึกลง Database
        Result.objects.create(
            number=number,
            name=name,
            types=type_office,
            result_flag=result_flag,
            book_number=book_number,
            descriptions=descriptions,
            create_by=username,
            update_by=username,
            status_flag='1'
        )

        #Get FK
        ResultQuerys = Result.objects.filter(name__icontains=name)
        print('ResultQuery : ', ResultQuerys)
        for ResultQuery in ResultQuerys:
            print('UUID : ',ResultQuery.result_id)
            result_id=str(ResultQuery.result_id)

        for i in range(0,len(paths)):
            Files.objects.get_or_create(
                result_id=Result(result_id=result_id),
                path=paths[i],
                size=sizes[i]
            )

        ResultDetails.objects.get_or_create(
            result_id=Result(result_id=result_id),
            specifications='General',
            result_flag=specs_general,
            remark=general_remark
        )

        ResultDetails.objects.get_or_create(
            result_id=Result(result_id=result_id),
            specifications='Electical General',
            result_flag=specs_elec_general,
            remark=elec_general_remark
        )

        ResultDetails.objects.get_or_create(
            result_id=Result(result_id=result_id),
            specifications='Electical Techniques',
            result_flag=specs_elec_techniques,
            remark=elec_techniques_remark
        )

        ResultDetails.objects.get_or_create(
            result_id=Result(result_id=result_id),
            specifications='Network General',
            result_flag=specs_network_general,
            remark=network_general_remark
        )

        ResultDetails.objects.get_or_create(
            result_id=Result(result_id=result_id),
            specifications='Network Techniques',
            result_flag=specs_network_techniques,
            remark=network_techniques_remark
        )

    return redirect('/resultForm')

def result(request):
    #Query Data From Model
    #dataResult=Result.objects.all()

    #SQL = '''
    #    SELECT uuid, number, name, type_office, book_number, `descriptions`,
    #    SUM(IF(specifications='General',result_flag,0)) AS 'g',
    #    SUM(IF(specifications='Electical General',result_flag,0)) AS 'e_g',
    #    SUM(IF(specifications='Electical Techniques',result_flag,0)) AS 'e_t',
    #    SUM(IF(specifications='Network General',result_flag,0)) AS 'n_g',
    #    SUM(IF(specifications='Network Techniques',result_flag,0)) AS 'n_t'
    #    FROM blogs_result 
    #    '''

    # SQL = '''
    #     SELECT r.result_id, f.path, r.number, r.name, r.types, r.book_number, r.`descriptions` , r.result_flag,
    #         SUM(IF(specifications='General',rd.result_flag,0)) AS 'g',
    #         SUM(IF(specifications='Electical General',rd.result_flag,0)) AS 'e_g',
    #         SUM(IF(specifications='Electical Techniques',rd.result_flag,0)) AS 'e_t',
    #         SUM(IF(specifications='Network General',rd.result_flag,0)) AS 'n_g',
    #         SUM(IF(specifications='Network Techniques',rd.result_flag,0)) AS 'n_t'
    #         FROM blogs_result r
    #         INNER JOIN  blogs_resultdetails rd ON r.result_id = rd.result_id_id INNER JOIN blogs_files f ON r.result_id = f.result_id_id
    # '''

    SQL = '''
        SELECT r.result_id, r.number, r.name, r.types, r.book_number, r.`descriptions` , r.result_flag,
            SUM(IF(specifications='General',rd.result_flag,0)) AS 'g',
            SUM(IF(specifications='Electical General',rd.result_flag,0)) AS 'e_g',
            SUM(IF(specifications='Electical Techniques',rd.result_flag,0)) AS 'e_t',
            SUM(IF(specifications='Network General',rd.result_flag,0)) AS 'n_g',
            SUM(IF(specifications='Network Techniques',rd.result_flag,0)) AS 'n_t'
            FROM blogs_result r
            INNER JOIN  blogs_resultdetails rd ON r.result_id = rd.result_id_id
    '''

    
    query = request.GET.get ("search")
    #แก้เซิสหาหลาย ๆ คำ 
    #if query:
    #    print(query.replace(' ','%%'))
    #    query = query.replace(' ','%%')

    if query:
        SQL += '''
        WHERE number LIKE '%%'''+ query +'''%%'
        OR name LIKE '%%''' + query + '''%%'
        OR types LIKE '%%'''+ query +'''%%'
        OR book_number LIKE '%%''' + query + '''%%'
        OR `descriptions` LIKE '%%'''+ query +'''%%' 
        '''

    SQL += '''GROUP BY r.name
    ORDER BY CONVERT(r.number, INT) ASC
    '''

    print(SQL)

    #print(SQL)
    #for p in Result.objects.raw(SQL):
    #    print(p)
    dataResult = Result.objects.raw(SQL)

    #for re in dataResult:
    #    print(re.name)


    #กรณีที่ Objects.all
    '''
    query = request.GET.get("search")
    if query:
        ResultQuery=Result.objects.all()
        print(type(ResultQuery))
        ResultQuery = ResultQuery.filter(name__icontains=query)
        #for re in ResultQuery:
        #    print(re.name)
    '''
    
    return render(request,'formSummary.html',{'results':dataResult})

def createForm(request):
    return render(request,'form.html')

def addUser(request):
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    email=request.POST['email']
    username=request.POST['username']
    password=request.POST['password']
    confirmpassword=request.POST['confirmpassword']

    if password==confirmpassword:
        if User.objects.filter(username=username).exists():
            print("Username นี้มีคนใช้แล้ว")
            messages.info(request,'Username มีคนใช้แล้ว')
            return redirect('/createForm')
        elif User.objects.filter(email=email).exists():
            print("Email นี้มีคนใช้แล้ว")
            messages.info(request,'Email นี้มีคนใช้แล้ว')
            return redirect('/createForm')
        else:
            User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=firstname,
                last_name=lastname
            )
            # User.objects.save()
            return redirect('/')
    else:
        print("Password ไม่ตรงกัน")
        messages.info(request,'Password ไม่ตรงกัน')
        return redirect('/createForm')

# @login_required(redirect_field_name='my_redirect_field')
def loginForm(request):
    print('Request Path : ', request.path)
    if request.user.is_authenticated:
        redirect('/')
    return render(request,'login.html')

# @login_required(redirect_field_name='my_redirect_field')
def login(request):
    username=request.POST['username']
    password=request.POST['password']

    #check username, password
    user=auth.authenticate(username=username,password=password)
    if user is not None :
        print('Succecss')
        #loginPOST = request.POST
        #request.session['username'] = loginPOST['username']
        #print(request.session['username'])
        #print(request.session.get_expiry_date())
        auth.login(request,user)
        return redirect('/')

        # print('Request : %s'% request.get_full_path)
        # return redirect('/login/?next=%s' % request.path)

        #return render(request, '/',{'username':loginPOST['username']})
        #return render(request,'layout.html',{'username':loginPOST})
    else:
        messages.info(request,'ไม่พบข้อมูล')
        return redirect('/loginForm')

def logout(request):
    auth.logout(request)
    #request.session.flush()
    return redirect('/')

def upload(request):
    if request.method == 'POST':
        uploaded_file=request.FILES['document']
        #print(str(uploaded_file.name))
        #print(str(uploaded_file.size))
        fs=FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'upload.html')

def editResult(request):
    editName = request.GET.get("edit")
    if editName:
        print('viewEdit')
    return redirect('/resultForm')

def formEditResult(request):
    #print(request.GET.get('edit'))
    if request.GET.get('edit'):
        #print(request.GET.get('edit'))

        uuid = request.GET.get('edit')
        #ResultQuerys = Result.objects.filter(uuid=str(uuid))
        #ResultDetailsQuerys = ResultDetails.objects.filter(result_uuid_id=str(uuid))

        SQL = '''
            SELECT r.uuid, number, name, types, book_number, `descriptions` , 
            SUM(IF(specifications='General',rd.result_flag,0)) AS 'g', 
            SUM(IF(specifications='Electical General',rd.result_flag,0)) AS 'e_g', 
            SUM(IF(specifications='Electical Techniques',rd.result_flag,0)) AS 'e_t', 
            SUM(IF(specifications='Network General',rd.result_flag,0)) AS 'n_g', 
            SUM(IF(specifications='Network Techniques',rd.result_flag,0)) AS 'n_t'
            FROM blogs_result r 
            INNER JOIN  blogs_resultdetails rd ON r.uuid = rd.result_uuid_id
        '''
        SQL += "WHERE r.uuid = '"  + uuid.replace('-','') + "' "
        SQL += "GROUP BY name"

        print(SQL)

        ResultQuerys = Result.objects.raw(SQL)
        
        print(ResultQuerys)

        print(type(ResultQuerys))
        print(ResultQuerys)
        for ResultQuery in ResultQuerys:
            print('UUID : ',ResultQuery.result_id)
            print('name : ',ResultQuery.name)
            print('result : ', ResultQuery.result_flag)
            print('g :', int(ResultQuery.g))
            print('e_g :', ResultQuery.e_g)


    return render(request,'formEditResult.html',{'ResultQuerys':ResultQuerys})

def deleteResult(request):
    print('Delete Result')
    result_id = request.GET.get("delete")
    if result_id:
        ###################################################################################
        objFiles = Files.objects.values_list('path',flat = True).filter(result_id=result_id) 
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print('objFiles : ', objFiles)
        for files in objFiles:
            location_file = os.path.join(BASE_DIR.strip(),files.replace('/','\\').strip()) #.strip ลบช่องว่าง ' '
            if os.path.isfile(location_file):
                print('Remove file')
                os.remove(location_file)
                #os.remove(path.get['path'])
            else:
                print('Can\'t found file')
            print('File : ', files.replace('/','\\'))
            print('Join base_dir and file : ', location_file)
        
        Result.objects.filter(result_id=result_id).delete()
        Files.objects.filter(result_id=result_id).delete()
        ###################################################################################
    else:
        print('Can\'t found result_id')

    return redirect('/resultForm')

def likePost(request):
    print('On Function GET')
    if request.method == 'GET':
        print('GET')
        uuid = request.GET['post_id']
        uuid = uuid.replace("-","")
        
        tasks = Office.objects.filter(province__icontains=uuid)

        data = serializers.serialize("json", tasks)
        return HttpResponse(data, content_type="application/json")
        #return render(request, "formTest.html",{'provinces':provinces})
    else:
        print('Request Not a GET')  
        return HttpResponse("Request method is not a GET")


@login_required(login_url='/loginForm/')
def office(request):
    offices = Office.objects.all().order_by('number')
    return render(request, "office.html", {'offices' : offices})










#-------------------- ASSET --------------------
def formAddAsset(request):
    if request.method == 'POST':
        print('formAddAsset POST')
        start_date = request.POST['start_date'] # YYYY-MM-DD
        expire_date = request.POST['expire_date'] # YYYY-MM-DD
        
        return render(request,'formAddAsset.html')
    elif request.method == 'GET' and 'type' in request.GET:
        print('TYPE')
        types = request.GET['type']
        print(types)

        brand = Assettype.objects.filter(name__icontains=types , status_flag='1').distinct()
        brand = serializers.serialize("json", brand)
        
        return HttpResponse(brand, content_type="application/json")
    elif request.method == 'GET' and 'brand' in request.GET:
        print('MODEL')
        brand = request.GET['brand']
        print(brand)
        model = Assettype.objects.filter(brand__icontains=brand, status_flag='1').distinct()
        model = serializers.serialize("json", model)

        return HttpResponse(model, content_type="application/json")
    else:
        if request.user.is_authenticated:
            print('formAddAsset NO')
            asset_types = Assettype.objects.values('name').distinct()
            locations = Location.objects.all()
            print(asset_types)

            return render(request,'formAddAsset.html',{'asset_types' : asset_types, 'locations' : locations})
        else:
            return render(request,'login.html',{'old_path':'formAddAsset'})

    return render(request,'formAddAsset.html')

def formAddLocation(request):
    if request.POST:
        name = request.POST['location_name']
        position = request.POST['position']
        user_id=request.user
        print('formAddLocation POST')
        print(name)
        print(position)

        Location.objects.create(
            name=name,
            position=position,
            update_by=user_id
        )

        return render(request,'formAddLocation.html')
    else:
        print('formAddLocation NO')
        if request.user.is_authenticated:
            pass
            return render(request,'formAddLocation.html')
        else:
            return redirect('/loginForm')
        return render(request,'formAddLocation.html')

    return render(request,'formAddLocation.html')


def formAddAssetType(request):
    if request.POST:
        types = request.POST['type']
        brand = request.POST['brand']
        model = request.POST['model']
        price = request.POST['price']
        status_flag = request.POST['status_flag']
        user_id=request.user
        print('formAddAssetType POST')
        Assettype.objects.create(
            name=types,
            brand=brand,
            model=model,
            price=price,
            status_flag=status_flag,
            update_by=user_id,
        )
        return render(request,'formAddAssetType.html')
    else:
        print('formAddAssetType NO')
        
        if request.user.is_authenticated:
            pass
            return render(request,'formAddAssetType.html')
        else:
            return redirect('/loginForm')
            
    return render(request,'formAddAssetType.html')
#-----------------------------------------------


#-------------------- SUMMARY --------------------
def getFiles(request):
    if request.method == 'GET':
        print('getFiles')
        result_id = request.GET['result_id'].replace('-','')
        print('result_id : ',result_id)
        query_set = Files.objects.filter(result_id=result_id).order_by('path')

        print('Query Set : ', query_set)

        files = serializers.serialize("json", query_set)
        print('files :', files)
        return HttpResponse(files, content_type="application/json")

def getResult(request):
    if request.method == 'GET':
        print('getResult')
        result_id = request.GET['result_id'].replace('-','')
        print('result_id : ',result_id)
        query_set = ResultDetails.objects.filter(result_id=result_id)

        print('Query Set : ', query_set)        

        result = serializers.serialize("json", query_set)
        print('Result :', result)
        return HttpResponse(result, content_type="application/json")
#-------------------------------------------------

#-------------------- Check List --------------------

def formAddCheckList(request):
    return render(request,'formAddCheckList.html')


def formCheckList(request):
    return render(request,'formCheckList.html')

#----------------------------------------------------


def CSVFiles(request):
    # csv_file = request.FILES['file']

    csv_file = request.FILES.get('file', None)

    if csv_file:
        print('CSV : ', csv_file)
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'This is not a CSV file')
        else:
            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)
            for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                print('ลำดับ : ',column[0])
                print('ชื่อ : ', column[1])
                print('ทั่วไป : ',column[2])
                print('ไฟฟ้า ทั่วไป :' ,column[3])
                print('ไฟฟ้า เทคนิค : ',column[4])
                print('สัญญาณ ทั่วไป : ',column[5])
                print('สัญญาณ เทคนิค : ',column[6])
                print('เลขหนังสือ : ',column[7])
                print('หมายเหตุ : ',column[8])

                user_id=request.user

                number=column[0]
                name=column[1]
                specs_general=column[2]
                specs_elec_general=column[3]
                specs_elec_techniques=column[4]
                specs_network_general=column[5]
                specs_network_techniques=column[6]
                book_number=column[7]
                remark=column[8]

                result_flag = '0'
                #ผลรวมว่าผ่านหรือไม่ : 1 คือผ่าน, 0 คือไม่ผ่าน
                if specs_general == '1' and specs_elec_general == '1' and specs_elec_techniques == '1' and specs_network_general == '1' and specs_network_techniques == '1':
                    result_flag = '1'
                else:
                    result_flag = '0'

                ##### GET Office Type #####
                OfficeQuerys = Office.objects.filter(name__icontains=name)
                for OfficeQuery in OfficeQuerys:
                    print('Type : ', OfficeQuery.types)
                    type_office = str(OfficeQuery.types)
                ###########################

                Result.objects.create(
                    number=number,
                    name=name,
                    types=type_office,
                    book_number=book_number,
                    result_flag=result_flag,
                    descriptions=remark,
                    create_by=user_id,
                    update_by=user_id,
                    status_flag=1,
                )

                ##### GET Result ID #####
                ResultQuerys = Result.objects.filter(name__icontains=name)
                for ResultQuery in ResultQuerys:
                    print('Type : ', ResultQuery.result_id)
                    result_id = str(ResultQuery.result_id)
                ###########################

                ResultDetails.objects.get_or_create(
                    result_id=Result(result_id=result_id),
                    specifications='General',
                    result_flag=specs_general,
                    remark=remark
                )

                ResultDetails.objects.get_or_create(
                    result_id=Result(result_id=result_id),
                    specifications='Electical General',
                    result_flag=specs_elec_general,
                    remark=remark
                )

                ResultDetails.objects.get_or_create(
                    result_id=Result(result_id=result_id),
                    specifications='Electical Techniques',
                    result_flag=specs_elec_techniques,
                    remark=remark
                )

                ResultDetails.objects.get_or_create(
                    result_id=Result(result_id=result_id),
                    specifications='Network General',
                    result_flag=specs_network_general,
                    remark=remark
                )

                ResultDetails.objects.get_or_create(
                    result_id=Result(result_id=result_id),
                    specifications='Network Techniques',
                    result_flag=specs_network_techniques,
                    remark=remark
                )
    else:
        messages.error(request, 'Not found CSV file')

    return redirect('/')


def profile_upload(request):
    # declaring template
    template = "profile_upload.html"
    data = Profile.objects.all()
    # prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be name, email, address,    phone, profile',
        'profiles': data    
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Profile.objects.update_or_create(
            name=column[0],
            email=column[1],
            address=column[2],
            phone=column[3],
            profile=column[4]
        )
    context = {}
    return render(request, template, context)