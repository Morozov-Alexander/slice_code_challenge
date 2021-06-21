# PizzaBot

Pizzabot is a robot that delivers pizza.

Pizzabot always starts at the origin point, (0, 0).

Therefore, given the following input string: 5x5 (1,3) (4,4) one correct solution would be: ENNNDEEEND

In other words: move east once and north thrice; drop a pizza; move east thrice and north once; drop a final pizza.

## HowTo
- Grid should consist of two numbers and be separated wit "x"
- Both numbers must be greater than zero
- Valid delivery co-ordinates should be enclosed by brackets '( )' and separated by a comma only ','
- There should be no spaces within the brackets.


## Running
To use this bot you should run python pizzabot.py with valid parameters:

`python pizzabot.py`

For example : `python pizzabot.py 5x5 (5,5) (4,4)`




## Tests

To run tests, you should run the command below.

` python test_pizzabot.py `
