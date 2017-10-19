from django.conf.urls import url, include
from webodt import views
from .views import test_pdf, test_iterator, test_pdf_from_html

app_name = 'webodt'

urlpatterns = [
    url(r'^test/pdf/$', test_pdf, name='webodt-test-pdf'),
    url(r'^test/iterator/$', test_iterator, name='webodt-test-iterator'),
    url(r'^test/pdf_from_html/$', test_pdf_from_html, name='webodt-test-pdf-from-html'),
]
