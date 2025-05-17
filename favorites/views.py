from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Favorite


@csrf_exempt  # Remove this in production and use proper CSRF protection
@require_http_methods(["POST"])
def add_favorite(request):
    try:
        data = json.loads(request.body)
        book_id = data.get('book_id')

        if not book_id:
            return JsonResponse({'success': False, 'error': 'No book ID provided'})

        # For now, if user isn't authenticated, use a session-based approach
        if request.user.is_authenticated:
            favorite, created = Favorite.objects.get_or_create(
                user=request.user,
                book_id=book_id
            )
        else:
            # Return success but note that it's only stored locally
            return JsonResponse({'success': True, 'note': 'stored_locally_only'})

        return JsonResponse({'success': True, 'created': created})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})


@csrf_exempt  # Remove this in production
@require_http_methods(["POST"])
def delete_favorite(request):
    try:
        data = json.loads(request.body)
        book_id = data.get('book_id')

        if not book_id:
            return JsonResponse({'success': False, 'error': 'No book ID provided'})

        if request.user.is_authenticated:
            deleted, _ = Favorite.objects.filter(user=request.user, book_id=book_id).delete()
            return JsonResponse({'success': True, 'deleted': deleted > 0})
        else:
            # Return success for consistency in local-only mode
            return JsonResponse({'success': True, 'note': 'stored_locally_only'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})


@require_http_methods(["GET"])
def get_favorites(request):
    try:
        if request.user.is_authenticated:
            favorites = list(Favorite.objects.filter(
                user=request.user
            ).values_list('book_id', flat=True))
            return JsonResponse({
                'success': True,
                'favorites': favorites
            })
        else:
            # For non-authenticated users, return empty list
            return JsonResponse({
                'success': True,
                'favorites': [],
                'note': 'user_not_authenticated'
            })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})
