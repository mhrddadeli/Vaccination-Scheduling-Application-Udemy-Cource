from django.forms import ModelForm
from center.models import Center, Storage


class CenterForm(ModelForm):
    class Meta:
        model = Center
        fields = "__all__"

    def __int__(self, *args, **kwargs):
        super(CenterForm, self).__int__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"


class StorageForm(ModelForm):
    def __int__(self, *args, **kwargs):
        super(StorageForm, self).__int__(*args, **kwargs)

        # following block is not working, no internet in iran, so I can't search why!!!
        self.fields["center"].queryset = Center.objects.filter(id=self.kwargs["center_id"])
        self.fields["center"].disabled = True
        self.fields["booked_quantity"].disabled = True

        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Storage
        fields = "__all__"






