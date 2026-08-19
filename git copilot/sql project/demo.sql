CREATE TABLE students (
    id NUMBER PRIMARY KEY,
    name VARCHAR2(50),
    age NUMBER
);

CREATE TABLE student_audit (
    audit_id NUMBER GENERATED AS IDENTITY PRIMARY KEY,
    student_id NUMBER,
    action_type VARCHAR2(20),
    old_name VARCHAR2(50),
    old_age NUMBER,
    action_date TIMESTAMP DEFAULT SYSTIMESTAMP
);

CREATE OR REPLACE TRIGGER trg_students_audit
AFTER INSERT OR UPDATE OF name, age OR DELETE ON students
FOR EACH ROW
BEGIN
    IF INSERTING THEN
        INSERT INTO student_audit (student_id, action_type, old_name, old_age)
        VALUES (:NEW.id, 'INSERT', :NEW.name, :NEW.age);
    ELSIF UPDATING THEN
        INSERT INTO student_audit (student_id, action_type, old_name, old_age)
        VALUES (:OLD.id, 'UPDATE', :OLD.name, :OLD.age);
    ELSIF DELETING THEN
        INSERT INTO student_audit (student_id, action_type, old_name, old_age)
        VALUES (:OLD.id, 'DELETE', :OLD.name, :OLD.age);
    END IF;
END;
/

INSERT INTO students VALUES (1, 'Vasil', 20);
INSERT INTO students VALUES (2, 'Ahmed', 21);

SELECT * FROM students;

DELETE FROM students WHERE id = 2;

SELECT * FROM students;
SELECT * FROM student_audit;