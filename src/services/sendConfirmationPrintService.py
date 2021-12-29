import pyautogui as rb
import time

def sendConfirmationPrint():
    
    rb.press('printscreen')
    time.sleep(1)

    #Abre Whatsapp
    rb.hotkey('ctrl', 't')
    rb.write('https://web.whatsapp.com/')
    rb.press('enter')

    #Busca grupo
    time.sleep(5)
    rb.click(240, 151)
    rb.write('getFreeGames')
    time.sleep(2)
    rb.click(205, 285)

    #Clica no chat
    # time.sleep(5)
    # rb.click(680, 700)
    
    #Envia o print
    time.sleep(1)
    rb.hotkey('ctrl', 'v')
    time.sleep(2)
    rb.press('enter')

    #Abre opções do grupo
    time.sleep(3)
    rb.click(383, 313)

    #Marca como não lido
    time.sleep(1)
    rb.click(450, 512)

    #Fecha browser
    time.sleep(1)
    rb.click(1342, 15)
