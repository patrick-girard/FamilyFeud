# Imports
import re

# Constants
closingDivString = "</div>\n"


# READ THE INFILE
with open("input.txt", encoding='utf8') as f:
    lines = f.readlines()

questions = list()
answers = list() # this will actually be a 2D list later.

for line in lines:
    question = re.findall('(?<=Question:).+', line) # technically a list of all matches is returned
    answer = re.findall('(?<=Answer:).+', line) # technically a list of all matches is returned

    # If the line is a question, add the question.
    if len(question) != 0:
        questions.append(question[0].lstrip().replace("'", ""))

    # If the line is a answer, add the answer.
    elif len(answer) != 0:
        # If adding answers for a new question, first append a list to add the answers to.
        if len(answers) < len(questions):
            answers.append(list())

        # Append the answers to the list of answers for the question.
        answers[len(questions) - 1].append(answer[0].lstrip().replace("'", ""))


# WRITE THE OUTFILE.
outfile = open("familyFued.html", "w", encoding="utf8")

# Write the heading stuff.
headingString = """<!DOCTYPE html>
<html>
\t<head>
\t\t<script src="scripts.js"></script>
\t</head>
\t<meta name="viewport" content="width=device-width, initial-scale=1">
\t<link rel="stylesheet" href="styles.css">

\t<body>
\t\t<div id=start class="container">
\t\t\t<div class="title">Family Feud</div>

\t\t\t<ol>
\t\t\t\t<li>Divide into 2 teams and select Team Captains.</li>
\t\t\t\t<li>The host will read the question and the player who hits the buzzer first has to immediately give an answer.</li>
\t\t\t\t<li>If the first player fails to give a correct answer, the other team player gets 5 seconds to guess a correct answer.</li>
\t\t\t\t<li>The team whose Captain gives a correct answer first gets the chance to play this round of the game OR they can pass the chance to play the round to the opposing team.</li>
\t\t\t\t<li>The team who chooses to play this round gets a chance to guess the remaining top answers to the question. Each team member (no help from the team) gets a chance to give an answer, one by one, until they've found all the answers or gotten three wrong answers (called strikes).</li>
\t\t\t\t<li>When the team has three strikes, the second team gets one chance to give one of the top answers to the question (team can collaborate). If they succeed, they will steal all of the other team's points from that round and win the round. If the opposing team fails, the first team keeps their points for that round.</li>
\t\t\t\t<li>The game ends when one of the competing teams earns 300 points.</li>
\t\t\t</ol>

\t\t\t<button class="next" style="float: right;" onclick="showFirstQuestion()">Let's Get Started!</button>
\t\t</div>\n
"""
outfile.write(headingString)

# Write the start.

# Write all the questions and answers.
for question_index, question in enumerate(questions):

    containerDivString = """\t\t<div id=question{} class="container" style="display: none;">\n""".format(question_index)
    questionDivString = """\t\t\t<div class="question">{}. {}</div>\n""".format((question_index + 1), question)

    outfile.write(containerDivString)
    outfile.write(questionDivString)

    for answer_index, answer in enumerate(answers[question_index]):

        answerButtonString = """\t\t\t\t<button id="answer{}-{}" class="answer" onclick="flipAnswer('answer{}-{}', {}, '{}')">{}</button>\n""".format(question_index, answer_index, question_index, answer_index, (answer_index + 1), answer, (answer_index + 1))
        outfile.write(answerButtonString)

    gridContainerDivString = "\t\t\t\t<div class=grid-container>\n"
    wrongAnswerButtonString = """\t\t\t\t\t<button id=wrongAnswers{} class="wrongAnswers" onclick="addWrongAnswer('wrongAnswers{}')">&nbsp;</button>\n""".format(question_index, question_index)
    team1ScoreButtonString = """\t\t\t\t\t<button id=team1Score{} class="score" onclick="addScore('team1Score{}', {})">0</button>\n""".format(question_index, question_index, question_index)
    team2ScoreButtonString = """\t\t\t\t\t<button id=team2Score{} class="score2" onclick="addScore('team2Score{}', {})">0</button>\n""".format(question_index, question_index, question_index)
    nextQuestionButtonString = """\t\t\t\t\t<button class="next" onclick="showNextQuestion({})">Show Next Question</button>\n""".format(question_index)
    showWinnerString = """<button class="next" onclick="showWinner({})">Show Winner</button>\n""".format(question_index)

    outfile.write(gridContainerDivString)
    outfile.write(wrongAnswerButtonString)
    outfile.write(team1ScoreButtonString)
    outfile.write(team2ScoreButtonString)
    # If this is not the last question, write the next question button.
    if question_index != len(questions) - 1:
        outfile.write(nextQuestionButtonString)
    # Otherwise, this is the last question, so write the show winner button.
    else:
        outfile.write(showWinnerString)

    outfile.write("\t\t\t\t" + closingDivString)
    outfile.write("\t\t" + closingDivString)
    outfile.write('\n')

# Write the winner.
winnerString = """\t\t<div id=congrats class="container" style="display: none;">
\t\t\t<div id=finalTeam1Score class="score">The Winner is Team 1!</div>
\t\t\t<div id=finalTeam2Score class="score2">The Winner is Team 2!</div>
\t\t</div>\n"""
outfile.write(winnerString)

# Write the closing stuff.
closingString = """\t</body>\n</html>"""
outfile.write(closingString)
