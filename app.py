from project import *
from project.authentication import *

@app.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return redirect(url_for('contacts'))



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001,debug=True,threaded=True)
