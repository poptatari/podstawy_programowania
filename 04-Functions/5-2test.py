import converters

print('### Test converters')
print(f'Three meters is {converters.m_to_cm(3)}cm')
print(f'532cm is {converters.cm_to_m(532)}m')
print(f'100cm is {converters.cm_to_in(100)}in')
print(f'5ft 10in is {converters.ft_and_in_to_cm(5, 10)}cm')
