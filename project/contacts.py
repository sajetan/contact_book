from project import *
from project.tables import db,Contact
from Authentication import UserAuth
#from test import *
from validate_form import *
from validate_email import validate_email

class ContactsAppShow(Resource):
    def get(self,id=None):
        '''
        Shows all the contacts in alphabetical order by name.
        Shows 10 contacts per page.
        '''
        if not session.get('logged_in'):
            flash("Please Log in")
            return redirect(url_for('index'))
        contact_data=[]
        app.logger.info('GET contacts data query')
        try:
            contact_data = Contact.query.order_by(Contact.name).paginate(per_page=10, page=id, error_out=True)
        except:
            contact_data = Contact.query.order_by(Contact.name).paginate(per_page=10, page=1, error_out=True)
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('app.html',contact_data=contact_data), 200, headers)



class ContactsAppSearch(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('search.html'), 200, headers)

    def post(self):
        '''
        Search any contact by name or email address
        '''
        if not session.get('logged_in'):
            flash("Please Log in")
            return redirect(url_for('index'))
        contact_data=None
        if 'name' in request.form.keys():
            if (request.form['name']):
                app.logger.info('Search for name [ %s ]',request.form['name'])
                contact_data = Contact.query.filter_by(name=request.form['name'])
        if 'email' in request.form.keys():
            if (request.form['email']):
                if (validate_email(request.form['email'])):
                    app.logger.info('Search for email [ %s ]',request.form['email'])
                    contact_data = Contact.query.filter_by(email=request.form['email'])
                else:
                    flash("Enter valid Email Address")

        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('search.html',contact_data=contact_data), 200, headers)




class ContactsAppDelete(Resource):
    def post(self):
        '''
        Delete the contact
        '''
        if not session.get('logged_in'):
            flash("Please Log in")
            return redirect(url_for('index'))

        try:
            contact_data = Contact.query.filter_by(id=request.form['id']).first()
            app.logger.info('Deleting contact [ %s ]',contact_data.name)
            db.session.delete(contact_data)
            db.session.commit()
            message="Deleted " +contact_data.name + "'s Contact"
            flash(message)
        except:
            db.session.rollback()
            flash('Error deleting contact.')
            app.logger.info('Error deleting contact ')
        return redirect(url_for('contacts',page=request.form['page']))


class ContactsAppEdit(Resource):
    def get(self,id):
        if not session.get('logged_in'):
            flash("Please Log in")
            return redirect(url_for('index'))
        contact_data= Contact.query.filter_by(id=id).first()
        form = ContactForm(obj=contact_data)
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('edit.html', form=form), 200, headers)

    def post(self,id):
        '''
        Edit by name/surname/email/phonenumber
        Email id is unique for the user, so throws error if email already exists in the database
        '''
        if not session.get('logged_in'):
            flash("Please Log in")
            return redirect(url_for('index'))
        pageid = request.args.to_dict()
        contact_data = Contact.query.filter_by(id=id).first()
        form = ContactForm(obj=contact_data)
        if form.validate_on_submit():
            try:
                #update to database
                form.populate_obj(contact_data)
                db.session.add(contact_data)
                db.session.commit()
                message = "Changed  " + contact_data.name + "'s Contact Details"
                app.logger.info('Edited contact [ %s ] success', contact_data.name)
                flash(message, 'success')
                return redirect(url_for('contacts',page=pageid["page"]))
            except:
                db.session.rollback()
                flash('Error updating contact. Email already exist or User not found')
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('edit.html', form=form), 200, headers)




class ContactsAppAdd(Resource):
    def get(self):
        if not session.get('logged_in'):
            flash("Please Log in")
            return redirect(url_for('index'))
        form = ContactForm()
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('add.html',form=form), 200, headers)

    def post(self):
        '''
        Add new contact with name/surname/email/phonenumber
        Email id is unique for the user, so throws error if email already exists in the database
        '''
        if not session.get('logged_in'):
            flash("Please Log in")
            return redirect(url_for('index'))
        form = ContactForm()
        if form.validate_on_submit():
            contact_data = Contact()
            form.populate_obj(contact_data)
            db.session.add(contact_data)
            try:
                # update to database
                db.session.commit()
                flash('Contact created Success')
                app.logger.info('Added a new user successfully')
                return redirect(url_for('contacts'))
            except:
                db.session.rollback()
                flash('Error Creating this contact - Email already in use')
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('add.html', form=form), 200, headers)


api.add_resource(ContactsAppShow,'/contacts','/contacts/<int:id>',endpoint="contacts")
api.add_resource(ContactsAppDelete,'/contacts/delete',endpoint="contacts_delete")
api.add_resource(ContactsAppEdit,'/edit_contact/<int:id>',endpoint="edit_contact")
api.add_resource(ContactsAppAdd,'/contact_add',endpoint="contact_add")
api.add_resource(ContactsAppSearch,'/contact_search',endpoint="contact_search")
