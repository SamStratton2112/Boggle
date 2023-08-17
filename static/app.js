const form = document.querySelector('form');
const restartBtn = document.getElementById('restartBtn')
const $wordInput = $('.word')
let totalTime= 5
const timer = setInterval(countdown,1000)

function countdown(){
    let time = document.getElementById('countdown')
    if (totalTime === 0){
        clearInterval(timer);
        time.innerText = 'Time is up!';
        let btn = document.getElementById('submitBtn');
        btn.style.display = 'none';
        return 
    }
    totalTime -= 1;
    time.innerText = `Time left: ${totalTime}`;
}


async function submitWord(){
    let result= await axios.get('/validate', {params:{ word: $wordInput.val()}});
    let msg = result.data.result
    const msgLocation = document.getElementById('msg');
    msgLocation.innerText = msg
    const scoreLocation = document.getElementById('score')
    let score = result.data.score
    scoreLocation.innerText = `Score: ${score}`

    // submits word to server 
}




form.addEventListener('submit', function(e){
    e.preventDefault();
    //stops page refresh 
    submitWord();
    $wordInput.val('');
    // clears input field
})

restartBtn.addEventListener('submit',)




