import random
import re

# Load and preprocess the input data
with open("shakespeare.txt", "r", encoding="utf-8") as file:
    shakespeare_text = file.read()

# Preprocess the text: remove extra whitespaces and split into words
shakespeare_text = re.sub(r'\s+', ' ', shakespeare_text)
shakespeare_words = shakespeare_text.split()

# Create a dictionary to store word transitions
word_transitions = {}
for i in range(len(shakespeare_words) - 1):
    current_word = shakespeare_words[i]
    next_word = shakespeare_words[i + 1]
    if current_word in word_transitions:
        word_transitions[current_word].append(next_word)
    else:
        word_transitions[current_word] = [next_word]

# Function to generate text using MCMC
def generate_text(initial_word, num_words=100):
    generated_text = [initial_word]
    current_word = initial_word

    for _ in range(num_words - 1):
        if current_word in word_transitions:
            next_word = random.choice(word_transitions[current_word])
            generated_text.append(next_word)
            current_word = next_word
        else:
            break

    return ' '.join(generated_text)

# Choose an initial word to start the chain
initial_word = random.choice(shakespeare_words)

# Generate text using MCMC
generated_text = generate_text(initial_word, num_words=200)

# Print the generated text
print(generated_text)
