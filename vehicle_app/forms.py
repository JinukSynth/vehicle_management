from django import forms
from .models import Vehicle

# Vehicle_Search_Form
class VehicleSearchForm(forms.ModelForm):
    license_number = forms.CharField(max_length=20, required=False, label='차량번호') # input field of vehicle number
    search_date = forms.DateField(required=False, label='출고일자(연도)', input_formats=['%Y-%m-%d']) # input field of vehicle model year


# Vehicle_Add_Form
class VehicleAddForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__' # All Model Database Data

class VehicleDeleteForm(forms.ModelForm):
    vehicle_ids = forms.CharField(widget=forms.HiddenInput(), required=False) # this ids_variable for vehicle Delete

class VehicleUpdateForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
