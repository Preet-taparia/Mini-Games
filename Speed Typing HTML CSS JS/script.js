const quoteDisplayElement = document.getElementById("quoteDisplay");
const quoteInputElement = document.getElementById("quoteInput");
const timerElement = document.getElementById("timer");

quoteInputElement.addEventListener('input', ()=>{
    const arrayQuote = quoteDisplayElement.querySelectorAll("span");
    const arrayValue = quoteInputElement.value.split("");

    let correct = true;

    arrayQuote.forEach((characterSpan, index) => {
        const character = arrayValue[index];
        if(character == null){
            characterSpan.classList.remove("correct");
            characterSpan.classList.remove("incorrect");
            correct = false;
        }
        else if(character === characterSpan.innerText){
            characterSpan.classList.add("correct");
            characterSpan.classList.remove("incorrect");
        }else{
            characterSpan.classList.remove("correct");
            characterSpan.classList.add("incorrect");
            correct = true
        }
    })
    if(correct){
        newQuote();
    }
});

async function randomQuote() {
  return fetch("https://api.quotable.io/random")
    .then((response) => response.json())
    .then((data) => data.content);
};

async function newQuote() {
  const quote = await randomQuote();
  console.log(quote);
  quoteDisplayElement.innerText = ""; 
  quote.split("").forEach(character => {
    const characterSpan = document.createElement('span');
    
    characterSpan.innerText = character
    quoteDisplayElement.appendChild(characterSpan)
  });
  quoteInputElement.value = null
  startTimer()
};

let startTime ;
function startTimer(){
    timerElement.innerText = 0;
    startTime = new Date()
    setInterval(()=>{
        timerElement.innerText = getTimertime()
    }, 1000)
    
}

function getTimertime(){
    return Math.floor((new Date() - startTime) / 1000)
}


newQuote();
