'''
BootStrapFormMixin is created so it can be
inherited by their forms and their widgets
attr get the same bootstrap class 'form-control'.
'''


class BootStrapFormViewMixin:
    def get_form(self, **kwargs):
        form = super().get_form(**kwargs)
        self.__apply_bootstrap_classes(form)
        return form

    @staticmethod
    def __apply_bootstrap_classes(form):
        for (_, field) in form.fields.items():
            if 'attrs' not in field.widget:
                field.widget.attrs = {}
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''

            field.widget.attrs['class'] += 'form-control'


class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_fields()

    def _init_bootstrap_fields(self):
        for (_, field) in self.fields.items():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += 'form-control'
