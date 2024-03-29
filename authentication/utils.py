from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six


class tokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):
        return (six.text_type(user.is_active) + six.text_type(user.pk) + six.text_type(timestamp))


account_activation_token = tokenGenerator()