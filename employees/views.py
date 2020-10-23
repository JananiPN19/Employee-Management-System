from django.shortcuts import render,redirect
from django.http import Http404

from .models import Employee,AvailableJob
from .forms import LoginForm,RegisterForm

# Create your views here.

def login(request):
    global emp
    if request.method == 'POST':
        l_form = LoginForm(request.POST or None)
        form = LoginForm()
        if l_form.is_valid():
            email,dob,role = l_form.cleaned_data.get('email_id'),l_form.cleaned_data.get('dob'),l_form.cleaned_data.get('job')
            try:
                emp = Employee.objects.get(email_id = email)
                job_list = list(AvailableJob.objects.values_list('job_name',flat=True))
                job_r = emp.job.all().values()[0]['id']
                job_role = job_list[(job_r)-1]
                #print(role.values()[0]['job_name'])
                if not (dob == emp.dob and role.values()[0]['job_name'] == job_role):
                    context={
                        'form':form,
                        'error': 'Invalid Credentials. Please check your credentials and re-enter it.',
                    }
                    return render(request,'login.html',context)
                if job_role == 'HR': 
                    return redirect('/hr_admin/')
                else: 
                    return redirect('/employee/{}'.format(emp.email_id))
            except Employee.DoesNotExist:
                raise Http404('Employee not found! Please re-enter the credentials.')
        else:
            #raise Http404('Employee not found! Please re-enter the credentials.')
            context = {
                'form': form,
                'error': 'Please enter valid details.',
            }
            return render(request,'login.html',context)
    else:
        l_form = LoginForm()
        context = {
            'form': l_form,
        }
    return render(request,'login.html',{'form' : l_form})


#Code for admin people starts
def admin(request):
    employees = Employee.objects.all()
    job_list = list(AvailableJob.objects.values_list('job_name',flat=True))
    dict_list = {('Content Writer','Inside Sales Representative','Technical Support Engineer'):20000,
                 ('Web Designer','Front end developer','Back end developer'):25000,
                 ('Full Stack developer','Web Developer'):30000,
                 ('Data Analyst','Software Engineer','Software Engineer in Test'):35000,
                 ('Data Engineer','Database Administrator'):40000,
                 ('Data Scientist','Program Manager','HR'):45000,
                 ('General Manager'):50000
                }
    #emp = Employee()
    for employee in employees:
        job_r = employee.job.all().values()[0]['id']
        job_role = job_list[(job_r)-1]
        for job in dict_list:
            if job_role in job:
                employee.basic_pay = dict_list[job]
                employee.save()
                break
    return render(request,'admin.html',{'employees':employees})

def delete(request,email):
    try:
        employee = Employee.objects.get(email_id=email)
        employee.delete()
    except Employee.DoesNotExist:
        raise Http404('Employee not found!')
    return redirect('/hr_admin/')

def create(request):
    emp = Employee()
    if request.method == 'POST':
        r_form = RegisterForm(request.POST or None)
        if r_form.is_valid():
            emp.first_name = r_form.cleaned_data.get('first_name')
            emp.last_name = r_form.cleaned_data.get('last_name')
            emp.email_id = r_form.cleaned_data.get('email_id')
            emp.phone_num = r_form.cleaned_data.get('phone_num')
            emp.gender = r_form.cleaned_data.get('gender')
            emp.address = r_form.cleaned_data.get('address')
            emp.dob = r_form.cleaned_data.get('dob')
            emp.basic_pay = r_form.cleaned_data.get('basic_pay')
            emp.net_salary = r_form.cleaned_data.get('net_salary')
            emp.save()   
            inst = Employee.objects.get(email_id=r_form.cleaned_data.get('email_id'))
            inst.job.set(r_form.cleaned_data.get('job'))
            inst.save()  
            return redirect('/hr_admin/')
        else:
            raise Http404('Please enter valid details.')   
    else:
        r_form = RegisterForm()
        context = {
            'form': r_form,
        }
    return render(request,'reg.html',context)
    
#Code for admin people ends

#Code for Employee people starts
def employee(request,email):
    try:
        empl = Employee.objects.get(email_id=email)
        context={
        'name':emp.first_name,
        'employee':empl,
        }
        return render(request,'employee.html',context)
    except Employee.DoesNotExist:
        raise Http404('Employee not found!')

def edit(request,email):
    try:
        emp = Employee.objects.get(email_id=email)
        if request.method == 'POST':
            form = RegisterForm(request.POST or None, instance=emp)
            if form.is_valid():
                emp.first_name = form.cleaned_data.get('first_name')
                emp.last_name = form.cleaned_data.get('last_name')
                emp.email_id = form.cleaned_data.get('email_id')
                emp.phone_num = form.cleaned_data.get('phone_num')
                emp.gender = form.cleaned_data.get('gender')
                emp.address = form.cleaned_data.get('address')
                emp.dob = form.cleaned_data.get('dob')
                emp.basic_pay = form.cleaned_data.get('basic_pay')
                emp.net_salary = form.cleaned_data.get('net_salary')  
                emp.job.set(form.cleaned_data.get('job'))
                emp.save()  
                context={
                    'form':form,
                    'success':'Information updated successfully.',
                }
            else:
                context = {
                    'form' : form,
                    'error' : "Please enter valid credentials."
                }
            return render(request,'update.html',context)
        else:
            form = RegisterForm(instance=emp)
            return render(request,'update.html',{'form':form})
    except Employee.DoesNotExist:
        raise Http404('Employee Not Found!')

#Code for Employee people ends


def employee_detail(request,email):
    try:
        employee = Employee.objects.get(email_id=email)
    except Employee.DoesNotExist:
        raise Http404('Employee not found!')
    return render(request, 'emp_detail.html',{'employee':employee})