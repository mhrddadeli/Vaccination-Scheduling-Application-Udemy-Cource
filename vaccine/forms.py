from django.forms import ModelForm
from vaccine.models import Vaccine


class VaccineForm(ModelForm):
    class Meta:
        model = Vaccine
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(VaccineForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
