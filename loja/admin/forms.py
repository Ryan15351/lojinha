from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):

    name = StringField('Nome Completo: ', [validators.Length(min=4, max=25)])
    username = StringField('Usuário: ', [validators.Length(min=4, max=25)])
    email = StringField('Email: ', [validators.Length(min=6, max=35)])
    password = PasswordField('Nova Senha: ',
         [validators.DataRequired(), 
         validators.EqualTo('Confirmação de senha', message='As senhas não conferem')])
    confirm = PasswordField('Repete a senha: ')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
