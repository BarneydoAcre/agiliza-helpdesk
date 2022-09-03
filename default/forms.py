from django import forms

from . import models


class AddBugReportForm(forms.ModelForm):
    class Meta:
        model = models.BugReport
        fields = [
            'company',
            'company_worker',
            'bug',
        ]
        exclude = []