"""jvbienesraices URL Configuration


Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

urlpatterns = [
    path('index/', include("index_app.urls")),
    path('propiedades/', include("propiedades.urls")),
    path('captacion/', include("captacion.urls")),
    path('contacto/', include("contacto.urls")),
]
