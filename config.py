import web
'''
db_host = 'localhost'
db_name = 'ferreteria_jhc'
db_user = 'ferreteria'
db_pw = 'ferreteria.2019'
'''

db_host = 'd6ybckq58s9ru745.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'bh00mm9t7gfekwtx'
db_user = 'qvgg6xm7ko11cqun'
db_pw = 'y9rrmmgpbqi3ujbt'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )
    