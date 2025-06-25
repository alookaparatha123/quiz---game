# Python Quiz Game

A console-based quiz game built using Python. The game supports multiple question types, tracks scores, and saves high scores locally. Designed for easy use and extension.

## Features

- Supports multiple-choice, true/false, and open-ended questions  
- 5 rounds, 10 questions per round  
- Tracks player score and accuracy  
- Saves high scores to a local JSON file  

## Project Structure

quiz-game/
├── quiz_game.py         # Main game script  
├── questions.py         # Question handling logic  
├── questions.json       # Question database  
├── scores.json          # Saved high scores  
├── requirements.txt     # Python dependencies  
├── LICENSE              # MIT License  
├── README.md            # Project information  

## How to Run

### Run from source

1. Ensure Python 3.x is installed on your system.  
2. Clone the repository:
   git clone https://github.com/alookaparatha123/quiz---game.git  
   cd quiz---game  
3. Install dependencies:
   pip install -r requirements.txt  
4. Run the game:
   python quiz_game.py  

## Usage Notes

- Type exit() or quit() during the game to exit at any time.  
- Make sure questions.json is in the same directory as quiz_game.py when running the game.  

## License

This project is licensed under the MIT License. See the LICENSE file for details.  

## Author

Developed by Madhav.
