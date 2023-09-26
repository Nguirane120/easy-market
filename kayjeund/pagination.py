from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 5  # Nombre d'éléments par page
    page_size_query_param = 'page_size'
    max_page_size = 100  # Limite supérieure de la taille de 
    
    def paginate_queryset(self, queryset, request, view=None):
        # Obtenez la taille de page à partir des paramètres de requête ou utilisez la valeur par défaut.
        self.page_size = int(request.query_params.get(self.page_size_query_param, self.page_size))
        return super().paginate_queryset(queryset, request, view)