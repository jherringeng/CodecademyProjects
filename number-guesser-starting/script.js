let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:
generateTarget = () => {
  return Math.floor(Math.random() * 10);
}

compareGuesses = (userGuess, compGuess, targetNum) => {

  let userDiff = Math.abs(targetNum - userGuess);
  let compDiff = Math.abs(targetNum - compGuess);

  if (userDiff <= compDiff) {
    return true;
  } else {
    return false;
  }
}

updateScore = (winner) => {
  if (winner === "human") {
    humanScore++;
  } else if (winner === "computer") {
    computerScore++;
  } else {
    console.log("Winner not recognised")
  }
}

advanceRound = () => {
  currentRoundNumber++;
}
