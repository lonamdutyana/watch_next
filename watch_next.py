import spacy

def load_spacy_model():
    # Load the English language model in spaCy
    nlp = spacy.load("en_core_web_md")
    return nlp

def get_most_similar_movie(description, movies, nlp):
    # Process the description using spaCy
    desc_doc = nlp(description)

    # Calculate similarity between description and each movie's description
    similarities = {}
    for movie_title, movie_description in movies.items():
        movie_doc = nlp(movie_description)
        similarity = desc_doc.similarity(movie_doc)
        similarities[movie_title] = similarity

    # Return the title of the movie with the highest similarity
    return max(similarities, key=similarities.get)

def main():
    # Load spaCy model
    nlp = load_spacy_model()

    # Read in the movies.txt file
    with open('movies.txt', 'r') as file:
        lines = file.readlines()

    # Parse movie titles and descriptions
    movies = {}
    for line in lines:
        movie_title, movie_description = line.split(':', 1)
        movies[movie_title.strip()] = movie_description.strip()

    # Description of "Planet Hulk"
    description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

    # Get the most similar movie
    next_movie = get_most_similar_movie(description, movies, nlp)
    print("Next movie to watch:", next_movie)

if __name__ == "__main__":
    main()
