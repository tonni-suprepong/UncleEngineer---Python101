class DigitalDoorLock:
        def __init__(self):
                self.status = 'open'
                self.password = '0000'

        def getStatus(self):
                return self.status
        
        def lock(self):
                self.status = 'locked'
                print('locked successful')

        def open(self,password):
                if self.password == password:
                        self.status = 'open'
                        print('open successful')
                else:
                        print('incorrect password')

        def change_pwd(self,password,new_password):
                if self.password == password:
                        self.password = new_password
                        print('change password successful')
                else:
                        print('incorrect password')
        

door = DigitalDoorLock()

print('1 - CHECK : initial door lock status')
print('door is ' + door.status)
print('\n')

print('2 - METHOD : lock the door')
door.lock()
print('CHECK STATUS : door is ' + door.status)
print('\n')


print('3 - METHOD : open the door with wrong password')
door.open('0010')
print('CHECK STATUS : door is ' + door.status)
print('\n')

print('4 - METHOD : open the door with right password')
door.open('0000')
print('CHECK STATUS : door is ' + door.status)
print('\n')

print('5 - METHOD : lock the door and change password to 0001')
door.lock()
print('CHECK STATUS : door is ' + door.status)
door.change_pwd('0000','0001')
print('CHECK PASSWORD : new password is ' + door.password)
print('\n')

print('6 - METHOD : open the door with old password')
door.open('0000')
print('CHECK STATUS : door is ' + door.status)
print('\n')

print('7 - METHOD : open the door with new password')
door.open('0001')
print('CHECK STATUS : door is ' + door.status)
print('\n')

print('\n')