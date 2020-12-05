import sass
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

print(os.path.join(dir_path, "assets"))

sass_file = os.path.join(dir_path, "assets", "css", "main.sass")
css_file = os.path.join(dir_path, "assets", "css", "main.css")

print(sass_file)

compiled_css = sass.compile(filename=sass_file, output_style='compressed')

with open(css_file, 'w') as cssfile:
     cssfile.write(compiled_css)