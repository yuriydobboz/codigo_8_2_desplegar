import os

SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
PWD = os.path.abspath(os.curdir)

DEBUG = True # En despliegue esto pasa a FALSE

#SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dbase.db'.format(PWD)
#SQLALCHEMY_TRACK_MODIFICATIONS = False

# Ejemplo basico de postgresql
# Comparalo con ejemplo de Mysql
#SQLALCHEMY_DATABASE_URI= 'postgresql+psycopg2://root:password@localhost/base_datos'
SQLALCHEMY_DATABASE_URI= 'postgresql://yuriydobboz:PyspvIrehAVI7Sd3IWrOF7L3cJlSz2we@dpg-cu1rho56l47c73a6goc0-a.oregon-postgres.render.com/db_despligue_8_2_b2m6'
SQLALCHEMY_TRACK_MODIFICATIONS=False

