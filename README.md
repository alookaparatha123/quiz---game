# 📝 Python Quiz Game

A simple console-based quiz game built using Python. Supports:
✅ Multiple-choice questions
✅ True/False questions
✅ Open-ended questions
✅ Multiple rounds (5 rounds, 10 questions each)
✅ Score and accuracy tracking
✅ Saves leaderboard

---

## 🚀 How to Run

### 🐍 Run from Python source:

1️⃣ Make sure Python 3.x is installed.
2️⃣ Clone this repo:

```bash
git clone https://github.com/alookaparatha123/quiz-game.git
cd quiz-game
```

3️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

4️⃣ Run the game:

```bash
python quiz_game.py
```

---

### 💻 Run executable (Windows)

If you downloaded the `.exe`:

* Extract the zip file.
* Make sure `quiz_game.exe` and `questions.json` are in the same folder.
* Double-click `quiz_game.exe`.

---

## 📂 Project Structure

```
quiz-game/
├── quiz_game.py         # Main game script
├── questions.json       # Questions database
├── scores.json          # Saved scores
├── requirements.txt     # Python dependencies
├── README.md            # This file
```

---

## 🛠 Build executable yourself

You can use PyInstaller:

```bash
pyinstaller --onefile quiz_game.py
```

The executable will be in `dist/`.

---

## 📌 Notes

⚠ Keep `questions.json` with your executable!
⚠ Type `exit()` or `quit()` during the game to quit anytime.

---

## 📬 License

MIT License

https://github.com/alookaparatha123/quiz---game