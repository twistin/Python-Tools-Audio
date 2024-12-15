
# pip install nbconvert


import nbformat
from nbconvert import HTMLExporter

# Cargar el notebook
notebook_filename = 'iterate-like-a-grandmaster.ipynb'
with open(notebook_filename) as f:
    notebook_content = nbformat.read(f, as_version=4)

# Crear un exportador HTML
html_exporter = HTMLExporter()

# Convertir el notebook a HTML
(body, resources) = html_exporter.from_notebook_node(notebook_content)

# Guardar el HTML en un archivo
html_filename = notebook_filename.replace('.ipynb', '.html')
with open(html_filename, 'w') as f:
    f.write(body)

print(f"El notebook ha sido convertido a HTML y guardado como {html_filename}")

