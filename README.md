**Describe the bug**

Customized models lead to errors at different stages of migration.

The complex case with the customized `Application` model and another model referencing the `AccessToken` model produces different errors while the migration process, depending on the application settings (direct swapping of the `AccessToken` model is also unavailable, see f.e. #1017).

Without the `settings.OAUTH2_PROVIDER_ACCESS_TOKEN_MODEL` the `makemigrations` command fails with the following:

```
AttributeError: 'Settings' object has no attribute 'OAUTH2_PROVIDER_ACCESS_TOKEN_MODEL'
```

Having the `settings.OAUTH2_PROVIDER_ACCESS_TOKEN_MODEL`, the `makemigrations` command is successful but the following initial migration fails with another error:
```
ValueError: Related model 'myoauth.oauth2app' cannot be resolved
```

**To Reproduce**
1. Install last `Django`, last `django-oauth-toolkit` package, and clone the repository https://github.com/nnseva/django-oauth-bad-case
2. Try `python manage.py makemigrations myoauth`, it should work properly
3. Try `python manage.py makemigrations badcase`, it produces the first error
4. Try to fix the error using modified settings `python manage.py makemigrations --settings djoauth.settings_case2` (use `diff` to see a difference)
5. Try to process migrations `python manage.py migrate --settings djoauth.settings_case2`, see the second error
6. You can see the first error again if trying to process migrations with the default settings `python manage.py migrate`
7. See the workaround, processing migrations for different applications separately:
- `python manage.py migrate myoauth --settings djoauth.settings_case2`
- `python manage.py migrate badcase --settings djoauth.settings_case2`

**Expected behavior**

Either step 3, or step 5 is expected to be errorless.

**Version**

```
(py3.8.test.djoauth) seva@SEVA-MOBILE:~/py3.8.test.djoauth/test/djoauth$ pip freeze
asgiref==3.5.2
backports.zoneinfo==0.2.1
certifi==2022.9.24
cffi==1.15.1
charset-normalizer==2.1.1
cryptography==38.0.3
Deprecated==1.2.13
Django==4.1.3
django-oauth-toolkit==2.2.0
idna==3.4
jwcrypto==1.4.2
oauthlib==3.2.2
pycparser==2.21
requests==2.28.1
sqlparse==0.4.3
urllib3==1.26.12
wrapt==1.14.1
```

The error looks like appears for all versions up to django-oauth-toolkit==2.2.0

I really have met the problem for the first time with django-oauth-toolkit==1.7.1 and Django==2.2.5, but checked against a last available stable Django version, and latest versions of the django-oauth-toolkit package. 

- [x] I have tested with the latest published release and it's still a problem.
- [x] I have tested with the master branch and it's still a problem.

**Additional context**
No any
