from conn import db
from sqlalchemy import *


class FlaskSyncRecord(db.Model):
    
    __tablename__ = 'sync_data'
    
    created_on = db.Column(db.String)
    updated_on = db.Column(db.String)
    operation_id = db.Column(db.String, primary_key=True)
    patient_age = db.Column(db.Integer)
    patient_gender_code = db.Column(db.String)
    operation_type_code = db.Column(db.String)
    operation_entry_time = db.Column(db.String)
    operation_leave_time = db.Column(db.String)
    operation_start_time = db.Column(db.String)
    operation_end_time = db.Column(db.String)
    operation_room_code = db.Column(db.String)
    surgeon_code = db.Column(db.String)
    surgeon_assistant_code = db.Column(db.String)
    surgeon_anesthesiologist_code = db.Column(db.String)
    surgeon_scrub_nurse_code = db.Column(db.String)
    surgeon_circulating_nurse_code = db.Column(db.String)

    def __repr__(self):
        return '<id {}, operation_id {}>'.format(self.id, self.operation_id)


class HISRecord(db.Model):

    __tablename__ = 'his_data'

    created_on = db.Column(db.String)
    updated_on = db.Column(db.String)
    operation_id = db.Column(db.String, primary_key=True)
    patient_age = db.Column(db.Integer)
    patient_gender_code = db.Column(db.String)
    operation_type_code = db.Column(db.String)
    operation_entry_time = db.Column(db.String)
    operation_leave_time = db.Column(db.String)
    operation_start_time = db.Column(db.String)
    operation_end_time = db.Column(db.String)
    operation_room_code = db.Column(db.String)
    surgeon_code = db.Column(db.String)
    surgeon_assistant_code = db.Column(db.String)
    surgeon_anesthesiologist_code = db.Column(db.String)
    surgeon_scrub_nurse_code = db.Column(db.String)
    surgeon_circulating_nurse_code = db.Column(db.String)

    def __repr__(self):
        return '<id {}, operation_id {}>'.format(self.id, self.operation_id)