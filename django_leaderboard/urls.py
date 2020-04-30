from django.conf.urls import url, include
from django_leaderboard.views import ScoresView, ScoresAroundMeView
from django.urls import path, include


urlpatterns = [
    #path('django_leaderboard.views'),
    # Api urls
    path(r'^$', ScoresView.as_view(), name='leaderboard_api'),
    path(r'^api/(?P<game>[\w.@+-]+)/user/(?P<user_id>[\w.@+-]+)/', ScoresAroundMeView.as_view(), name='leaderboard_around_me_api'),
    path(r'^api/(?P<game>[\w.@+-]+)/$', ScoresView.as_view(), name='leaderboard_api'),
    path(r'^api/(?P<game>[\w.@+-]+)/(?P<page>[0-9]+)/$', ScoresView.as_view(), name='leaderboard_api_with_page'),

    # the leaderboard for the high scores
   # path(r'^highscores/(?P<game>[\w.@+-]+)/$', 'highscores', name="leaderboard_high_scores"),
    #path(r'^highscores/(?P<game>[\w.@+-]+)/(?P<page>[\w.@+-]+)/$', 'highscores', name="leaderboard_high_scores_with_page"),
]