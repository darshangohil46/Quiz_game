# Quiz Game README

## Introduction
This Python-based quiz game allows users to register, login, play quizzes on various topics, view scores, and exit the game. It utilizes MySQL for database management and consists of several modules including `score` and `play_quiz`.

## Features
- **Registration**: Users can register by providing their username, password, phone number, and email.
- **Login**: Registered users can log in using their credentials.
- **Quiz Playing**: Users can choose from various quiz categories including Mythology, Sports, History, Movies, and General Knowledge.
- **Score Viewing**: Users can view their scores as well as scores for specific quiz categories or the total score.
- **MySQL Database**: The game utilizes MySQL database for storing user information and scores.

## Modules

### score.py
- **ScoreList Class**: Manages the scores for individual users.
- **AllPlayersScore Class**: Retrieves and displays scores for all players or scores for specific quiz categories.

### play_quiz.py
- **Play_quiz Class**: Handles the quiz-playing functionality including selecting quiz categories and displaying questions.

## Usage
1. Run the main script `quiz_game.py`.
2. Choose from the options provided:
    - **Login**: Existing users can login to play quizzes and view scores.
    - **Register**: New users can register to create an account.
    - **View Score List**: Users can view their scores or scores for specific quiz categories.
    - **Exit**: Terminate the application.

## Dependencies
- **Python 3.x**
- **MySQL Connector Python**: Required for connecting to MySQL database.

## Setup
1. Install Python 3.x on your system if not already installed.
2. Install MySQL Connector Python using `pip install mysql.connector`.

## Database Configuration
- Ensure MySQL server is running.
- Modify the database connection parameters in the `quiz_game.py` script according to your MySQL server configuration.

## Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to create an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
