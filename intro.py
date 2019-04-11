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