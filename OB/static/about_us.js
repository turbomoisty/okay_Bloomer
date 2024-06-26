document.addEventListener('DOMContentLoaded', function() {
  // Function to dynamically set the height of the header
  const header = document.querySelector("header");
  const bgImage = new Image();
  bgImage.src = ""; // Adjust the path if necessary

  bgImage.onload = function() {
      const aspectRatio = bgImage.height / bgImage.width;
      const headerWidth = header.offsetWidth;
      const headerHeight = headerWidth * aspectRatio;
      header.style.height = `${headerHeight}px`;
  };

  // Function to expand or collapse information sections
  const infoBlocks = document.querySelectorAll('.info-block');

  infoBlocks.forEach(block => {
      block.addEventListener('click', () => {
          const content = block.querySelector('p');
          content.style.display = content.style.display === 'none' ? 'block' : 'none';
      });
  });

  // Function to add background color to nav on scroll
  const navbar = document.querySelector('nav');
  window.addEventListener('scroll', function() {
      if (window.scrollY > 50) { // Adjust this value as needed
          navbar.classList.add('scrolled');
      } else {
          navbar.classList.remove('scrolled');
      }
  });
});
