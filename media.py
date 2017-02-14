import webbrowser

class Video():
    def __init__(self, title, duration)
        self.title = title
        self.duration = duration

class Movie(Video):
    """ Title, duration ,movie storyline, poster image,
    and youtube trailer will all be displayed for movies"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self, title, duration, movie_storyline,
                poster_image, trailer_youtube):
        Video.__init__(self, title, duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class TvShow(Video):
    """title, duration, season, episode, and tv station will all
    be displayed for tv shows"""

    def _init__(self, title, duration, season, episode, tv_station)
        Video.__init__(self, title, duration)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station

    def get_local_listings(self):
