const firstName = document.querySelector('#firstName').value;
const lastName = document.querySelector('#lastName').value;
const age = document.querySelector('#age').value;
const height = document.querySelector('#height').value;
const petName = document.querySelector('#petName').value;


let buttonInput = document.querySelector('#checkSpy');

buttonInput.addEventListener('click', () => {
    event.preventDefault();

    if (firstName === 'Jose' && lastName === 'Johnson' && 20 < age < 30 && height > 170 && petName === 'Sammy') {
        console.log('Welcome, Agent Jose.')
    } else {
        console.log(`Greetings, ${firstName}${lastName }!`)
    }
})