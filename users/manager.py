from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email: str, password: str, username: str = None, **extra_fields):
        """Management user.
        Required fields: email, password.
        """
        if not email:
            raise ValueError('email cannot be empty')
        email = self.normalize_email(email)

        if not username:
            username = self.name_from_email(email=email)

        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    @classmethod
    def name_from_email(cls, email: str):
        name, domain = email.strip().rsplit("@", 1)
        return name

    def create_user(self, email: str, password: str, username: str, **extra_fields):
        extra_fields.setdefault('is_admin', False)
        return self._create_user(email, password, username, **extra_fields)

    def create_superuser(self, email: str, password: str, username: str, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, username, **extra_fields)
