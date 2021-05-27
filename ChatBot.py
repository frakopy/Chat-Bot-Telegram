import telegram
from telegram.ext import *
import datetime, time
import logging

#Para saber que y cuando paso algo con nuestro programa
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


'''
Token del bot ---> 1042288743:AAHbO-tsc7HuaQaulgXXXer3QKOFRfqJ2WQ
ID de Telegram --> @Frank454Bot
'''
bot = telegram.Bot(token='1042288743:AAHbO-tsc7HuaQaulgXXXer3QKOFRfqJ2WQ')

#bot_updater recibe actualizaciones de Telegram(mensajes,archivos,audio,video,etc) y 
#las enrega al Dispatcher mas abajo de este codigo
bot_updater=Updater(bot.token)

def start(bot,update,pass_chat_data=True):
    update.message.chat_id
    bot.sendMessage(chat_id=update.message.chat_id, text='Hola me llamo CoreBot y estoy para servirte')

def saluda(bot=bot, update=bot_updater):
    update.message.chat_id
    bot.sendMessage(chat_id=update.message.chat_id, text='Hola gusto en saludarte, estoy programado para brindar')
    bot.sendMessage(chat_id=update.message.chat_id, text='informacion sobre las credenciales de acceso')
    bot.sendMessage(chat_id=update.message.chat_id, text='a los diferentes nodos del CORE de VOZ')
    
def tiempo(bot=bot, update=bot_updater):
    Fecha = time.strftime("%Y/%m/%d")
    hora = time.strftime("%H:%M:%S")
    update.message.chat_id
    bot.sendMessage(chat_id=update.message.chat_id, text='Hoy es: '+Fecha+' y son las '+hora)

def info_nodos(bot=bot, update=bot_updater):
    elementos ='''
    PANAMA:\n\nPANSL4M--AP2_PAN4--DAVTE3M--BSP_DAVID\n\nPANSL2P--DAVTE1P--PANSL1G--PANSL2G\n
    PANSL3G--DAVTE1G--PANSL1H--DAVTE1H\n
    PGWPA\n\n
    COSTA RICA:\n\nSJLIN1HSS--SJLIN2HSS--PGWCR--SJLIN1M\n\nAP2_SJ1M--SJLIN1G--SJLIN2G--SJLIN2P\n\n
    NICARAGUA:\n\nNICMA4M--AP2_NIC4--NICGR1M--NICMA2M\n\nNICMA4B--NICMA5B--NICMA6B--NICGR1B\n
    NICMA2X--NICMA3X--NICGR1X--NICGR2X\n
    NICMA1G--NICMA2G--NICMA3G--NICGR1G\n
    BSP_GRANADA--NICMA1H--NICGR1H\n
    PGWNI--NICGR1P\n\n
    NODOS-REGIONALES:\n\nVPN_SV--PPS_CR--PPS_PA--CCN--VPN_PA\n\nACCESO_TS:\n\nTS_ADMIN
    '''
    
    bot.sendMessage(chat_id=update.message.chat_id, text=elementos.replace(' ',''))

def crede_nodos(bot=bot, update=bot_updater):
    
    contador=0

    lista_nodos= ["PANSL4M",'AP2_PAN4',"DAVTE3M","PANSL2P","DAVTE1P","PANSL1G","PANSL2G","PANSL3G",'DAVTE1G',
    "VPN_SV","PPS_CR","PPS_PA","BSP_DAVID",'CCN','PANSL1H','DAVTE1H','PGWPA','SJLIN1HSS','SJLIN2HSS','PGWCR',
    'SJLIN1M','AP2_SJ1M','SJLIN1G','SJLIN2G','SJLIN2P','NICMA4M','AP2_NIC4','NICGR1M','NICMA2M','NICMA4B','NICMA5B',
    'NICMA6B','NICGR1B','NICMA2X','NICMA3X','NICGR1X','NICGR2X','NICMA1G','NICMA2G','NICMA3G','NICGR1G','BSP_GRANADA',
    'NICMA1H','NICGR1H','PGWNI','NICGR1P','TS_ADMIN','VPN_PA']

    ruta_archivo_credenciales = 'D:\A_PYTHON\ProgramasPython\ChatBot\IPnodos.txt'

    for i in lista_nodos:
        if update.message.text.upper().find(i) >= 0:
            archivo = open(ruta_archivo_credenciales, "r")
            direccionesIP = ""
            fin = True
            linea= ""
            tamaño= len(archivo.readlines())
            archivo.seek(0)
            while fin == True:
                linea = str(archivo.readline()).replace("\n","")
                if linea == i:
                    for j in range(tamaño):
                        linea = str(archivo.readline())
                        if linea == "\n":
                            fin = False
                            break
                        else:
                            direccionesIP = direccionesIP + linea
            archivo.close()
            bot.sendMessage(chat_id=update.message.chat_id, text=direccionesIP)
        else:
            contador +=1
    
    if contador == len(lista_nodos):
        aviso='lo siento no puedo darte la informacion que solicitas,por favor has click en este comando ---> /nodos ,para ver la lista de nodos que tengo disponible sobre los cuales puedo darte informacion'

        bot.sendMessage(chat_id=update.message.chat_id, text=aviso)

#Se declaran los controladores de tipo CommandHandler, se les pasa el comando enviado por 
#el usuario desde Telegram y se hace la llamada a la respectiva funcion 
start_handler = CommandHandler('start',start)
saluda_handler = CommandHandler('saluda',saluda)
tiempo_handler = CommandHandler('tiempo',tiempo)
nodos_handler = CommandHandler('nodos',info_nodos)

#Se entregan las actualizaciones de Telegram del UPDATER al despachador
#En nuestro caso se entregan los mensajes y comandos que el usuario envia desde Telegram
dispatcher = bot_updater.dispatcher

#El despachador invoca a los Command handlers que estan declarados mas arriba de este codigo
dispatcher.add_handler(start_handler)
dispatcher.add_handler(saluda_handler)
dispatcher.add_handler(tiempo_handler)
dispatcher.add_handler(nodos_handler)

#El despachador invoca al MessageHandler le pasa el texto que escribio el usuario en Telegram y 
#llama a la funcion que declaramos arriba que se llama core_nodos
dispatcher.add_handler(MessageHandler(Filters.text, crede_nodos))

#----------------------------Iniciamos el bot----------------------------------------------------------------------
bot_updater.start_polling()
bot_updater.idle()
#------------------------------------------------------------------------------------------------------------------

while True:
    pass
