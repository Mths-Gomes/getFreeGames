import pyautogui as rb
import time

from services.sendConfirmationPrintService import sendConfirmationPrint

rb.PAUSE = 1

link = 'https://www.epicgames.com/store/pt-BR/free-games'
# link = 'https://www.epicgames.com/store/pt-BR/'

def getOneFreeGames():
  # Abre o chrome
  rb.press('winleft')
  rb.write('chrome')
  rb.press('enter')

  #Seleciona user browser
  # time.sleep(3)
  # rb.click(1017,570)

  #Nova guia e direcionamento Epic Store
  rb.hotkey('ctrl', 't')
  rb.write(link)
  rb.press('enter')

  #Clica no banner de game gratis
  time.sleep(7)
  rb.click(386, 523)

  # Pop-up +18
  time.sleep(5)
  rb.click(688, 469)

  #Clica em obter
  time.sleep(6)
  rb.click(1072, 557)

  # #Confirma a "compra"
  time.sleep(6)
  rb.click(1014, 692)

  #Fecha card de agradecimento
  time.sleep(6)
  rb.click(945, 118)

  sendConfirmationPrint()

def getTwoFreeGames():
  rb.press('winleft')
  rb.write('chrome')
  rb.press('enter')

  #Seleciona user browser
  # time.sleep(3)
  # rb.click(1017,570)

  #Nova guia e direcionamento Epic Store
  rb.hotkey('ctrl', 't')
  rb.write(link)
  rb.press('enter')

  #Clica no banner de game gratis
  time.sleep(7)
  rb.click(386, 523)

  # Pop-up +18
  time.sleep(5)
  rb.click(688, 469)

  #Clica em obter
  time.sleep(6)
  rb.click(1072, 557)

  # #Confirma a "compra"
  time.sleep(6)
  rb.click(1014, 692)

  #Fecha card de agradecimento
  time.sleep(6)
  rb.click(945, 118)

  sendConfirmationPrint()
