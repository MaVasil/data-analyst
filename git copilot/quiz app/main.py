def run_quiz():
    """Main quiz function that manages the quiz flow."""
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
            "answer": "C"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["A) 3", "B) 4", "C) 5", "D) 22"],
            "answer": "B"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
            "answer": "B"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
            "answer": "D"
        },
        {
            "question": "Who wrote Romeo and Juliet?",
            "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Jane Austen", "D) Mark Twain"],
            "answer": "B"
        },
        {
            "question": "What is the smallest prime number?",
            "options": ["A) 0", "B) 1", "C) 2", "D) 3"],
            "answer": "C"
        },
        {
            "question": "Which country is home to the kangaroo?",
            "options": ["A) Brazil", "B) India", "C) Australia", "D) South Africa"],
            "answer": "C"
        },
        {
            "question": "What is the chemical symbol for Gold?",
            "options": ["A) Go", "B) Gd", "C) Au", "D) Ag"],
            "answer": "C"
        },
        {
            "question": "How many continents are there?",
            "options": ["A) 5", "B) 6", "C) 7", "D) 8"],
            "answer": "C"
        },
        {
            "question": "What year did the Titanic sink?",
            "options": ["A) 1912", "B) 1920", "C) 1905", "D) 1915"],
            "answer": "A"
        }
    ]
    
    score = 0
    user_answers = []
    
    print("\n" + "="*60)
    print(" "*15 + "WELCOME TO THE QUIZ APP")
    print("="*60)
    print(f"\nTotal Questions: {len(questions)}")
    print("Instructions: Enter A, B, C, or D as your answer\n")
    
    # Display each question
    for index, q in enumerate(questions, 1):
        print(f"\nQuestion {index}/{len(questions)}: {q['question']}")
        for option in q['options']:
            print(f"  {option}")
        
        # Get user input with validation
        while True:
            user_answer = input("Your answer (A/B/C/D): ").strip().upper()
            if user_answer in ['A', 'B', 'C', 'D']:
                break
            else:
                print("Invalid input! Please enter A, B, C, or D.")
        
        user_answers.append(user_answer)
        
        # Check if answer is correct
        if user_answer == q['answer']:
            score += 1
            print("✓ Correct!")
        else:
            print(f"✗ Incorrect! The correct answer was {q['answer']}")
    
    # Display results
    display_results(score, len(questions), user_answers, questions)


def display_results(score, total, user_answers, questions):
    """Display quiz results and statistics."""
    percentage = (score / total) * 100
    
    print("\n" + "="*60)
    print(" "*20 + "QUIZ COMPLETED!")
    print("="*60)
    print(f"\nYour Score: {score}/{total}")
    print(f"Percentage: {percentage:.2f}%")
    
    # Grade assignment
    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    else:
        grade = "F"
    
    print(f"Grade: {grade}")
    print(f"\nCorrect Answers: {score}")
    print(f"Incorrect Answers: {total - score}")
    print("="*60)
    
    # Option to review answers
    review = input("\nWould you like to review your answers? (yes/no): ").strip().lower()
    if review == 'yes':
        display_review(user_answers, questions)
    
    # Option to retake quiz
    retry = input("\nWould you like to retake the quiz? (yes/no): ").strip().lower()
    if retry == 'yes':
        run_quiz()
    else:
        print("\nThank you for taking the quiz! Goodbye!\n")


def display_review(user_answers, questions):
    """Display detailed review of all answers."""
    print("\n" + "="*60)
    print(" "*20 + "ANSWER REVIEW")
    print("="*60)
    
    for index, (user_ans, q) in enumerate(zip(user_answers, questions), 1):
        correct_ans = q['answer']
        status = "✓" if user_ans == correct_ans else "✗"
        
        print(f"\nQuestion {index}: {q['question']}")
        print(f"Your Answer: {user_ans}")
        print(f"Correct Answer: {correct_ans}")
        print(f"Result: {status}")
    
    print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    while True:
        run_quiz()
        break