from conn import db
from sync.model import FlaskSyncRecord, HISRecord
from flask import Blueprint, render_template, jsonify
import sqlalchemy.ext.declarative

# Initiate blueprint
sync_blueprint = Blueprint('sync', __name__, template_folder='templates', url_prefix="/sync")

# HIS db server connection
his_conn = db.create_engine("postgresql+psycopg2://postgres:His123@127.0.0.1:5434/his_db", echo=True)
Session = sqlalchemy.orm.sessionmaker(bind=his_conn)


def data_from_his_server():
    session = Session()
    records = session.query(HISRecord)
    return records


def data_from_app_server():
    records = db.session.query(FlaskSyncRecord)
    return records

    
# Routes
@sync_blueprint.route('/', methods=['GET'])
def get():
    return render_template('home.html', his_records=data_from_his_server(), app_records=data_from_app_server())
    
    
@sync_blueprint.route('/', methods=['POST'])
def sync():
    
    msg = ""
    app_records = FlaskSyncRecord.query.all()
    
    if len([r.operation_id for r in app_records]) > 0:
    
        # Get flask app records
        app_records = FlaskSyncRecord.query.all()
        app_operation_ids = [r.operation_id for r in app_records]
        app_created_ons = [r.created_on for r in app_records]
        app_updated_ons = [r.updated_on for r in app_records]
    
        # Get HIS updated records
        his_session = Session()
        filtered_records = his_session.query(
            HISRecord
        ).filter(HISRecord.operation_id.in_(app_operation_ids)) \
            .filter(HISRecord.created_on.in_(app_created_ons)) \
            .filter(~HISRecord.updated_on.in_(app_updated_ons))
    
        # Sync new records
        for fr in filtered_records:
            r = FlaskSyncRecord.query.filter_by(operation_id=fr.operation_id).first()
            r.created_on = str(fr.created_on)
            r.updated_on = str(fr.updated_on)
            r.operation_id = str(fr.operation_id)
            r.patient_age = int(fr.patient_age)
            r.patient_gender_code = str(fr.patient_gender_code)
            r.operation_type_code = str(fr.operation_type_code)
            r.operation_entry_time = str(fr.operation_entry_time)
            r.operation_leave_time = str(fr.operation_leave_time)
            r.operation_start_time = str(fr.operation_start_time)
            r.operation_end_time = str(fr.operation_end_time)
            r.operation_room_code = str(fr.operation_room_code)
            r.surgeon_code = str(fr.surgeon_code)
            r.surgeon_assistant_code = str(fr.surgeon_assistant_code)
            r.surgeon_anesthesiologist_code = str(fr.surgeon_anesthesiologist_code)
            r.surgeon_scrub_nurse_code = str(fr.surgeon_scrub_nurse_code)
            r.surgeon_circulating_nurse_code = str(fr.surgeon_circulating_nurse_code)
            db.session.commit()
    
        msg = str(len([r for r in filtered_records])) + " records have been updated!"
    
        # Get HIS new records
        his_session = Session()
        filtered_records = his_session.query(
            HISRecord
        ).filter(~HISRecord.operation_id.in_(app_operation_ids))
    
        # Sync new records
        for fr in filtered_records:
            r = FlaskSyncRecord()
            r.created_on = str(fr.created_on)
            r.updated_on = str(fr.updated_on)
            r.operation_id = str(fr.operation_id)
            r.patient_age = int(fr.patient_age)
            r.patient_gender_code = str(fr.patient_gender_code)
            r.operation_type_code = str(fr.operation_type_code)
            r.operation_entry_time = str(fr.operation_entry_time)
            r.operation_leave_time = str(fr.operation_leave_time)
            r.operation_start_time = str(fr.operation_start_time)
            r.operation_end_time = str(fr.operation_end_time)
            r.operation_room_code = str(fr.operation_room_code)
            r.surgeon_code = str(fr.surgeon_code)
            r.surgeon_assistant_code = str(fr.surgeon_assistant_code)
            r.surgeon_anesthesiologist_code = str(fr.surgeon_anesthesiologist_code)
            r.surgeon_scrub_nurse_code = str(fr.surgeon_scrub_nurse_code)
            r.surgeon_circulating_nurse_code = str(fr.surgeon_circulating_nurse_code)
            db.session.add(r)
        db.session.commit()
    
        msg = msg + " " + str(len([r for r in filtered_records])) + " records have been inserted!"
        return msg
    else:
        # If no records in app server db insert all
        result = his_conn.execute("Select * From his_data")

        for _r in result:
            r = FlaskSyncRecord()
            r.created_on = str(_r["created_on"])
            r.updated_on = str(_r["updated_on"])
            r.operation_id = str(_r["operation_id"])
            r.patient_age = int(_r["patient_age"])
            r.patient_gender_code = str(_r["patient_gender_code"])
            r.operation_type_code = str(_r["operation_type_code"])
            r.operation_entry_time = str(_r["operation_entry_time"])
            r.operation_leave_time = str(_r["operation_leave_time"])
            r.operation_start_time = str(_r["operation_start_time"])
            r.operation_end_time = str(_r["operation_end_time"])
            r.operation_room_code = str(_r["operation_room_code"])
            r.surgeon_code = str(_r["surgeon_code"])
            r.surgeon_assistant_code = str(_r["surgeon_assistant_code"])
            r.surgeon_anesthesiologist_code = str(_r["surgeon_anesthesiologist_code"])
            r.surgeon_scrub_nurse_code = str(_r["surgeon_scrub_nurse_code"])
            r.surgeon_circulating_nurse_code = str(_r["surgeon_circulating_nurse_code"])
            db.session.add(r)

        db.session.commit()

        return "All records have been inserted!"
    