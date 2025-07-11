age: int
name: str
height: float
is_human: bool

# age = 56
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

if police_check(1):
    print('You may pass')
else:
    print("Pay a fine")