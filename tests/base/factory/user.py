from django.contrib.auth.models import User


def create(username, password, email):
    u = User.objects.filter(username=username)
    if not u:
        u = User(username=username, email=email)
        u.set_password(password)
        u.save()
    return u


def remove(username):
    User.objects.filter(username=username).delete()


''' FAKES '''
fake_username = 'fake_user'
fake_password = 'password_of_fake_user'
fake_email = 'test@t.ru'


def create_fake_user():
    return create(fake_username, fake_password, fake_email)


def remove_fake_user():
    try:
        remove(fake_username)
    except:
        pass
