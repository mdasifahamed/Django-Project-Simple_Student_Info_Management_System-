from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from add_member.models import Students

@csrf_exempt
def search(request):
    if request.method == 'POST':
        reg = int(request.POST['reg_no'])
        list_of_tuple_of_reg = Students.objects.values_list('reg_no')
        list_of_reg = []
        for items in list_of_tuple_of_reg:
            list_of_reg.append(items[0])

        if reg in list_of_reg:
            data_of_reg = Students.objects.filter(reg_no=reg).values()
            contex1 ={
                'data': data_of_reg,
                'reg': reg
            }
            display_template = loader.get_template('display_info.html')
            return HttpResponse(display_template.render(contex1, request))

        else:
            context2 = {
                'reg':reg,
            }
            data_not_found = loader.get_template('data_not_found_update.html')
            return HttpResponse(data_not_found.render(context2))
    else:
        template = loader.get_template('search_info.html')
        return HttpResponse(template.render())


@csrf_exempt
def to_add(request):
    return redirect('add_member:add')

@csrf_exempt
def to_update(request):
    return redirect('update_student:update')

@csrf_exempt
def to_delete(request):
    return redirect('delete_student:delete')

@csrf_exempt
def to_home(request):
    return redirect('/')



