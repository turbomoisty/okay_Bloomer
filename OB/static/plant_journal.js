document.addEventListener('DOMContentLoaded', () => {
    const saveEntryButton = document.getElementById('save-entry');
    const backToPlantButton = document.getElementById('back-to-plant');

    saveEntryButton.addEventListener('click', () => {
        const journalText = document.getElementById('journal-text').value;
        const imageUpload = document.getElementById('image-upload').files[0];

        // Logic to save the journal entry and uploaded image
        console.log('Journal Entry:', journalText);
        console.log('Image Upload:', imageUpload);
    });

    backToPlantButton.addEventListener('click', () => {
        window.history.back();
    });
});
