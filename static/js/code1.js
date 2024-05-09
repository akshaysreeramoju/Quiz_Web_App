var quizScore = localStorage.getItem('quizScore');
        
        // Display the score
        var scoreElement = document.getElementById('score');
        scoreElement.textContent = quizScore;
        
        // Clear the score from localStorage
        localStorage.removeItem('quizScore');