# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'DiCIPHR-Pipeline-Documentation'
copyright = '2025, Drew Parker and Sai Krishna Chaitanya Annavazala'
author = 'Drew Parker and Sai Krishna Chaitanya Annavazala'
release = '1.0.0'
master_doc = 'index'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_copybutton',  # Add sphinx_copybutton extension
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

def setup(app):
    app.add_js_file('copybutton.js')  # Link your JavaScript file
    app.add_css_file('styles.css')    # Link your CSS file

# Optionally, customize the copybutton extension's behavior
copybutton_prompt_text = ">>> "
