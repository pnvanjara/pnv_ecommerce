# pnv_eccomerce
    # Commands
        # django-admin
            # commands using django
        # django-admin startproject project_name
            # made project
        # python manage.py runserver
            # server run
        # python manage.py startapp app_name
            # made sub project in main project
        # python manage.py migrate
            # includes all tables django used this make
        # python manage.py makemigrations
            # store migrations
            # only store in over programme
            # but not migrate in database
        # python manage.py createsuperuser
                # add admin functonality
    # include file
         # path('pnv_shop/', include('pnv_shop.urls'))
            # include other app urls
    # Templating Add
        # in you sub folder made tempates forlder & in to this made same name your sub folder made
        # after in setting. py of main folder in installed apps give both tmplates sub folder name
        # after in views render this templates
    # Static directory
        # made directory same as templates
        # static directory you made for includeing in main files
        # load in templates html file
            # {% load static %}
            # href="{%static 'pnv_blog/static_file'  %}"
    # Model in Django
        # python manage.py migrate
            # includes all tables django used this make
        # python manage.py makemigrations
            # store migrations
            # only store in over programme
            # but not migrate in database
            # first made model table class after used it
            # python manage.py migrate
                # when you apply in database
        # Django Admin & addin data
            # made super user
                # admin functionality add
            # python manage.py createsuperuser
                # add admin functonality
                # so you are used admin/ in browser
            # After register you table model
                # go to pnv_shp/admin.py
                # write this
                    # from .models import Product
                    # admin.site.register(Product)
                # after restart you server
                