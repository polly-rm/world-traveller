from unittest import TestCase

from django.core.exceptions import ValidationError

from world_traveller.core.validators import validate_text_starts_with_capital


class ValidatorsTests(TestCase):
    def test_validateTextStartsWithCapitalLetter__whenStartsWithCapital_expectToDoNothing(self):
        validate_text_starts_with_capital('Test')
        self.assertTrue(True)

    def test_validateTextStartsWithCapitalLetter__whenNotStartsWithCapital_expectToRaise(self):
        with self.assertRaises(ValidationError) as ex:
            validate_text_starts_with_capital('test')

        self.assertIsNotNone(ex.exception)
