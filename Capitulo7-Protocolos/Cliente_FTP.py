from ftplib import *

ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())

usuario = input("Digite o usuario: ")
senha = input("Digite a senha: ")

ftp.login(usuario, senha)
print("O diretorio atual eh: ", ftp.pwd())
ftp.cwd('pub')
print("O diretorio atual eh: ", ftp.pwd())
print(ftp.retrlines('LIST'))
ftp.quit()
