from sphinx.application import Sphinx

def setup(app: Sphinx):
    app.add_js_file('static/copybutton.js')
    app.add_css_file('static/copybutton.css')
