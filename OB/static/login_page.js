const signInButtonLink = document.querySelector('.signInButton-link');
const signUpButtonLink = document.querySelector('.signUpButton-link');
const wrapper = document.querySelector('.wrapper');

signUpButtonLink.addEventListener('click', () =>{
    wrapper.classList.toggle('active');
});

signInButtonLink.addEventListener('click', () =>{
    wrapper.classList.toggle('active');
});