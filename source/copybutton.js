document.addEventListener('DOMContentLoaded', function() {
    const codeBlocks = document.querySelectorAll('div.highlight pre');

    codeBlocks.forEach(block => {
        const button = document.createElement('button');
        button.className = 'copy-button';
        button.type = 'button';
        button.innerText = 'Copy';

        button.addEventListener('click', function() {
            const code = block.innerText;
            navigator.clipboard.writeText(code).then(function() {
                button.innerText = 'Copied!';
                setTimeout(() => button.innerText = 'Copy', 2000);
            });
        });

        block.parentNode.insertBefore(button, block);
    });
});
