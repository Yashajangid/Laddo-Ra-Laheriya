document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById('language-toggle');

    toggleButton.addEventListener('click', function () {
        const englishElements = document.querySelectorAll('.lang[data-lang="en"]');
        const hindiElements = document.querySelectorAll('.lang[data-lang="hi"]');

        englishElements.forEach(el => {
            el.style.display = (el.style.display === 'none' || el.style.display === '') ? 'inline' : 'none';
        });

        hindiElements.forEach(el => {
            el.style.display = (el.style.display === 'none' || el.style.display === '') ? 'inline' : 'none';
        });
    });
});
