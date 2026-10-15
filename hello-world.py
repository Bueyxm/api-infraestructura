# -------------------------------------------------------------
#  Copyright (c) 2022 Red Hat, Inc. All rights reserved.
#  Licensed under the MIT License. See LICENSE in project root.
# -------------------------------------------------------------
# This program prints Hello, world!

# str = 'world'
# print('Hello, ' + str + '!')
servicio = 'Sistema de respaldos'
estado = 'Detenido'

print('Servicio: ' + servicio)

if estado == 'Operativo':
    print('Resultado: el servicio esta operativo')
else:
    print('ALERTA: el servicio no esta operativo')
