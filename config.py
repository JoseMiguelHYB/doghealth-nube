class Config:
    SECRET_KEY = 'tu_secreto_aqui'
    #SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:miguel123@localhost/doghealth'
    #SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://u6bxjkv8ymamom98:MoaBebmwKrKWZc5D9dUZ@b0owcdtabmtqehtscyph-mysql.services.clever-cloud.com/b0owcdtabmtqehtscyph'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://u6bxjkv8ymamom98:MoaBebmwKrKWZc5D9dUZ@b0owcdtabmtqehtscyph-mysql.services.clever-cloud.com:3306/b0owcdtabmtqehtscyph'   
    SQLALCHEMY_TRACK_MOD0IFICATIONS = False

    SECURITY_RECOVERABLE = True  # Habilita la recuperación de contraseñas
    SECURITY_SEND_PASSWORD_RESET_NOTICE_EMAIL = False  # Si quieres notificar después de cambiar la contraseña
    SECURITY_EMAIL_SENDER = 'no-reply@tudominio.com'  # Correo que se usará para enviar los emails
    SECURITY_MSG_PASSWORD_RESET = ('Instrucciones para restablecer tu contraseña han sido enviadas a tu correo.', 'success')
