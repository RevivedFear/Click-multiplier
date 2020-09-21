import mouse

multiplier = input("How many times you want to multiply your clicks?")
while 0<1:
    if(mouse.is_pressed(button='left')==true):
    count=0
    while count<multiplier:
        mouse.click(button='left')
