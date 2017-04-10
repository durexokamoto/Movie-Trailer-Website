import media
import fresh_tomatoes

the_shawshank_redemption = media.Movie("The Shawshank Redemption",
                                       "Two imprisoned men bond over a number of years,"
                                       " finding solace and eventual redemption through"
                                       " acts of common decency.",
                                       "https://images-na.ssl-images-amazon.com/images/M/MV5BODU4M"
                                       "jU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._"
                                       "V1_SY1000_CR0,0,672,1000_AL_.jpg",
                                       "https://www.youtube.com/watch?v=RLw6hBFJ8bk")

the_godfather = media.Movie("The Godfather",
                            "The aging patriarch of an organized crime dynasty transfers control"
                            " of his clandestine empire to his reluctant son.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BZTRmNjQ1ZDYt"
                            "NDgzMy00OGE0LWE4N2YtNTkzNWQ5ZDhlNGJmL2ltYWdlL2ltYWdlXkEyX"
                            "kFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,704,1000_AL_.jpg",
                            "https://www.youtube.com/watch?v=vdQi6Ebjm8c")

the_godfather_part_ii = media.Movie("The Godfather: Part II",
                                    "The early life and career of Vito Corleone in 1920s "
                                    "New York is portrayed while his son, Michael, expands "
                                    "and tightens his grip on the family crime syndicate.",
                                    "https://images-na.ssl-images-amazon.com/images/M/MV5B"
                                    "MjZiNzIxNTQtNDc5Zi00YWY1LThkMTctMDgzYjY4YjI1YmQyL2ltYW"
                                    "dlL2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,702,1000_AL_.jpg",
                                    "https://www.youtube.com/watch?v=a8PT11hT-aM")

the_dark_knight = media.Movie("The Dark Knight",
                              "When the menace known as the Joker wreaks havoc and "
                              "chaos on the people of Gotham, the Dark Knight must "
                              "come to terms with one of the greatest psychological "
                              "tests of his ability to fight injustice.",
                              "https://images-na.ssl-images-amazon.com/images/M/M"
                              "V5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1"
                              "_SY1000_CR0,0,675,1000_AL_.jpg",
                              "https://www.youtube.com/watch?v=qY3UkAHufLY")

twelve_angry_men = media.Movie("12 Angry Men",
                               "A jury holdout attempts to prevent a miscarriage of justice"
                               " by forcing his colleagues to reconsider the evidence.",
                               "https://images-na.ssl-images-amazon.com/images/M/MV5BODQwOTc5"
                               "MDM2N15BMl5BanBnXkFtZTcwODQxNTEzNA@@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
                               "https://www.youtube.com/watch?v=J61XJhYiUpg")

pulp_fiction = media.Movie("Pulp Fiction",
                           "The lives of two mob hit men, a boxer, a gangster's"
                           " wife, and a pair of diner bandits intertwine in fou"
                           "r tales of violence and redemption.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV"
                           "5BMTkxMTA5OTAzMl5BMl5BanBnXkFtZTgwNjA5M"
                           "Dc3NjE@._V1_SY1000_CR0,0,673,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=hhMtO1MVFSo")

movies = [the_shawshank_redemption, the_godfather, the_godfather_part_ii, the_dark_knight, twelve_angry_men, pulp_fiction]
fresh_tomatoes.open_movies_page(movies)
