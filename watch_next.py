# Import spacy
import spacy

# load spacy language model
n1p = spacy.load('en_core_web_md')

# Sample text to pass into function
sample_text = "“Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, " \
              "the Illuminati " \
              "trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. " \
              "Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.”"


# Function to get the highest similarity from movie text file taking movie description as parameter
def get_similar_movie(description_comparison):
    # Create lists to store movie name and description
    movie_names = []
    description_list = []
    # Open movie text file
    with open("movies.txt", "r") as movie_file:
        for line in movie_file:
            # Split each line by : to give 2 parts of sentence movie / description
            movie_description = line.strip().split(":")
            # Assign movie name to part 1 of line
            movie = movie_description[0]
            # Assign description to part 2
            description = movie_description[1]
            # Append each part to corresponding list
            description_list.append(description)
            movie_names.append(movie)

    # applies spacy language model to function argument for comparison
    model_sentence = n1p(description_comparison)

    # Used to track the highest similarity movie description, and it's index position
    max_similarity = -1
    best_match_index = -1
    # Enumerate and iterate through description list
    for i, movie_synopsis in enumerate(description_list):
        # Assign similarity score to variable - comparing list synopsis to model sentence score
        similarity = n1p(movie_synopsis).similarity(model_sentence)
        if similarity > max_similarity:
            # Then assign the similarity score and index position to variables
            max_similarity = similarity
            best_match_index = i
    # Return movie and description with the highest matched score
    print("Movie: ", movie_names[best_match_index])
    print("Description: ", description_list[best_match_index])


get_similar_movie(sample_text)
