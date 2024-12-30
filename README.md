# 🐍 Blind Snake: Comparative Analysis of Heuristics

Blind Snake is a standard game of snake chasing an apple - but without you knowing the position, nor the size of the map! <br>
The project was originally created as a part of JetBrains Student Internship application.

Date of creation: December, 2024

# 📄 Read the paper!!!
TODO

# ⚙️ Implementation details
The project has a very simple structure.

## 💻 Code
`Board` represent a current game board. It contains `width`, `height`, and the position of the `snake` and `apple`. <br>
It also contains the moving logic, i.e. the `send_move` method, moving the snake in respective direction (`UP`, `DOWN`, `LEFT`, `RIGHT`).

`Strategy` represents a class that others, concrete strategies, inherit from. It contains initalization method, and also `sample_move()` and `reset()` methods, which are used for move generation and refreshing the strategy, in case of sweeping. <br>
Strategies receive previous moves, so that the more complex ones, such as coiling, can be implemented.

`Engine` object is loaded once and is used to play the game. It contains the `strategy` currently being played, and the `board` played on. <br>
Engine can change the strategies if needed, using the `load_strategy()` method, and it should, for optimal performance, use `load_board()` to load different board, i.e. there is no need to create engine for each game, but just load a new game into the engine. <br>
To simulate a game, it is sufficient to set a strategy and a board, and then call `simulate()` method, which will take care of the rest of the logic.

## 📊 Experimentation
To run a single game, `simulate_board.py` is used, with a respective script. However, to run large scale experimentation, the sweeper is implemented, namely in `sweep_boards.py`, which takes into consideration maximum width and height, and then runs for each possible dimension combination a certain number of `shots`, to make the statistical analysis credible. Keep in mind that overlaps may happen (i.e. the same game played several times), but the shots are randomly generated each time, so that also provides the statistical benefit.

To run experiments, it is possible to set up bash scripts running both of the files. By calling `sweep_boards.py`, the sweeping is independently performed of the `simulate_board.py` file.
