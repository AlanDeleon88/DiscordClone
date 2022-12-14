from .db import db
from datetime import datetime

class DmRoom(db.Model):
    __tablename__= 'dm_rooms'
    id = db.Column(db.Integer, primary_key=True)
    user1_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user2_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user1_active = db.Column(db.Boolean, default=False)
    user2_active = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    user_one = db.relationship('User', foreign_keys=[user1_id], back_populates='dm_left')
    user_two = db.relationship('User', foreign_keys=[user2_id], back_populates='dm_right')

    direct_messages = db.relationship('DirectMessage',back_populates = 'dm_rooms')

    def to_dict(self):
        return{
            'id': self.id,
            'user1_id' : self.user1_id,
            'user2_id' : self.user2_id,
            'direct_messages' : [{'id': message.id, 'sender_id' : message.sender_id, 'body' : message.body, 'img' : message.img} for message in self.direct_messages]
        }
