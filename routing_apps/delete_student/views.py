from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from add_member.models import Students

@csrf_exempt
def delete(request):
    if request.method == 'POST':
        reg = int(request.POST['inputted_reg_no'])
        list_of_tuple_all_reg_no = Students.objects.values_list('reg_no')
        list_for_store_only_reg_from_tuple = []
        for item in list_of_tuple_all_reg_no:
            list_for_store_only_reg_from_tuple.append(item[0])

        if reg in list_for_store_only_reg_from_tuple:
            data_for_reg = Students.objects.filter(reg_no=reg).values()
            context1 ={
                'data': data_for_reg,
                'reg':reg,
            }
            template_fdtd = loader.get_template('found_data_to_delete.html')
            return HttpResponse(template_fdtd.render(context1, request))
        else:
            template_data_not_found = loader.get_template('data_not_found_delete.html')
            context3 = {
                'reg': reg
            }
            return HttpResponse(template_data_not_found.render(context3, request))

    else:
        template = loader.get_template('delete.html')
        return HttpResponse(template.render())

@csrf_exempt
def delete_record(request):
    reg = int(request.POST.get('reg_no'))
    print(reg)
    student = Students.objects.get(reg_no=reg)
    student.delete()
    after_delete_template = loader.get_template("successfully_deleted.html")
    return HttpResponse(after_delete_template.render())

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
def to_update(request):

    return redirect('update_student:update')





