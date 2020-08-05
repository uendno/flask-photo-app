from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db():
    db.create_all()


def clear_db():
    db.drop_all()


def insert_test_data():
    file = open('tests/test_data.sql', 'r')
    sql_data = file.read()
    file.close()

    sql_commands = sql_data.split(';')
    for command in sql_commands:
        try:
            db.session.execute(command)
            db.session.commit()
        except Exception as err:
            print(err)
