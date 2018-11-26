#vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
from project import *
#from project.tables import db,User
from Authentication import UserAuth
from contacts import *


class UserAuthentication(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('login.html'), 200, headers)

    def post(self):
        userObj = UserAuth(request.form['username'],request.form['password'])
        res = userObj.do_authentication()
        if res:
            flash("Login Success")
            app.logger.info('Login successful')
            return redirect(url_for('contacts'))
        else:
            flash("Password entered is Invalid")
            app.logger.info('Invalid Password')
            return redirect(url_for('index'))


class UserLogout(Resource):
    def get(self):
        session['logged_in'] = False
        app.logger.info('Logout successful')
        return redirect(url_for('index'))



'''
#test 

@auth.error_handler
def unauthorized():
    return make_response(jsonify( { 'error': 'Unauthorized access!!!' } ), 403)

@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    print('Authenticating..')
    user = User.verify_auth_token(username_or_token)
    #return True
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(username = username_or_token).first()

    g.user = user
    print('Authentication successful')
    return True

@app.route('/api/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(600)
    return jsonify({'token': token.decode('ascii'), 'duration': 600})
'''

api.add_resource(UserAuthentication, '/login',endpoint="login")
api.add_resource(UserLogout, '/logout',endpoint="logout")


