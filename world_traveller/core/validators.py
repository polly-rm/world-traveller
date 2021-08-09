from django.core.exceptions import ValidationError

'''
Custom validator is created.
'''


def validate_text_starts_with_capital(text):
    first_letter = text[0]
    if first_letter.islower():
        raise ValidationError('This field must start with a capital letter!')