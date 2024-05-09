
function calculateScore() {
    // Calculate the score
    var score = 0;
    // Calculate the score logic here

    // Question 1
    var q1Answer = document.querySelector('input[name="q1"]:checked');
    if (q1Answer !== null && q1Answer.value === "3") {
        score++;
    }

    // Question 2
    var q2Answer = document.querySelector('input[name="q2"]:checked');
    if (q2Answer !== null && q2Answer.value === "2") {
        score++;
    }

    // Question 3
    var q3Answer = document.querySelector('input[name="q3"]:checked');
    if (q3Answer !== null && q3Answer.value === "2") {
        score++;
    }

    // Store the score in localStorage
    localStorage.setItem('quizScore', score);

    // Submit the form to the Flask route
    document.getElementById('quiz-form').submit();
}

// Retrieve the score from localStorage and populate the hidden input field
var quizScore = localStorage.getItem('quizScore');
document.getElementById('quiz-score-input').value = quizScore;
