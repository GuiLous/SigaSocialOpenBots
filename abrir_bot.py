import os, time
import sys

contas = [
  'userprofile01',
]

# read the code to change where is required

for i in range(0, ->bots quantity<-):
  string = '[headers]\ntitle = Config File\ncompression = yes\ncompression_level = 9\n\n[configuracoes]\nlineedit_login = yourSigaSocialEmail\nlineedit_senha = yourSigaSocialPassword\ntexteditcontas = {}\n\tinstagramPassword'.format(contas[i])
  with open('C:/Your bot Directory/user-data/database/login.ini', 'w+') as file:
    file.write(string)
  os.startfile('C:/Your Bot Directory/SCRobot-SigaSocial.exe')
  time.sleep(2)
