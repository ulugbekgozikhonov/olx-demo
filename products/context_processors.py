def language_processor(request):
    return {'LANGUAGE_CODE': request.session.get('language', 'uz')}
