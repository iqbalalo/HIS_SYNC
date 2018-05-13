CREATE TABLE his_data(
  created_on VARCHAR(25) NOT NULL
  ,updated_on VARCHAR(25) NOT NULL
  ,operation_id VARCHAR(10) NOT NULL
  ,patient_age INTEGER  NOT NULL
  ,patient_gender_code CHAR(1) NOT NULL
  ,operation_type_code VARCHAR(10) NOT NULL
  ,operation_entry_time VARCHAR(25) NOT NULL
  ,operation_leave_time VARCHAR(25) NOT NULL
  ,operation_start_time VARCHAR(25) NOT NULL
  ,operation_end_time VARCHAR(25) NOT NULL
  ,operation_room_code VARCHAR(10)  NOT NULL
  ,surgeon_code VARCHAR(10)  NOT NULL
  ,surgeon_assistant_code VARCHAR(10) 
  ,surgeon_anesthesiologist_code VARCHAR(10)  NOT NULL
  ,surgeon_scrub_nurse_code VARCHAR(10)  NOT NULL
  ,surgeon_circulating_nurse_code VARCHAR(10) NOT NULL
);
INSERT INTO his_data(created_on,updated_on,operation_id,patient_age,patient_gender_code,operation_type_code,operation_entry_time,operation_leave_time,operation_start_time,operation_end_time,operation_room_code,surgeon_code,surgeon_assistant_code,surgeon_anesthesiologist_code,surgeon_scrub_nurse_code,surgeon_circulating_nurse_code) VALUES ('2015-01-3108:55:00.000000','2015-01-3112:00:00.000000','15131085C',24,'M','K533','2015-01-3108:55:00.000000','2015-01-3112:00:00.000000','2015-01-3109:51:00.000000','2015-01-3111:48:00.000000',3,570,8834,8974,1243,'4012|');
INSERT INTO his_data(created_on,updated_on,operation_id,patient_age,patient_gender_code,operation_type_code,operation_entry_time,operation_leave_time,operation_start_time,operation_end_time,operation_room_code,surgeon_code,surgeon_assistant_code,surgeon_anesthesiologist_code,surgeon_scrub_nurse_code,surgeon_circulating_nurse_code) VALUES ('2015-01-3108:56:00.000000','2015-01-3117:40:00.000000','15131065F',56,'M','K607','2015-01-3108:56:00.000000','2015-01-3117:40:00.000000','2015-01-3110:17:00.000000','2015-01-3117:17:00.000000',6,334,8974,601,1243,'3781|');
INSERT INTO his_data(created_on,updated_on,operation_id,patient_age,patient_gender_code,operation_type_code,operation_entry_time,operation_leave_time,operation_start_time,operation_end_time,operation_room_code,surgeon_code,surgeon_assistant_code,surgeon_anesthesiologist_code,surgeon_scrub_nurse_code,surgeon_circulating_nurse_code) VALUES ('2015-01-3112:48:00.000000','2015-01-3113:57:00.000000','15131122C',88,'F','K617','2015-01-3112:48:00.000000','2015-01-3113:57:00.000000','2015-01-3113:20:00.000000','2015-01-3113:47:00.000000',3,695,601,91079,3133,'4012|');
INSERT INTO his_data(created_on,updated_on,operation_id,patient_age,patient_gender_code,operation_type_code,operation_entry_time,operation_leave_time,operation_start_time,operation_end_time,operation_room_code,surgeon_code,surgeon_assistant_code,surgeon_anesthesiologist_code,surgeon_scrub_nurse_code,surgeon_circulating_nurse_code) VALUES ('2015-01-3114:50:00.000000','2015-01-3115:56:00.000000','15131140C',81,'F','K333-3','2015-01-3114:50:00.000000','2015-01-3115:56:00.000000','2015-01-3115:15:00.000000','2015-01-3115:44:00.000000',3,695,NULL,91079,4122,'4012|');
INSERT INTO his_data(created_on,updated_on,operation_id,patient_age,patient_gender_code,operation_type_code,operation_entry_time,operation_leave_time,operation_start_time,operation_end_time,operation_room_code,surgeon_code,surgeon_assistant_code,surgeon_anesthesiologist_code,surgeon_scrub_nurse_code,surgeon_circulating_nurse_code) VALUES ('2015-01-3120:24:00.000000','2015-02-0106:16:00.000000','15131184F',71,'M','K867-2','2015-01-3120:24:00.000000','2015-02-0106:16:00.000000','2015-01-3121:55:00.000000','2015-02-0105:50:00.000000',6,334,8834,601,4012,'3492');