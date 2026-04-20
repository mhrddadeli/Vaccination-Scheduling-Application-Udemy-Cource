from django.forms import ModelForm
from center.models import Center


class CenterForm(ModelForm):
    class Meta:
        model = Center
        fields = "__all__"

    def __int__(self, *args, **kwargs):
        super(CenterForm, self).__int__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"


