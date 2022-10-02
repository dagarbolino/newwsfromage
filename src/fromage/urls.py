from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from fromage import settings

from cheese import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('patepresseescuite/', views.patepresseescuite, name='patepresseescuite'),
    path('patemolle/', views.patemolle, name='patemolle'),
    path('patefleurie/', views.patefleurie, name='patefleurie'),
    path('fromagedechevre/', views.fromagedechevre, name='fromagedechevre'),
    path('fromagedebrebis/', views.fromagedebrebis, name='fromagedebrebis'),
    path('patepersillee/', views.patepersillee, name='patepersillee'),
    path('triplecreme/', views.triplecreme, name='triplecreme'),
    path('pateforte/', views.pateforte, name='pateforte'),
    path('allcheese/', views.allcheese, name='allcheese'),
    path('detail/<str:slug>/', views.product_detail, name='detail'),
    path('contact/', views.contact, name='contact'),
    path('lieux/', views.lieux, name='lieux'),
    path('recettes/', views.recettes, name='recettes'),
    path('questions/', views.questions, name='questions'),
    path('livraison/', views.livraison, name='livraison'),
    path('nous/', views.nous, name='nous'),
    path('origine_nord/', views.origine_nord, name='origine_nord'),
    path('plateau/', views.plateau, name='plateau'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
