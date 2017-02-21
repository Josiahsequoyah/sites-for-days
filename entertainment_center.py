import fresh_tomatoes
import media

# List of Movies and their information
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "1 hour 21 minutes",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
# print(toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "2 hours and 42 minutes",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")
# print(avatar.storyline)
# avatar.show_trailer()
lord_of_the_rings = media.Movie("Lord of the Rings",
                                "A hobbit on a fellowship",
                                "2 hours and 58 minutes",
                                "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_(2001)_theatrical_poster.jpg",
                                "https://www.youtube.com/watch?v=Pki6jbSbXIY")
# lord_of_the_rings.show_trailer()
avengers = media.Movie("Avengers",
                       "Marvel superheroes fighting villians",
                       "2 hours and 23 minutes",
                       "https://images-na.ssl-images-amazon.com/images/I/61bINjWK62L.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")
star_wars = media.Movie("Star Wars: Force Awakens",
                       "Rey looks for Luke Skywalker",
                       "http://a.dilcdn.com/bl/wp-content/uploads/sites/6/2015/10/star-wars-force-awakens-official-poster.jpg",
                       "https://www.youtube.com/watch?v=sGbxmsDFVnE")
inception = media.Movie("Inception",
                        "Man uses machine to enter dreams",
                        "2 hours and 28 minutes",
                        "http://www.impawards.com/2010/posters/inception.jpg",
                        "https://www.youtube.com/watch?v=66TuSJo4dZM")

# This function call opens a page of movies generated from the input, an array
# of movie instances.
movies = [toy_story, avatar, lord_of_the_rings, avengers, star_wars, inception]
fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.VALID_RATINGS)
# print(media.Movie.__doc__)
