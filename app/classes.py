import app.test.classesfortests as classesfortests
from wtforms import ValidationError
import datetime
import re

class Email:
    """
    Validates an email address. Requires email_validator package to be
    installed. For ex: pip install wtforms[email].

    :param message:
        Error message to raise in case of a validation error.
    :param granular_message:
        Use validation failed message from email_validator library
        (Default False).
    :param check_deliverability:
        Perform domain name resolution check (Default False).
    :param allow_smtputf8:
        Fail validation for addresses that would require SMTPUTF8
        (Default True).
    :param allow_empty_local:
        Allow an empty local part (i.e. @example.com), e.g. for validating
        Postfix aliases (Default False).
    """

    def __init__(
        self,
        message=None,
        granular_message=False,
        check_deliverability=False,
        allow_smtputf8=True,
        allow_empty_local=False,
    ):
        if classesfortests is None:  # pragma: no cover
            raise Exception("Install 'email_validator' for email validation support.")
        self.message = message
        self.granular_message = granular_message
        self.check_deliverability = check_deliverability
        self.allow_smtputf8 = allow_smtputf8
        self.allow_empty_local = allow_empty_local

    def __call__(self, form, field):
        try:
            if field.data is None:
                raise classesfortests.EmailNotValidError()
            classesfortests.validate_email(self,field.data)
        except classesfortests.EmailNotValidError as e:
            message = self.message
            if message is None:
                if self.granular_message:
                    message = field.gettext(e)
                else:
                    message = field.gettext("Invalid email address.")
            raise ValidationError(message) from e


class Date_Time:
    def validate_date(self, field):
        if field.data < datetime.datetime.today():
            raise ValidationError("The date cannot be in the past!")

class Name_Validation:
    def validate_name(self,field):
        if not re.match(r'^[a-zA-Z-\s]+$', field.data):
            raise ValidationError("Only have alphabets or dash in name field are allowed")