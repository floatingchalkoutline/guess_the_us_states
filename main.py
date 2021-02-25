import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guess_list = []
incomplete = True
current_score = 0
with open("current_score.txt", mode="w") as scoreboard:
    scoreboard.write(str(current_score))
# USE A LOOP TO ALLOW THE USER TO KEEP GUESSING
while incomplete:
    # CONVERT THE GUESS TO TITLE CASE
    answer_state = (screen.textinput(title=f"Score: {current_score}/50", prompt="What's another state's name?")).title()
    # CHECK IF THE GUESS IS AMONG THE 50 STATES
    states_data = pandas.read_csv("50_states.csv")
    states_list = states_data.state.to_list()
    # IF THE USER ENTERS THE WORD "EXIT", WRITE ALL THE STATES THEY MISSED INTO ANOTHER CSV CALLED STATES_TO_LEARN.CSV
    if answer_state == "Exit":
        missed = []
        for state in states_list:
            if state not in guess_list:
                missed.append(state)
        missed_states = pandas.DataFrame(missed)
        missed_states.to_csv("states_to_learn.csv")
        break
    # IF THE USER GETS A CORRECT GUESS, DO THE FOLLOWING
    if answer_state in states_list and answer_state not in guess_list:
        # WRITE THE CORRECT GUESSES ON THE MAP
        state_row = states_data[states_data.state == answer_state]
        label = turtle.Turtle()
        label.hideturtle()
        label.penup()
        label.goto(int(state_row.x), int(state_row.y))
        label.write(f"{answer_state}", move=False, align="center")
        # RECORD THE CORRECT GUESSES IN A LIST
        guess_list.append(answer_state)
        # KEEP TRACK OF THE SCORE IN THE PROMPT
        current_score += 1
        with open("current_score.txt", mode="w") as scoreboard:
            scoreboard.write(f"{current_score}")
        if current_score == 50:
            game_over = turtle.Turtle()
            game_over.penup()
            game_over.goto(0, 250)
            game_over.hideturtle()
            game_over.write("YOU WIN! NICE JOB!", move=False, align="center", font=("Arial", 30, "normal"))
            incomplete = False

screen.exitonclick()



