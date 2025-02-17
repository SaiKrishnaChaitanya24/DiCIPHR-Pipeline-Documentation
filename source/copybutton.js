function addCopyButtons() {
    document.querySelectorAll('pre').forEach((codeBlock) => {
        let button = document.createElement('button');
        button.className = 'copy-btn';
        button.textContent = 'Copy';

        button.addEventListener('click', () => {
            let code = codeBlock.querySelector('code').textContent;
            navigator.clipboard.writeText(code).then(() => {
                alert('Code copied to clipboard!');
            });
        });

        let wrapper = document.createElement('div');
        wrapper.className = 'code-container';
        codeBlock.parentNode.insertBefore(wrapper, codeBlock);
        wrapper.appendChild(codeBlock);
        wrapper.appendChild(button);
    });
}

document.addEventListener('DOMContentLoaded', addCopyButtons);
