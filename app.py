from flask import Flask, request, render_template
from crawler import crawler

app = Flask(__name__)


@app.route('/', methods=('POST', 'GET'))
def index():
    result = None
    
    if request.method == 'POST':
        result = crawler(int(request.form.get('year')),
                         int(request.form.get('month')))

    return render_template('index.html', 
                           result=result, 
                           form_data=request.form)