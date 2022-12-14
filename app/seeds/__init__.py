from flask.cli import AppGroup
from .users import seed_users, undo_users
from .servers import seed_servers, undo_servers
from .channels import seed_channels, undo_channels
from .server_messages import seed_server_messages, undo_server_messages
from .permissions import seed_permissions, undo_permissions
from .server_members import seed_server_members, undo_server_members
from .dm_rooms import seed_dm_rooms, undo_dm_rooms
from .direct_messages import seed_direct_messages, undo_direct_messages

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_permissions()
    seed_servers()
    seed_server_members()
    seed_channels()
    seed_server_messages()
    seed_dm_rooms()
    seed_direct_messages()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_direct_messages()
    undo_dm_rooms()
    undo_server_messages()
    undo_channels()
    undo_server_members()
    undo_permissions()
    undo_servers()
    undo_users()
    # Add other undo functions here
