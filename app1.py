from flask import Flask, request, redirect

app = Flask(__name__)
@app.route('/calc/<int:num1>/<string:operation>/<int:num2>')

def calculator(num1, operation, num2):

    if operation == "-":
        result = num1 - num2
    else:  
        result = num1 + num2


    return f'{num1} {operation} {num2} = {result}'

@app.route('/search')

def search():

    query = request.args.get('q', '')

    category = request.args.get('category', 'all')

    return f'Searching for "{query}" in category: {category}'


todos = []

@app.route('/')
def list_todos():
    s = ''
    for i in todos:
        s = s + i +'<br>'
    return s


@app.route('/add/<task>')
 
def add_todo(task):
    todos.append(task)

    return redirect('/')



@app.route('/remove/<int:task_id>')

def delete_todo(task_id):
    todos.pop(task_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True) 

