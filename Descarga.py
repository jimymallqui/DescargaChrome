#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from chrome_version import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys
import os
from Encriptación import *
# from savepage import *
import json
import pyautogui
from time import sleep
import requests
import urllib.request, urllib.error, urllib.parse, urllib
import pdfkit
from pywebcopy import save_webpage
from pywebcopy import save_website
from bs4 import BeautifulSoup
from requests_html import HTMLSession

class MyTestCase(unittest.TestCase):

    def setUp(self):
        # El constructor recibe como parámetros:
        ## hora = en un string con formato hh:mm:ss y es la hora a la que queremos que se ejecute la función.
        ## delay = tiempo de espera entre comprobaciones en segundos.
        ## funcion = función a ejecutar.

        #super(MyTestCase, self).__init__()
        self.rutadriver = "C:\CarpetaProyecto"
        # self.driver = ""
        inicio = 1
        while inicio == 1:
            # codigo desconocido By LH
            chromeOptions = Options()
            chromeOptions.add_argument('--no-sandbox')
            chromeOptions.add_argument('ignore-certificate-errors')
            chromeOptions.add_argument('--log-level=3')
            chromeOptions.add_argument('start-maximized')
            chromeOptions.add_experimental_option("prefs", {"download.default_directory": "Ruta\\DESCARGAAUTOMATICA",
                                                            "download.prompt_for_download": False,
                                                            "directory_upgrade": True,
                                                            "safebrowsing_for_trusted_sources_enabled": False,
                                                            "safebrowsing.enabled": False})
            chromeOptions.add_argument('--save-page-as-mhtml')

            options = Options()
            options.page_load_strategy = 'normal'
            # desired_caps = {'prefs': {'download': {'default_directory': 'Ruta/DESCARGAAUTOMATICA'}}}


            # try:
            # histolog(archivo_log, f'{datetime.now()}: Se procede a abrir el aplicativo')
            # ubica el chromedriver que se situa en la misma carpeta del codigo
            global driver
            try:

                if getattr(sys, 'frozen', False):
                    print("*/***************************")
                    chromedriver_path = os.path.join(sys._MEIPASS, "Ruta\\del\\chromedriver.exe")

                    self.driver = webdriver.Chrome(chromedriver_path, chrome_options=chromeOptions, options=options)
                    # histolog(archivo_log, f'{datetime.now()}: Abrimos el Chrome 1')
                else:
                    self.driver = webdriver.Chrome(chrome_options=chromeOptions, options=options)
                    # histolog(archivo_log, f'{datetime.now()}: Abrimos el Chrome 2')
                    # ingresar al link de logeo

                inicio = 0
            except:
                Nomb_error = 'Error en la apertura de chromedriver'
                print(Nomb_error)
                descargachrome(self.rutadriver)
                inicio = 1



    def test_logeo(self):
        # Realizamos la lectura de las credenciales
        with open('data.json') as file:
            data = json.load(file)
            usuariocrip = data[0]['usuario']
            passcrip = data[0]['contrasena']

        # funcion para desencriptar
        user = self.desencriptar(usuariocrip)
        passw = self.desencriptar(passcrip)
        time.sleep(5)

        driver = self.driver
        driver.get('url_pagina_gestionar')
        driver.implicitly_wait(20)

        
        
        # ingresar usuario
        ingresousuario = EC.presence_of_element_located((By.NAME, 'Name_de_la_etiqueta'))
        WebDriverWait(driver, 30).until(ingresousuario)
        usuario = driver.find_element(By.NAME, 'Name_de_la_etiqueta')
        usuario.send_keys(user)
        time.sleep(5)

        # ingresar contraseña
        ingresoclave = EC.presence_of_element_located((By.NAME, 'Name_de_la_etiqueta'))
        WebDriverWait(driver, 30).until(ingresoclave)
        clave = driver.find_element(By.NAME, 'Name_de_la_etiqueta')
        clave.send_keys(passw)
        time.sleep(5)

        # presionar el boton inicio
        botoninicio = EC.presence_of_element_located((By.XPATH, '//*XPATHe_de_la_etiqueta'))
        WebDriverWait(driver, 30).until(botoninicio)
        btninicio = driver.find_element(By.XPATH, '//*XPATHe_de_la_etiqueta')
        btninicio.click()
        driver.implicitly_wait(30)
        time.sleep(7)

        # presionar la opción todos los casos
        optionpanel = EC.presence_of_element_located((By.XPATH, '//*XPATHe_de_la_etiqueta'))
        WebDriverWait(driver, 30).until(optionpanel)
        optpanel = driver.find_element(By.XPATH, '//*XPATHe_de_la_etiqueta')
        optpanel.click()
        time.sleep(5)

        # ingresar Solicitudes 
        inputbuscador = EC.presence_of_element_located(
            (By.XPATH, '//*XPATHe_de_la_etiqueta'))
        WebDriverWait(driver, 30).until(inputbuscador)
        inputbuscador = driver.find_element(By.XPATH, '//*XPATHe_de_la_etiqueta')
        inputbuscador.send_keys("2323523523")
        time.sleep(5)


        # presionar el boton Informes
        botonInformes = EC.presence_of_element_located((By.XPATH, '//*XPATHe_de_la_etiqueta'))
        WebDriverWait(driver, 30).until(botonInformes)
        btnInformes = driver.find_element(By.XPATH, '//*XPATHe_de_la_etiqueta')
        btnInformes.click()
        driver.implicitly_wait(30)

        # /html/body/div[1]/div[2]/div/div/div[3]/div/div[4]/div/div/div[1]/div[2]/section/div[2]/div[1]/div[2]/div/div[2]/span[1]
        # ingresar número de caso
        veridupli = EC.presence_of_element_located((By.XPATH, './/span[contains(text(),"texto a buscar")]'))
        WebDriverWait(driver, 2).until(veridupli)
        ingresarnumero = driver.find_element(By.XPATH, './/span[contains(text(),"texto a buscar")]')
        actions = ActionChains(driver)
        actions.double_click(ingresarnumero).perform()


        try:
            while 1:
                # presionar el menu proceso de tención
                # //*[@id="conversation"]/div[3]/div/div[2]/div[2]/div[2]/div[1]/div[2]
                # //*[@id="conversation"]/div[6]/div/div[2]/div[2]/div[2]/div[1]/div[2]
                # //*[@id="conversation"]/div[8]/div/div[2]/div[2]/div[2]/div[1]/div[2]
                # //*[@id="conversation"]/div[11]/div/div[2]/div[2]/div[2]/div[1]/div[2]
                #$x('//div[contains(text(),"Mostrar más")]')
                # /html/body/div[1]/div[2]/div/div/div[3]/div/table/tbody/tr/td[1]/div[1]/div/div[1]/div/div/div[6]/div/div[2]/div[2]/div[2]/div[1]/div[2]

                #//*[@id="conversation"]/div[3]/div/div[2]/div[2]/div[2]/div[1]/div[2]   /html/body/div[1]/div[2]/div/div/div[3]/div/table/tbody/tr/td[1]/div[1]/div/div[1]/div/div/div[3]/div/div[2]/div[2]/div[2]/div[1]/div[2]
                desplmas = EC.presence_of_element_located((By.XPATH, '//div[2]/div[1]/div[contains(text(),"texto a buscar")]'))
                WebDriverWait(driver, 2).until(desplmas)
                desplemost = driver.find_element(By.XPATH, '//div[2]/div[1]/div[contains(text(),"texto a buscar")]')
                desplemost.click()

        except Exception as e:
            print("Ya no se encontro mas desplegables")

        time.sleep(7)

        # optiene la url de la pagina web
        url = driver.current_url
        print(url)

        FILE_NAME = '132313423'
        pyautogui.hotkey('ctrl', 's')
        time.sleep(2)
        if FILE_NAME != '':
            pyautogui.typewrite(FILE_NAME)

        time.sleep(3)
        # pyautogui.hotkey('shift', 'tab')
        time.sleep(3)
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(3)
        # pyautogui.hotkey('enter')
        time.sleep(2)
        pyautogui.write('C:/SKY', interval=0.25)
        time.sleep(3)
        pyautogui.hotkey('enter')
        time.sleep(3)
        pyautogui.hotkey('enter')
        time.sleep(3)
        pyautogui.hotkey('enter')
        time.sleep(3)
        pyautogui.hotkey('enter')
        time.sleep(3)
        print("acabo la ejecución")
        time.sleep(30)


    def tearDown(self):
        # close the browser window
        time.sleep(7)
        driver = self.driver
        driver.quit()

    def desencriptar(self, variable):
        # funcion para desencriptar
        key = ""
        clasee = AESCipher(key)
        desencriptado = clasee.decrypt(variable)
        return desencriptado



if __name__ == '__main__':
    unittest.main()
