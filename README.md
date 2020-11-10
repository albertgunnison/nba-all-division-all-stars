# My name is Albert, and this is my final project for Harvard University's Introduction to Computer Science course.

## For this project, I was tasked to write a software application from scratch using the skills I learned in the class.

### What the program does

My web-based application allows a user to draft a fantasy basketball team with players from one of the six NBA divisions and test how many wins that team would earn if it played in the 2019-2020 NBA season.

When the user opens the application (by running it in main.py), they are greeted with a menu of all six divisions and the five teams included within. Once they choose a division, they are redirected to a page with all players in that division and their per-game averages for the five main statistical categories (points, rebounds, assists, steals, and blocks), ordered by team. They are invited to select 13 players for their new fantasy team by selecting the checkbox that accompanies each player. Once the user selects 13 players they believe will give them the best chance to win games, they scroll to the bottom and click "Finalize Your Team," which returns the approximate number of wins they would likely earn. From this point, they can click "reset" to reload the page and start the game over, or scroll to the top and click "Return" to go back to the main menu and try the game again with a different division.

### How I built it

I built this web application in Pycharm. I created the framework in an "application.py" file and made seven HTML templates (one for the homepage and six more for the divisions). For all HTML pages, I used a Bootstrap stylesheet to make my tables more aesthetically pleasing. In each of the division pages, I downloaded player performance data from Basketball Reference, which I then displayed through HTML using Python dictionaries, displayed through Jinja. To calculate the final number of wins, I summed each selected player's Win Shares metric together. If the total number of wins exceeds 82 (the number of games in an NBA season), the program returns "all 82" games rather than any number above 82.

### How to run it

Go into the terminal, run the main.py python script, and open the program up to see the main menu. Everything flows from there!
