from flask import Blueprint, jsonify, session, request
from app.models import User, Server, Channel, db
from app.forms import CreateServer, EditServerIcon, EditServerName
from app.forms import EditServerName
from flask_login import current_user, login_user, logout_user, login_required
from app.utils import buildServerDict


server_routes = Blueprint('servers', __name__)

def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages


@server_routes.route('/')
@login_required
def get_all_servers():
    servers = Server.query.all()
    return {'servers' : [server.to_dict()] for server in servers}

@server_routes.route('/<int:id>')
@login_required
def get_server_by_id(id):
    server = Server.query.get(id)
    if server:
        server_dict = buildServerDict(server) #! maybe include channel messages?
        return server_dict
    return {'error' : 'could not find server with that id'}

#! add new server routes here..

@server_routes.route('/', methods = ['POST'])
@login_required
def new_server():
    form = CreateServer()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit() :
        if form.data['server_icon']:
            server = Server(
                name = form.data['name'],
                owner_id = current_user.id,
                server_icon = ['server_icon']
            )
            general_channel = Channel(
                name = 'general',
                description = 'general chat',
                server_id = server.id
            )
            db.session.add(server)
            db.session.add(general_channel)
            db.session.commit()
        else:
            server = Server(
                name = form.data['name'],
                owner_id = current_user.id
            )
            general_channel = Channel(
                name = 'general',
                description = 'general chat',
                server_id = server.id
            )
            db.session.add(server)
            db.session.add(general_channel)
            db.session.commit()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401

@server_routes.route('/<int:id>/name', methods = ['PUT'])
@login_required
def edit_server_name(id):
    server = Server.query.get(id)
    form = EditServerName()
    if not server:
        return {'errors' : 'could not find server with that id'}

    if form.validate_on_submit():
        server.name = form.data['name']
        db.commit()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401

@server_routes.route('/<int:id>/server_icon', methods = ['PUT'])
@login_required
def edit_server_icon(id):
    server = Server.query.get(id)
    form = EditServerIcon()

    if not server:
        return{'errors' : 'could not find server with that id'}

    if form.validate_on_submit():
        server.name = form.data['server_icon']
        db.commit()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401

@server_routes.route('/<int:id>',methods=['DELETE'])
@login_required
def delete_server(id):
    server = Server.query.get(id)

    if server:
        db.session.delete(server)
        db.session.commit()
        return {'deletedServerId' : id}
    return {'errors' : 'server could not be found with that id'}
