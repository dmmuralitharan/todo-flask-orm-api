class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:''@localhost/test_todo_orm_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False