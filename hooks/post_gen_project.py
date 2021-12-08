import os
import random
import shutil
import string

try:
    # Inspired by
    # https://github.com/django/django/blob/master/django/utils/crypto.py
    random = random.SystemRandom()
    using_sysrandom = True
except NotImplementedError:
    using_sysrandom = False

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "

DEBUG_VALUE = "debug"


def generate_random_string(
        length, using_digits=False, using_ascii_letters=False, using_punctuation=False
):
    """
    Example:
        opting out for 50 symbol-long, [a-z][A-Z][0-9] string
        would yield log_2((26+26+50)^50) ~= 334 bit strength.
    """
    if not using_sysrandom:
        return None

    symbols = []
    if using_digits:
        symbols += string.digits
    if using_ascii_letters:
        symbols += string.ascii_letters
    if using_punctuation:
        all_punctuation = set(string.punctuation)
        # These symbols can cause issues in environment variables
        unsuitable = {"'", '"', "\\", "$"}
        suitable = all_punctuation.difference(unsuitable)
        symbols += "".join(suitable)
    return "".join([random.choice(symbols) for _ in range(length)])


def set_flag(file_path, flag, value=None, formatted=None, *args, **kwargs):
    if value is None:
        random_string = generate_random_string(*args, **kwargs)
        if random_string is None:
            print(
                "We couldn't find a secure pseudo-random number generator on your "
                "system. Please, make sure to manually {} later.".format(flag)
            )
            random_string = flag
        if formatted is not None:
            random_string = formatted.format(random_string)
        value = random_string

    with open(file_path, "r+") as f:
        file_contents = f.read().replace(flag, value)
        f.seek(0)
        f.write(file_contents)
        f.truncate()

    return value


def set_django_secret_key(file_path):
    django_secret_key = set_flag(
        file_path,
        "!!!SET DJANGO_SECRET_KEY!!!",
        length=64,
        using_digits=True,
        using_ascii_letters=True,
    )
    return django_secret_key


def set_django_admin_url(file_path):
    django_admin_url = set_flag(
        file_path,
        "!!!SET DJANGO_ADMIN_URL!!!",
        formatted="{}/",
        length=32,
        using_digits=True,
        using_ascii_letters=True,
    )
    return django_admin_url


def generate_random_user():
    return generate_random_string(length=32, using_ascii_letters=True)


def generate_postgres_user(debug=False):
    return DEBUG_VALUE if debug else generate_random_user()


def generate_postgres_user(debug=False):
    return DEBUG_VALUE if debug else generate_random_user()


def set_postgres_user(file_path, value):
    postgres_user = set_flag(file_path, "!!!SET POSTGRES_USER!!!", value=value)
    return postgres_user


def set_postgres_password(file_path, value=None):
    postgres_password = set_flag(
        file_path,
        "!!!SET POSTGRES_PASSWORD!!!",
        value=value,
        length=64,
        using_digits=True,
        using_ascii_letters=True,
    )
    return postgres_password


def set_flags_in_envs(postgres_user, celery_flower_user, debug=False):
    local_django_envs_path = os.path.join(".envs", ".local", ".spot")
    production_django_envs_path = os.path.join(".envs", ".production", ".spot")
    local_postgres_envs_path = os.path.join(".envs", ".local", ".postgres")
    production_postgres_envs_path = os.path.join(".envs", ".production", ".postgres")

    set_django_secret_key(production_django_envs_path)
    set_django_admin_url(production_django_envs_path)

    set_postgres_user(local_postgres_envs_path, value=postgres_user)
    set_postgres_password(
        local_postgres_envs_path, value=DEBUG_VALUE if debug else None
    )
    set_postgres_user(production_postgres_envs_path, value=postgres_user)
    set_postgres_password(
        production_postgres_envs_path, value=DEBUG_VALUE if debug else None
    )


def set_flags_in_settings_files():
    set_django_secret_key(os.path.join("spot", "app", "config", "settings", "local.py"))
    set_django_secret_key(os.path.join("spot", "app", "config", "settings", "test.py"))


def append_to_gitignore_file(s):
    with open(".gitignore", "a") as gitignore_file:
        gitignore_file.write(s)
        gitignore_file.write(os.linesep)


def spot():
    debug = "{{ cookiecutter.debug }}".lower() == "y"

    set_flags_in_envs(
        DEBUG_VALUE if debug else generate_random_user(),
        DEBUG_VALUE if debug else generate_random_user(),
        debug=debug,
    )
    set_flags_in_settings_files()

    append_to_gitignore_file(".env")
    append_to_gitignore_file(".envs/*")

    print(SUCCESS + "Project initialized, keep up the good work!" + TERMINATOR)


def main():
    enable_adapter = '{{cookiecutter.enable_adapter}}' == 'y'
    enable_cache = '{{cookiecutter.enable_cache}}' == 'y'
    enable_ui = '{{cookiecutter.enable_ui}}' == 'y'
    enable_proxy = '{{cookiecutter.enable_proxy}}' == 'y'
    enable_spot = '{{cookiecutter.enable_spot}}' == 'y'

    def remove(filepath):
        if os.path.isfile(filepath):
            os.remove(filepath)
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath)

    if not enable_adapter:
        remove('./adapter')
        remove('./tests/adapter')
        remove('./compose/local/adapter')

    if not enable_cache:
        remove('./cache')
        remove('./tests/cache')
        remove('./compose/local/cache')

    if not enable_ui:
        remove('./ui')
        remove('./tests/ui')
        remove('./compose/local/ui')

    if not enable_proxy:
        remove('./proxy')
        remove('./tests/proxy')
        remove('./compose/local/proxy')

    if not enable_spot:
        remove('./spot')
        remove('./tests/spot')
        remove('./compose/local/spot')


if __name__ == "__main__":
    main()
    spot()
