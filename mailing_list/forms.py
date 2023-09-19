from django.forms import ModelForm

from mailing_list.models import MailingListSettings, Message


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = "form-control"


class MailingListSettingsForm(StyleFormMixin, ModelForm):

    class Meta:
        model = MailingListSettings
        fields = ('start_time', 'end_time', 'periodicity', 'status', 'clients', )


class MessageForm(StyleFormMixin, ModelForm):

    class Meta:
        model = Message
        fields = ('subject', 'text', 'status', )
