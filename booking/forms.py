from django import forms
from django.core.exceptions import ValidationError
import datetime
from .models import Booking


# Creates date imput for initial booking
class StartDateInput(forms.DateInput):
    input_type = 'date'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs.setdefault('min', datetime.date.today() + datetime.timedelta(days=1))


class EndDateInput(forms.DateInput):
    input_type = 'date'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs.setdefault('min', datetime.date.today() + datetime.timedelta(days=2))


# Form for initial booking
class BookingForm(forms.Form):
    start_date = forms.DateField(widget=StartDateInput)
    end_date = forms.DateField(widget=EndDateInput)
    amount_adults = forms.IntegerField(min_value=1, max_value=3, initial=1)
    amount_kids = forms.IntegerField(required=False, min_value=0, max_value=3)
    
    # Prevents user from sending in wrong date order
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if end_date <= start_date:
            raise ValidationError("The end date has to be later than the start date")

        return cleaned_data


READ_ONLY_FIELD = {'readonly': True, 'class': 'form-control'}


# Step two of booking form, where input is only first+last name
class ConfirmBookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('start_date', 'end_date', 'amount_adults', 'amount_kids', 'first_name', 'last_name', 'total_price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['start_date'].widget.attrs.update(READ_ONLY_FIELD)
        self.fields['end_date'].widget.attrs.update(READ_ONLY_FIELD)
        self.fields['amount_adults'].widget.attrs.update(READ_ONLY_FIELD)
        self.fields['amount_kids'].widget.attrs.update(READ_ONLY_FIELD)
        self.fields['first_name'].widget.attrs.update({'placeholder': 'First name*', 'class': 'form-control col-xs-3'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Last name*', 'class': 'form-control col-xs-3'})
        self.fields['total_price'].widget.attrs.update(READ_ONLY_FIELD)


# Form for edit reservation
class EditBookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('start_date', 'end_date', 'amount_adults', 'amount_kids', 'first_name', 'last_name')
        widgets = {
            'start_date': forms.DateInput(attrs={
                'min': datetime.date.today() + datetime.timedelta(days=1),
                'type': 'date'
            }),
            'end_date': forms.DateInput(attrs={
                'min': datetime.date.today() + datetime.timedelta(days=2),
                'type': 'date'
            }),
            'amount_adults': forms.NumberInput(attrs={
                'min': 1,
                'max': 3
            }),
            'amount_kids': forms.NumberInput(attrs={
                'min': 0,
                'max': 3,
                'required': False
            })

        }
