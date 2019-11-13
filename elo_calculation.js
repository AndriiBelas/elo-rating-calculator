document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#calculateButton').onclick = calculate
});

function getExpectedScore(ratingDifference){
    return 1/(1+Math.pow(10, ratingDifference/400));
}

function calculate() {
    const firstRating = document.querySelector('#firstRating').value;
    const secondRating = document.querySelector('#secondRating').value;
    const k = document.querySelector('#k').value;
    const resultSelector = document.getElementsByName('result');
    for (var i = 0, length = resultSelector.length; i < length; i++) {
        if (resultSelector[i].checked) {
            result = Number(resultSelector[i].value);
            break;
        }
    }
    let ratingDifference = secondRating-firstRating;
    let expectedScore1 = getExpectedScore(ratingDifference);
    let expectedScore2 = getExpectedScore(-ratingDifference);
    let newRating1 = Math.round(Number(firstRating) + k*(result-expectedScore1));
    let newRating2 = Math.round(Number(secondRating) + k*(1-result-expectedScore2));
    alert(`Result is ${result}. New rating for the first player is ${newRating1}, for the second player is ${newRating2}`);
}