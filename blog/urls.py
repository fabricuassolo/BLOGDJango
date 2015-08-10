from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
                       url(r'^$', 'blog.views.verhome', name='Inicio' ),
                       url(r'^ver_post/(?P<id_post>[0-9]+)/$', 'blog.views.ver_post', name='vermipost'),
                       url(r'^cv/$', 'blog.views.vercv', name='CV' ),
                       url(r'^botonmagico/$', 'blog.views.verbtnmg', name='Boton Magico' ),
                       url(r'^calculadora/$', 'blog.views.vercal', name='Calculadora' ),
                       url(r'^contactos/$', 'blog.views.vercon', name='Contactos' ),
                       url(r'^conversor/$', 'blog.views.verconv', name='Conversor' ),
                       url(r'^cronometro/$', 'blog.views.vercro', name='Cronometro' ),
                       url(r'^galeria/$', 'blog.views.verimagen', name='Galeria' ),

                       url(r'^noticias/$', 'blog.views.vernoticias', name='Noticias' ),
                      )
