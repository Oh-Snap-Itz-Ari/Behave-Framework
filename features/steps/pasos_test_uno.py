from behave import given, when, then

@given(u'Abriendo el navegador')
def step_impl(context):
    print(u'STEP: Given Abriendo el navegador')


@when(u'Cargando el nombre del usuario')
def step_impl(context):
    print(u'STEP: When Cargando el nombre del usuario')


@then(u'Cargando su email')
def step_impl(context):
    print(u'STEP: Then Cargando su email')


@then(u'Cargando su dirección')
def step_impl(context):
    print(u'STEP: Then Cargando su dirección')
