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


#contact_form-------------------------------------------------------------------------------------------------
from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)



@app.route('/contact', methods=['GET', 'POST'])

def contact():

    if request.method == 'POST':

        name = request.form['name']

        email = request.form['email']

        message = request.form['message']

        # Here you would typically save this data or send an email

        return redirect(url_for('thankyou', name=name, message=message))

    return render_template('contact.html')



@app.route('/thankyou')

def thankyou():

    name = request.args.get('name')

    message = request.args.get('message')

    return render_template('thankyou.html', name=name, message=message)

#-------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    app.run(debug=True)


