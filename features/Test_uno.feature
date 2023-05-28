Feature: Nuestro primer Demo

  Background: # Esta función permite que no sea necesario repetir el codigo en todos los Scenarios
      Given Abriendo el navegador

  Scenario Outline: Corriendo nuestro primer test
      When Cargando el nombre "<userName>"
      Then Cargando su "<userEmail>"
      And Cargando su dirección "<currentAddress>"
      And Cargando su dirección2 <permanentAddress>
      And Se da clic al botón de Submit

      Examples:
      | userName | userEmail | currentAddress | permanentAddress |
      | MrBlueSky123 | alexfabianmelo12@hotmail.com | Calle 28 # 01 - 26 San Fernando | Calle 28 # 01 - 26 San Fernando |
      | Insheloots | divher566@gmail.com | Calle 12 # 15 - 12 Centro | Calle 12 # 15 - 12 Centro |
