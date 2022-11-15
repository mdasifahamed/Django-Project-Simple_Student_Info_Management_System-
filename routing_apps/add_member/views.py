from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from add_member.models import Students
import datetime


@csrf_exempt
def add(request):
    if request.method == 'POST':
        template2 = loader.get_template(
            'success.html')  # template for suucessfuly adding means no duplicate dat is found
        template3 = loader.get_template(
            'Duplicate_check.html')  # template for display data if any duplicata is found during inserting
        name = request.POST['name']
        b_date = (request.POST['birthdate'])
        reg = int(request.POST['reg_no'])
        dept = request.POST['department']
        session = request.POST['session']
        check = Students.objects.values_list('reg_no')  # fetching all the registartion number from qureyset for data calidation i.e
        '''
        check will be like this  [(1111111,),(222222,),(3333333,),(4444444,),.......]
        That's Why Last 3 Line of Code in Needed
        '''
        list_reg = []  # This list is stong data from avove chek list as qureyset list contains reg_no as list of and a tuplle cannot be iterated so this list will be used for storing reg number
        for item in check:  # looping thron list of tupple gotten from Queryset
            list_reg.append(item[0])  # Adding the registartion numbers to the list from the tupple inside from list and it is in first index so it will be
        # Validation And Decision Making
        if reg in list_reg:  # checking for any duplicate is found or not if as per unique value registartion number

            duplicate = Students.objects.filter(reg_no=reg).values()#Getting Data According to Registartion Number For Display
            contex = {
                # A dictinary which will pass as paramete in the render function and its key can used in zinga inside html code for making html dynamic
                'Data': duplicate,
                'reg': reg,
            }
            return HttpResponse(template3.render(contex, request))
        # iF No Duplicate Is Then  Data Will Be Stoder to Database And it will Be Open Success Page
        else:
            student = Students(name=name, b_date=b_date, reg_no=reg, department=dept, session=session)
            student.save()
            contex2 = {
                'name': name,
            }
            return HttpResponse(template2.render(contex2, request))
    else:
        template = loader.get_template('input.html')
        return HttpResponse(template.render())


@csrf_exempt
def to_home(request):
    return redirect('/')


@csrf_exempt
def to_update(request):
    return redirect('update_student:update')


@csrf_exempt
def to_delete(request):
    return redirect('delete_student:delete')


@csrf_exempt
def to_search(request):
    return redirect('search_student:search')
