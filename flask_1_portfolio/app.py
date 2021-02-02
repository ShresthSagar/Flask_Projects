from flask import Flask, render_template, request, url_for, redirect
from forms import SignUPForm

app = Flask(__name__)
# app.config["TEMPLATES_AUTO_RELOAD"] = True
# app.jinja_env.auto_reload = True
# app.config["SECRET_KEY"] = 'flask_key'
# app.run(debug=True)
if __name__ == "__main__":
    app.run(debug=True)


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/about')
def about():
    return 'This is a about page'


@app.route('/blogs')
def blogs():
    return 'This is a blog page'


@app.route('/blogs/<int:blog_id>')
def blog_num(blog_id=None):
    return "This is the blog number" + str(blog_id)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUPForm()
    if form.is_submitted():
        result = request.form
        return render_template('user.html', result=result)
    return render_template('signup.html', form=form)
