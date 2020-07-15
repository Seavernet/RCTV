from bravia_tv import BraviaRC


ip_address = ('router assigned ip')

b = BraviaRC(ip_address)
Device_ID = 'your MAC Address'
Device_Name = 'name of device'
PSK = 'PSK'

def tvselection():
    if ip_address == (''):
        Device_ID = ''
        Device_Name = ''
        PSK = ''
        cred = ('Device ID: ' + Device_ID + ' Device name:  ' + Device_Name + ' PSK:  ' + PSK)
        print(cred)
    elif ip_address == (''):
        Device_ID = ''
        Device_Name = ''
        PSK = ''
    else:
        print('tv address not recognized')
        exit()

def connection():
    try:
        b.connect(PSK, Device_ID, Device_Name)
    except Exception:
         print('connection unsuccessful')


def applist():
    app_info = b.load_app_list()
    print (app_info)
    
def appstart(app):
    b.start_app(app)

def changechannel(channel):
    b.play_content(channel)
    
def powercheck():
    power_status = b.get_power_status()
    print ('power supply is ' + power_status)

def volinfo():
    volume_info = b.get_volume_info()
    print(volume_info)

def turnoff():
    print('the linked device has been turned off')
    b.turn_off()
    
def turnon():
    print('the linked device has been turned on')
    b.turn_on()

def volumeup():
    volumemultiplier = input('how many ticks up?')
    volumemultiplier = int(volumemultiplier)
    for i in range(0, volumemultiplier):
        print(' +1')
        b.volume_up
    volinfo()
    
def volumedown():
    volumedenominator = input('how many ticks down?')
    volumedenominator = int(volumedenominator)
    for i in range(0, volumedenominator):
        print(' -1')
        b.volume_up
    volinfo()

def commandcenter():
        
    while True:
        commandinput = input('action to preform')
        if commandinput == ('powercheck'):
            try:
                powercheck()
            except:
                print('power check failed')
        elif commandinput == ('quit'):
            try:
                break

            except:
                import consolelog
        elif commandinput == ('applist'):
            try:
                applist()
            except:
                print('app list not found')
        elif commandinput == ('app start'):
            try:
                app = input('app to start?')
                appstart(app)
            except:
                print('could not start ' + app)
        elif commandinput == ('change channel'):
            try:
                channel = input('channel to change to?')
                changechannel(channel)
            except:
                print('channel could not be changed')
        elif commandinput == ('check volume'):
            try:
                volinfo()
            except:
                print('could not collect volume data')
        elif commandinput == ('turn off'):
            try:
                turnoff()
            except:
                print('could not turn off Device')
        elif commandinput == ('turn on'):
            try:
                turnon()
            except:
                print('could not turn on device')
        elif commandinput == ('volume up'):
            try:
                volumeup()
            except:
                print('could not turn volume up')
        elif commandinput == ('volume down'):
            try:
                volumedown()
            except:
                print('could not turn volume down')
                
