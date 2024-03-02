from django import forms
from .models import Booking




class DataInput(forms.DateInput):
    input_type = "date"
class BookingForms(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'booking_date' : DataInput()
        }
        labels = {
            'p_name': "Paitent Name",
            'p_phone' : 'Paitent Phone',
            'p_email':'Paintent Email',
            'doc_name':'Doctor Name',
            'booking_date':"Booking Date",
            'booked_on ':'Booked On',
        }
        
    
        