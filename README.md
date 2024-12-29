# nimap
# 1. Clone Repository
    git clone https://github.com/devvaja/nimap.git

# 2. Setup Project
     cd nimap
     python -m venv .venv
    .venv/Scripts/activate
    pip install django djangorestframework mysqlclient
    
# 3. Install all requirements
    pip install -r requirements.txt

# 4. Change Database To MYSQL
        DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'Your database name',
            'USER': 'your username',
            'PASSWORD': 'your password',
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
        }
# 5. Run server
        python manage.py runserver
        
