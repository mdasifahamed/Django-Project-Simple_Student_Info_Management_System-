from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from add_member.models import Students

@csrf_exempt
def update(request):

    if request.method == 'POST':
        reg = int(request.POST['reg_no'])
        list_of_tuple_of_all_reg = Students.objects.values_list('reg_no')
        list_of_all_reg =[]
        for item in list_of_tuple_of_all_reg:
            list_of_all_reg.append(item[0])

        if reg in list_of_all_reg:

            data_to_display = Students.objects.filter(reg_no = reg)
            context1 = {
                'data':data_to_display,
                'reg': reg
            }
            update_inside_form_template = loader.get_template('update_fields.html')

            return HttpResponse(update_inside_form_template.render(context1,request))
        else:
            data_not_found_template = loader.get_template('data_not_found_update.html')
            context2 = {
                'reg':reg,
            }
            return HttpResponse(data_not_found_template.render(context2, request))


    else:

        template = loader.get_template('update.html')
        return HttpResponse(template.render())

@csrf_exempt
def update_record(request):
    if request.method == 'POST':
        name = request.POST['name']
        b_date = request.POST['birthdate']
        reg = int(request.POST['reg_no'])
        department = request.POST['department']
        session = request.POST['session']
        student = Students.objects.get(reg_no=reg)
        student.name = name
        student.b_date = b_date
        student.reg_no = reg
        student.department = department
        student.session = session
        student.save()
        contex1 = {
            'data': student,
            'reg':reg,
        }

        after_update_template = loader.get_template('After_update.html')

        return HttpResponse(after_update_template.render(contex1))

    else:
        pass

@csrf_exempt
def to_home(request):
    return redirect('/')

@csrf_exempt
def to_add(request):
    return redirect('add_member:add')

@csrf_exempt
def to_search(request):
    return redirect('search_student:search')

@csrf_exempt
def to_delete(request):
    return redirect('delete_student:delete')





