import web

db_host = 'localhost'
db_name = 'ferreteria_jhc'
db_user = 'ferreteria'
db_pw = 'ferreteria.2019'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    ) 