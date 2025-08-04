from django.urls import reverse
from django.shortcuts import redirect

class RedirectAuthenticatedUserMiddleware:
    def __init__(self, get_response): #checking that any path requested or responsed in middleware
        self.get_response = get_response #suppose there is no other middleware it just return to the view function

    def __call__(self, request):
        #check the user is authencticated
        if request.user.is_authenticated:
            #List of paths to check
            paths_to_redirect = [reverse('blog:login'), reverse('blog:register')]
            #checking the user is already is there in this path

            if request.path in paths_to_redirect:
                return redirect(reverse('blog:index'))
            
        #suppose redirection cant unable to the request
        response = self.get_response(request)
        return response

#Restrictedunauthenticated class
class RestrictedUnauthenticatedUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        restricted_paths = [reverse('blog:dashboard')]

        if not request.user.is_authenticated and request.path in restricted_paths:
            return redirect(reverse('blog:login'))
        response = self.get_response(request)
        return response

        
