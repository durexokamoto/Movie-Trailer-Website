import webbrowser
class Movie(object):
    '''This class provides a way to store movie related information

        Attributes:
            title (str): Name of the movie.
            storyline (str): A brief summary of the plot.
            poster_image_url (str): A link which directs to the box art of this movie.
            trailer_youtube_url (str): A youtube link directs to the movie's trailer'''
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Define a method to open the youtube link in the browser and play the trailer.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
