document.addEventListener('DOMContentLoaded', function() {
    // Function to expand or collapse information sections
    const infoBlocks = document.querySelectorAll('.info-block');

    infoBlocks.forEach(block => {
        block.addEventListener('click', () => {
            const content = block.querySelector('p');
            content.style.display = content.style.display === 'none' ? 'block' : 'none';
        });
    });
});
