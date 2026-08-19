import time
import random

sentences=[
    "The quick brown fox jumps over the lazy dog.",
    "Pack my box with five dozen liquor jugs.",
    "How vexingly quick daft zebras jump!",
]

def typing_test():
    """Run a typing test with random sentences."""
    sentence = random.choice(sentences)
    print("Type the following sentence:")
    print(sentence)
    
    start_time = time.time()
    user_input = input("Your input: ")
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    words_typed = len(user_input.split())
    wpm = (words_typed / elapsed_time) * 60
    
    accuracy = sum(1 for a, b in zip(user_input, sentence) if a == b) / len(sentence) * 100
    
    print(f"Time taken: {elapsed_time:.2f} seconds")
    print(f"Words per minute (WPM): {wpm:.2f}")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    typing_test()
    