function flipAnswer(identifier, num, answer) {
    var btn = document.getElementById(identifier);
    if (btn.innerHTML == answer)
    {
        btn.innerHTML = num;
    }
    else {
        btn.innerHTML = answer;
    }
}

function addWrongAnswer(identifier) {
    var xBox = document.getElementById(identifier);
    xBox.innerHTML = xBox.innerHTML + "X";
}

function addScore(identifier, questionNumber) {
    var scoreBox = document.getElementById(identifier);

    var amountToAdd = 0;
    for (i = 0; i <= 4; i++) {
    //for (i = 1; i <= 5; i++) {
      var inner = document.getElementById("answer" + questionNumber + "-" + i).innerHTML;

      if (!inner.match(/^\d/)) {
        var val = parseInt(inner.match(/\d+/));
        if (val != null) {
          amountToAdd += val;
        }
      }
    }

    scoreBox.innerHTML = parseInt(scoreBox.innerHTML) + amountToAdd;
}

function showFirstQuestion() {
    var start = document.getElementById("start");
    var firstQuestion = document.getElementById("question0");
    start.style["display"] = 'none';
    firstQuestion.style["display"] = 'block';
}

function showNextQuestion(prevQuestionNumber) {
    hideAndShow("question" + prevQuestionNumber, "question" + (parseInt(prevQuestionNumber) + 1))

    var prevTeam1Score = parseInt(document.getElementById("team1Score" + prevQuestionNumber).innerHTML);
    var prevTeam2Score = parseInt(document.getElementById("team2Score" + prevQuestionNumber).innerHTML);
    document.getElementById("team1Score" + (parseInt(prevQuestionNumber) + 1)).innerHTML = prevTeam1Score;
    document.getElementById("team2Score" + (parseInt(prevQuestionNumber) + 1)).innerHTML = prevTeam2Score;
}

function showWinner(prevQuestionNumber) {
    hideAndShow("question" + prevQuestionNumber, "congrats")

    var prevTeam1Score = parseInt(document.getElementById("team1Score" + prevQuestionNumber).innerHTML);
    var prevTeam2Score = parseInt(document.getElementById("team2Score" + prevQuestionNumber).innerHTML);

    if (prevTeam1Score > prevTeam2Score) {
      document.getElementById("finalTeam2Score").style["display"] = 'none';
    }
    else if (prevTeam1Score < prevTeam2Score){
      document.getElementById("finalTeam1Score").style["display"] = 'none';
    }
    else {
      // Indicate the tie and change the box to a neutral color.
      document.getElementById("finalTeam1Score").innerHTML = "It's a Tie!";
      document.getElementById("finalTeam1Score").style["background-color"] = "#B3000C";
      document.getElementById("finalTeam1Score").style["border-color"] = "#DC3D2A";
      // Hide the second box.
      document.getElementById("finalTeam2Score").style["display"] = 'none';
    }
}

function hideAndShow(identifier1, identifier2) {
    document.getElementById(identifier1).style["display"] = 'none';
    document.getElementById(identifier2).style["display"] = 'block';
}
