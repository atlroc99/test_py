from classes.Phone import Phone

samsung = Phone('Samsung', '11S+', 1300)
samsung.desc_phone()
samsung.callNumber('889-992-2929')

print('---------------------------')

nokia = Phone("Nokia", "N92", 799)
nokia.desc_phone()
nokia.callNumber('470-339-0390')
print('---------------------------')

iPhone = Phone("iPhone", "11x", 1900)
iPhone.desc_phone()
iPhone.callNumber('993-000-3030')

print('---------------------------')
oppo = Phone("Oppo", 'Oppo-V2', 899)
oppo.desc_phone()
oppo.callNumber('339-003-0303')
oppo.set_serial_number('ABD233422LL')
oppo.set_color('Yellow')
print('Oppo serial number', oppo.get_serial_number())

print('---------------------------')
print('Set iPhone serial number:')
iPhone.set_serial_number('234543234L')
iPhone.set_color('Pink')
print('iPhone serial number: ', iPhone.get_serial_number())
print(f'{iPhone.desc_phone()}')
print(f'Phone Color: {iPhone.get_color()}')
