#%%

from flask import Flask, send_from_directory

app = Flask("serving_static_files")

# 1. create a route that serves the file html/index.html in the base path
# 2. create another route that serves the css/index.css in the /css/index.css path
# 3. modify the HTML file to link to the css file

app.run()
# %%






