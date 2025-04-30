# Inspiration

After years of teaching math, I noticed that many students — even older ones — struggled with basic arithmetic operations.
This game was inspired by a desire to help learners practice fluently and build confidence in a fun, interactive way.

## Features

* Score tracking – Earn more points for faster answers.
  
* Timed questions – You have 10 seconds to answer each one.

* Four operations – Choose from:

Addition (+)

Subtraction (-)

Multiplication (×) (type with Alt + 0215 on Windows or Option + 8 on Mac)

Division (÷) (type with Alt + 0247)

* Two difficulty levels:

Level 1: Simple positive integers

Level 2: Includes negative numbers and more complex expressions

* Colorful feedback – Uses colorama to highlight:

Correct answers (green)

Slow answers (yellow)

Incorrect or timed-out answers (red)

* Score tracking – Earn more points for faster answers

### Requirements

- Python 3.x
- [`colorama`](https://pypi.org/project/colorama/)

#### How to Play
Run the game using:

python math_game.py
Then follow the prompts:

Choose your operation (+, -, ×, or ÷)

Select a difficulty level (1 or 2)

Answer 10 randomly generated math questions within 10 seconds each

##### Scoring System
Answer within 5 seconds: ✅ +2 points

Answer within 10 seconds: ✅ +1 point

Incorrect or timeout: ❌ 0 points

Final score is out of 20.

📁 File Structure

math_game.py     # Main game script
README.md        # Project description and instructions (this file)

🧑‍💻 Example

Which operation (+, -, ×, or ÷)? ×
Which level (1 or 2)? 1
7 × 3 = 21
Excellent! (+2 points) answered in 2.04 sec

18 × 0 = 0
Good! (+1 point) answered in 7.32 sec

12 × 8 = 
⏰ Time's up!
...
🏁 Final score: 13/20 🏁
