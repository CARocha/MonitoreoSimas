from django.http import HttpResponseRedirect

def session_required(f):
    def check_session(request, **kwargs):
        if 'activo' not in request.session:
            return HttpResponseRedirect('/')
        return f(request, **kwargs)
    return check_session
