import pyautogui as rb
import time

from services.countFreeGamesService import countFreeGames
from services.sendConfirmationPrintService import sendConfirmationPrint, closeBrowser, unableToGetFreeGames

rb.PAUSE = 1

link = 'https://www.epicgames.com/store/pt-BR/free-games'
# link = 'https://www.epicgames.com/store/pt-BR/'

def getFreeGames():
  quantity = countFreeGames()
  if(quantity == 3):
    getThreeFreeGames()
  elif(quantity == 2):
    getTwoFreeGames()
  elif(quantity ==1):
    getOneFreeGames()
  else:
    unableToGetFreeGames()
    closeBrowser()

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
  rb.click(390, 530)

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
  closeBrowser()

def getTwoFreeGames():
  screenMap = [[320, 530], [660, 530]]

  # Abre o chrome
  rb.press('winleft')
  rb.write('chrome')
  rb.press('enter')

  #Seleciona user browser
  # time.sleep(3)
  # rb.click(1017,570)

  for game in screenMap:
    #Nova guia e direcionamento Epic Store
    rb.hotkey('ctrl', 't')
    rb.write(link)
    rb.press('enter')

    #Clica no banner de game gratis
    time.sleep(7)
    rb.click(game[0], game[1])

    # Pop-up +18
    time.sleep(6)
    rb.click(688, 469)

    #Clica em obter
    time.sleep(6)
    rb.click(1070, 515)

    # #Confirma a "compra"
    time.sleep(6)
    rb.click(1014, 692)

    #Fecha card de agradecimento
    time.sleep(6)
    rb.click(945, 118)

    sendConfirmationPrint()
  closeBrowser()

def getThreeFreeGames():

  screenMap = [[280, 530], [550, 530], [810, 530]]

  # Abre o chrome
  rb.press('winleft')
  rb.write('chrome')
  rb.press('enter')

  #Seleciona user browser
  # time.sleep(3)
  # rb.click(1017,570)

  for game in screenMap:
    #Nova guia e direcionamento Epic Store
    rb.hotkey('ctrl', 't')
    rb.write(link)
    rb.press('enter')

    #Clica no banner de game gratis
    time.sleep(7)
    rb.click(game[0], game[1])

    # Pop-up +18
    time.sleep(6)
    rb.click(688, 469)

    #Clica em obter
    time.sleep(6)
    rb.click(1070, 515)

    # #Confirma a "compra"
    time.sleep(6)
    rb.click(1014, 692)

    #Fecha card de agradecimento
    time.sleep(6)
    rb.click(945, 118)

    sendConfirmationPrint()
  closeBrowser()
