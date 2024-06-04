const signInButtonLink = document.querySelector('.signInButton-link');
const signUpButtonLink = document.querySelector('.signUpButton-link');
const wrapper = document.querySelector('.wrapper');

signUpButtonLink.addEventListener('click', () =>{
    wrapper.classList.toggle('active');
});

signInButtonLink.addEventListener('click', () =>{
    wrapper.classList.toggle('active');
});

document.addEventListener('DOMContentLoaded', function() {
    const flashes = document.getElementById('flashes');
    if (flashes) {
        flashes.querySelectorAll('li').forEach(function(flash) {
            const message = flash.getAttribute('data-message');
            alert(message);
        });
    }
});