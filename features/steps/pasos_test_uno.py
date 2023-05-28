from behave import given, when, then

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from Funciones import Funciones_Globales

t = 1

@given(u'Abriendo el navegador')
def step_impl(context):
    ser = Service("C:\Drivers\chromedriver.exe")
    op = webdriver.ChromeOptions()
    global driver, f
    context.driver = webdriver.Chrome(service=ser, options=op) # 1. Es importante añadir el context antes del driver
    f = Funciones_Globales(context.driver)
    f.Navegar("https://demoqa.com/text-box",t)

@when(u'Cargando el nombre "{userName}"')
def step_impl(context, userName):
    print(u'STEP: When Cargando el nombre usuario')
    f.TextoMixto("ID", "userName", userName, t) # 2. Una buena practica es siempre priorizar el ID ante el XPATH o CSS


@then(u'Cargando su "{userEmail}"')
def step_impl(context, userEmail):
    print(u'STEP: Then Cargando su email')
    f.TextoMixto("ID", "userEmail", userEmail, t)


@then(u'Cargando su dirección "{currentAddress}"')
def step_impl(context, currentAddress):
    print(u'STEP: Then Cargando su dirección nombre')
    f.TextoMixto("ID", "currentAddress", currentAddress, t)

@then(u'Cargando su dirección2 {permanentAddress}')
def step_impl(context, permanentAddress):
    print(u'STEP: Then Cargando su dirección2 mombre')
    f.TextoMixto("ID", "permanentAddress", permanentAddress, t)

@then(u'Se da clic al botón de Submit')
def step_impl(context):
    print(u'STEP: Then Se da clic al botón de Submit')
    f.ClickMixto("ID", "submit", t)
    time.sleep(2)
    context.driver.close()
