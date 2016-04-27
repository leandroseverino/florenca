import os, sys

florenca_configuration = os.path.realpath(os.path.dirname(__file__))
project = os.path.join(florenca_configuration, 'website')

# sys.path.append('/home/imobiliariaflorenca/apps_wsgi')
# sys.path.append('/home/imobiliariaflorenca/apps_wsgi/website')

sys.path.append(florenca_configuration)
sys.path.append(project)
sys.path.insert(0, "/home/imobiliariaflorenca/.virtualenvs/florenca/lib/python2.7/site-packages")

os.environ['PYTHON_EGG_CACHE'] = '/home/imobiliariaflorenca/apps_wsgi/.python-eggs'
#os.environ['DJANGO_SETTINGS_MODULE']='website.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE" , "website.settings")

#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
