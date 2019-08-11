import logging
import os
from django.db.models import Q
from core.modules.youtube import searchengine
from core.models import Song


logger = logging.getLogger('django')


def search(q, local_only=False, *args, **kwargs):
    """
    Search for songs on current (local) library
    """
    result = list()
    fst_result = Song.objects.select_related('artist', 'colabs', 'genres')\
        .filter(
            Q(title__icontains=q)\
             | Q(artist__name__icontains=q)\
             | Q(colabs__name__icontains=q)\
             | Q(genres__name__icontains=q)
        )
    if not local_only:
        logger.debug('Sin resultados en la primera busqueda')
        # Search on YouTube
        try:
            snd_result = searchengine.search_youtube(search=q, max_duration=600)
        except Exception as e:
            logger.error(repr(e))
            snd_result = list()
        if len(snd_result):
            result = [
                {
                    'id': track['id'],
                    'artist': track['artist'],
                    'title': track['title'],
                    'url': track['url']
                } for track in snd_result
            ]
            result.extend(fst_result.values('id', 'artist', 'title', 'url'))
        else:
            logger.debug('Sin resultados en la segunda busqueda')
    else:
        result = fst_result.values('id', 'artist', 'title', 'url')
    logger.debug(repr(result))
    return result


def reindex(*args, **kwargs):
    pass
