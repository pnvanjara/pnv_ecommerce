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
        # Adding media Directory
            # go to pnv_eccomerse/settings.py
            # Add Last (static url after)
                # MEDIA_ROOT = os.path.join(BASE_DIR,'media')
                # MEDIA_URL = '/media/'
            # then go you main project urls.py
                # imports this
                    # form django.conf import settings
                    # from django.conf.urls.static imprt static
                # urlpatterns = [
                # ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        # Fetching product using python manage.py shell
            # Written codes
                # python manage.py shell
                    # open shell
                # from pnv_shop.models import Product
                    # import product table in pnv_shop
                # from django.utils import timezone
                    # import timezone
                # Product.objects.all
                    # all object get
                # Add data in your database table
                    # myprod = Product(product_name="mouse",category="computer",subcategory="devices",price=10,desc="mouses of product",pub_date=timezone.now())
                        # add all poduct
                    # myprod.save()
                        # save myprod
                        # add new record in your database
                # get any product
                    # Product.objects.get(product_name="mouse")
        # Template Inheritance
            # you extends file give path
                # {% extends 'file_path' %}
            # after main file made so, all same content add this file all other file extends this file
                # made blocks you add in this extends file
                # ex...
                    # in body
                        # {% block body %} {% endblock %}
                    # add i extends file
                        # {% block body %} written all in this {% endblock %}
                    #ex...
                        # in about.html
                            # '   {% extends 'pnv_shop/main.html' %}
                            #     {% block title %}About{% endblock %}
                            #     {% block body %}
                            #     <center><h1>About Page</h1></center>
                            #     {% endblock %}
        # Showing Product in homepage
            # first import in views model
                # from .models import Product
            # written in views 
                # products = Product.objects.all()
                    # for get all product table data fetch

