import webbrowser


class Media():
    """This class provides general information for
    all types of stories, regardless of medium."""
    def __init__(self,
                 title,
                 synopsis,
                 poster_image_url,
                 trailer_youtube_url,
                 genre,
                 release_year):
        # Initialize instance
        self.title = title
        self.synopsis = synopsis
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.genre = genre
        self.release_year = release_year


class Movie(Media):
    """This extends Media with details specific to Movies"""
    def __init__(self,
                 title,
                 synopsis,
                 poster_image_url,
                 trailer_youtube_url,
                 genre,
                 release_year,
                 rotten_tomatoes_score,
                 director,
                 leads):
        Media.__init__(self,
                       title,
                       synopsis,
                       poster_image_url,
                       trailer_youtube_url,
                       genre,
                       release_year)
        self.rotten_tomatoes_score = rotten_tomatoes_score
        self.director = director
        self.leads = leads


class Game(Media):
    """This extends Media with details specific to Movies"""
    def __init__(self,
                 title,
                 synopsis,
                 poster_image_url,
                 trailer_youtube_url,
                 genre,
                 release_year,
                 ign_score,
                 studio,
                 protagonist):
        Media.__init__(self,
                       title,
                       synopsis,
                       poster_image_url,
                       trailer_youtube_url,
                       genre,
                       release_year)
        self.ign_score = ign_score
        self.studio = studio
        self.protagonist = protagonist
