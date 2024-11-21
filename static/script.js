document.addEventListener('DOMContentLoaded', function() {
    const submitButton = document.getElementById('submit-btn');
    const resetButton = document.getElementById('reset-btn');
    const userInput = document.getElementById('user-input');
    const messageEl = document.getElementById('message');
    const gameStatus = document.getElementById('game-status');

    submitButton.addEventListener('click', function() {
        const userChoice = userInput.value;
        if (userChoice === '') {
            alert('Please enter a number');
            return;
        }

        fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: `choice=${userChoice}`
        })
        .then(response => response.json())
        .then(data => {
            messageEl.innerHTML = data.message;
            gameStatus.innerHTML = `You have ${data.attempts} attempt${data.attempts === 1 ? '' : 's'} left.`;

            if (data.attempts === 0 || data.message === "You won!") {
                submitButton.disabled = true;
                resetButton.style.display = 'inline-block';
            }
        });
    });

    resetButton.addEventListener('click', function() {
        fetch('/reset')
        .then(response => response.json())
        .then(data => {
            gameStatus.innerHTML = "You have 3 attempts to guess the correct number.";
            messageEl.innerHTML = '';
            userInput.value = '';
            submitButton.disabled = false;
            resetButton.style.display = 'none';
        });
    });
});
