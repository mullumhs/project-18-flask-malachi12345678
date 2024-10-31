from flask import Flask, render_template
app = Flask(__name__)


#base------------------------------------------------------------------------------------------------------
@app.route('/base')
def basic():

    return render_template('base.html')



#greet---------------------------------------------------------------------------------------------------
@app.route('/greet/<name>')
def greet(name):

    return render_template('greet.html', name=name)


#inventory--------------------------------------------------------------------------------------------------
@app.route('/inventory')
def inventory():

    inventory_items = ['apple', 'banana', 'cherry']

    return render_template('inventory.html', inventory=inventory_items)

#inheritance_test-------------------------------------------------------------------------------------------
@app.route('/test/<message>')

def test(message):

    return render_template('test.html', message=message)

#static_assets-----------------------------------------------------------------------------------------------
from flask import Flask, render_template, url_for



app = Flask(__name__)



@app.route('/profile/<username>')

def profile(username):

    return render_template('profile.html', username=username)



if __name__ == '__main__':

    app.run(debug=True)



#-------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    app.run(debug=True)


