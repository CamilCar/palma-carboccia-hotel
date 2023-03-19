from django import forms
import datetime


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


class BookingForm(forms.Form):
    start_date = forms.DateField(widget=StartDateInput)
    end_date = forms.DateField(widget=EndDateInput)
    amount_adults = forms.IntegerField(min_value=1, initial=1)
    amount_kids = forms.IntegerField(required=False)


class ConfirmBookingForm(BookingForm):
    total_price = forms.IntegerField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    special_request = forms.Textarea()
