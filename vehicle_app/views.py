# import
from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse

from vehicle_app.models import Vehicle

from .forms import VehicleSearchForm
from .forms import VehicleAddForm
from .forms import VehicleDeleteForm
#from .forms import VehicleUpdateForm

# MainPage_vehicle.html(urls.py : local/vehicles/)
def Vehicle_Management(request): # All data get from models.py 
    vehicles = Vehicle.objects.all()
    return render(request, 'MainPage_vehicle.html', {'vehicles':vehicles}) # form rendering


# Vehicle MainPage Header

# vehicle search
def search_vehicle(request):
    # POST: data response through input form from user
    if request.method == 'POST':
        form = VehicleSearchForm(request.POST)
        if form.is_valid():
            license_number = form.cleaned_data.get('license_number', '')
            vehicles = Vehicle.object.filter(license_number__icontains=license_number)
            
            return render(request, 'vehicles/MainPage_vehicle.html', {'vehicles':vehicles, 'form':form})
    else: # Get: frist Request
        form = VehicleSearchForm()
    return render(request, 'vehicles/MainPage_vehicle.html', {'form' : form}) # form rendering

# vehicle search by date
def search_vehicle_by_date(request):
    if request.method == 'POST':
        form = VehicleSearchForm(request.POST)
        if form.is_valid(): # if form data is true
            search_date = request.POST.get('search_date', '')
            vehicles = Vehicle.objects.filter(model_year = search_date)

            return render(request, 'MainPage_vehicle.html', {'vehicles' : vehicles, 'form' : form})
    else: # Get: First Request
        form = VehicleSearchForm()
    
    return render(request, 'MainPage_vehicle.html', {'form' : form, 'test': test}) # form rendering

# Header view done


# MainContaioner

# MainContaioner -> header(CRUD)

# add vehicle information - popup screen
def vehicle_add(request):
    if request.method =='POST': # if request method is POST(user click the add vehicle button)
        form = VehicleAddForm(request.POST, request.FILES) #make form from transfered data
        if form.is_valid(): # if form data is true
            form.save() # form data save in DB
            return JsonResponse({'message' : 'Vehicle added succesfully'}, status=200) # succesful message
        else:
            return JsonResponse({'error': form.error}, status=400) # failure error message
    else: # Get: First Request
        form = VehicleAddForm() 
    
    return render(request, 'MainPage_vehicle.html', {'form':form}) # form rendering # form 옆에 html에서 폼 불러서 쓸 코드 추가 '테스트': test

# Get 요청 post.get -> form 굳이
# delete vehicle information - MainConationer Header
def vehicle_delete(request):
    if request.method == 'POST':
        form = VehicleDeleteForm(request.POST.get)
        if form.is_valid():
            vehicle_ids = form.cleaned_data['vehicle_ids'].split(',')
            Vehicle.objects.filter(id__in = vehicle_ids).delete()
            return JsonResponse({'meessage' : 'Vehicle delete successfully'}, status=200)
        else:
            return JsonResponse({'error': form.error}, status = 400)
    else:
        form = VehicleDeleteForm() # Get: First Request
    return render(request, 'MainPage_vehicle.html', {'form': form})


# # Vehicle Detail Information Update
# def vehicle_update(request):
#     if request.method == 'POST':
#         form = VehicleUpdateForm(request.POST)
#         if form.is_vaild():
#             form.save()
#             return JsonResponse({'message': 'Vehicle Updeate successfully'}, status = 200)
#         else: 
#             return JsonResponse({'error': form.error}, status = 400) # failure error message
#     else: # Get request
#         form = VehicleUpdateForm()
#     return render(request,'MainPage_vehicle.html', {'form':form}) # form rendering
