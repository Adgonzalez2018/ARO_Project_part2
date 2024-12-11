# your_app/validators.py

import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class CustomPasswordValidator:
    """
    Validates whether the password meets complexity requirements:
    - Minimum length of 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character
    """

    def validate(self, password, user=None):
        errors = []

        if len(password) < 8:
            errors.append(_('Password must be at least 8 characters long.'))

        if not re.search(r'[A-Z]', password):
            errors.append(_('Password must contain at least one uppercase letter.'))

        if not re.search(r'[a-z]', password):
            errors.append(_('Password must contain at least one lowercase letter.'))

        if not re.search(r'\d', password):
            errors.append(_('Password must contain at least one digit.'))

        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            errors.append(_('Password must contain at least one special character (!@#$%^&*(),.?":{}|<>).'))

        if errors:
            raise ValidationError(errors)

    def get_help_text(self):
        return _(
            "Your password must contain at least 8 characters, including one uppercase letter, "
            "one lowercase letter, one digit, and one special character (!@#$%^&*(),.?\":{}|<>)."
        )