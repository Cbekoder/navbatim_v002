from .models import User

def user_data(request):
    """
    Context processor to provide user data to all templates.
    """
    if request.user.is_authenticated:
        return {
            'current_user': request.user,
            'username': request.user.username,
            'is_authenticated': True,
        }
    return {
        'current_user': None,
        'username': None,
        'is_authenticated': False,
    }