import json
import random
import time
from colorama import init, Fore, Style
import sys

# Initialize colorama
init(autoreset=True)

def load_questions(filename):
    try:
        with open(filename, 'r') as file:
            questions_data = json.load(file)
            return questions_data['questions']
    except FileNotFoundError:
        print(f"{Fore.RED}❌ Error: The file '{filename}' was not found.")
        return []
    except json.JSONDecodeError:
        print(f"{Fore.RED}❌ Error: The file '{filename}' is not valid JSON.")
        return []

def display_feedback(is_correct, explanation, current_score):
    if is_correct:
        print(Fore.GREEN + "\n✅ Correct!")
    else:
        print(Fore.RED + "\n❌ Incorrect!")
    print(Fore.YELLOW + f"Explanation: {explanation}")
    print(Fore.CYAN + f"Your current score: {current_score}\n")

def check_answer(user_answer, current_question, score):
    correct_answer = current_question['correct_answer']
    question_type = current_question['type']
    is_correct = False
    explanation = f"The correct answer is {correct_answer}."

    if question_type == "multiple-choice":
        user_answer = user_answer.strip().upper()
        if len(user_answer) != 1 or user_answer not in ['A', 'B', 'C', 'D']:
            print(Fore.RED + "⚠ Invalid input. Please enter A, B, C, or D.")
            return score, False
        index = ord(user_answer) - ord('A')
        selected = current_question['options'][index]
        if selected.strip().lower() == correct_answer.strip().lower():
            is_correct = True
            score += 10

    elif question_type == "true/false":
        mapped = ''
        if user_answer.upper() == 'A':
            mapped = 'true'
        elif user_answer.upper() == 'B':
            mapped = 'false'
        else:
            mapped = user_answer.strip().lower()
        if mapped == correct_answer.strip().lower():
            is_correct = True
            score += 10

    elif question_type == "open-ended":
        if isinstance(correct_answer, list):
            is_correct = any(user_answer.strip().lower() == ans.strip().lower() for ans in correct_answer)
        else:
            is_correct = user_answer.strip().lower() == correct_answer.strip().lower()
        if is_correct:
            score += 15

    display_feedback(is_correct, explanation, score)
    return score, is_correct

def display_round_number(current_round, difficulty):
    print("\n" + "=" * 40)
    print(f"{Fore.MAGENTA}🏁 ROUND {current_round} | Difficulty: {difficulty}")
    print("=" * 40 + "\n")

def ask_question(q):
    print(Fore.BLUE + f"\nCategory: {q.get('category', 'General')}")
    print(Fore.BLUE + f"Question: {q['question']}")
    if q['type'] == 'multiple-choice':
        options = q['options'].copy()
        random.shuffle(options)
        for idx, option in enumerate(options):
            letter = chr(ord('A') + idx)
            print(f"{letter}) {option}")
        return options
    elif q['type'] == 'true/false':
        print("A) True")
        print("B) False")
    elif q['type'] == 'open-ended':
        print("Please provide your answer:")

def save_score(player_name, final_score, accuracy):
    try:
        with open("scores.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append({
        "name": player_name,
        "score": final_score,
        "accuracy": accuracy,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    })

    with open("scores.json", "w") as file:
        json.dump(data, file, indent=2)

def display_leaderboard():
    try:
        with open("scores.json", "r") as file:
            data = json.load(file)
        if not data:
            print(Fore.YELLOW + "⚠ No scores yet!")
            return
        print("\n🏆 LEADERBOARD (Top 5)")
        sorted_data = sorted(data, key=lambda x: x['score'], reverse=True)
        for entry in sorted_data[:5]:
            print(f"{entry['name']} | {entry['score']} pts | {entry['accuracy']:.2f}% | {entry['timestamp']}")
    except FileNotFoundError:
        print(Fore.YELLOW + "⚠ No leaderboard data found.")

def get_input_with_exit(prompt):
    user_input = input(prompt).strip()
    if user_input.lower() in ['exit()', 'quit()']:
        print(Fore.YELLOW + "👋 Exiting the game. Goodbye!")
        sys.exit()
    return user_input

# --- MAIN FLOW ---
questions = load_questions("questions.json")

if questions:
    display_leaderboard()

    total_score = 0
    current_round = 1
    total_correct = 0
    total_questions = 0

    player_name = get_input_with_exit("Enter your name (or type exit() to quit): ")
    difficulty = get_input_with_exit("Choose difficulty (easy/medium/hard): ").lower()

    # Filter questions for selected difficulty
    available_questions = [q for q in questions if q.get('difficulty', 'medium') == difficulty]
    if not available_questions:
        print(Fore.RED + f"No questions found for difficulty '{difficulty}'.")
        sys.exit()

    while current_round <= 5:
        if len(available_questions) < 10:
            print(Fore.YELLOW + f"⚠ Not enough questions left for Round {current_round}. Ending game.")
            break

        display_round_number(current_round, difficulty)

        round_questions = random.sample(available_questions, 10)  # pick 10 unique questions
        for q in round_questions:
            ask_question(q)

            start_time = time.time()
            user_answer = get_input_with_exit(Fore.WHITE + "\nEnter your answer: ")
            time_taken = time.time() - start_time

            if time_taken > 30:
                print(Fore.RED + "⏰ Time's up! Moving to next question.")
                continue

            total_score, is_correct = check_answer(user_answer, q, total_score)
            total_questions += 1
            if is_correct:
                total_correct += 1

            available_questions.remove(q)  # remove asked question

        print(f"\n✅ Round {current_round} completed!")
        print(Fore.CYAN + f"Your total score: {total_score}")

        current_round += 1

    accuracy = (total_correct / total_questions) * 100 if total_questions > 0 else 0
    print("\n🎉 Thanks for playing!")
    print(Fore.CYAN + f"🏁 Final Score: {total_score}")
    print(Fore.CYAN + f"📊 Accuracy: {accuracy:.2f}%")
    save_score(player_name, total_score, accuracy)
    print(Fore.GREEN + "✅ Your score has been saved!")
else:
    print(Fore.RED + "⚠ Cannot start the game without questions.")
