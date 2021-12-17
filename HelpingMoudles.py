#Add Any helpfull stuff in functions here for later use
def GetMouseInfos(WhatToGet="leaving emety will get you x and y", GetXOnly=False, GetYOnly=False, GetColor=False, Key='Right', OverrideKey=False):#gets color of whats under Key cursor on right click
    try:
        import win32api
    except ModuleNotFoundError:
        print("win32api not found, to install do pip install pywin32")
    try:
        import time
    except ModuleNotFoundError:
        print("time not found, to install do pip install time?")
    try:
        import pyautogui
    except ModuleNotFoundError:
        print("py auto gui not found, to install do pip install pyautogui")
    #--------------------------------------------------------------
    #above checks if needed modules are installed if not tells user
    #code below is to get all varibles needed
    #---------------------------------------------------------------
    print(WhatToGet)
    if OverrideKey:
        Key_To_click = Key
    if Key == 'Left':
        Key_To_click = 0x01
    if Key == 'Right':
        Key_To_click = 0x02
    if Key == 'Wheel':
        Key_To_click = 0x04
    state_left = win32api.GetKeyState(Key_To_click)  # Left button up = 0 or 1. Button down = -127 or -128
    IsTrue = True
    while IsTrue:
        a = win32api.GetKeyState(Key_To_click)
        if a != state_left:  # Button state changed
            state_left = a
            if a < 0:
                #global Xpos, Ypos
                Xpos, Ypos = win32api.GetCursorPos()
                x, y = pyautogui.position()
                pixelColor = pyautogui.screenshot().getpixel((x, y))
            else:
                posnowX, posnowY = win32api.GetCursorPos()
                win32api.SetCursorPos((posnowX, posnowY))
                IsTrue = False#remove this for it to keep giving coords on click without it just quitting after 1 click
        time.sleep(0.001)
    #--------------------------------------------------------------------
    #The Code above is the code to get all varibles and code below is for the user to get what he wants
    #--------------------------------------------------------------------
    
    if GetXOnly: #Checks if we should get Only X (def options) the command to do this would be GetKeyInfos("Click To get X ONLY", True)
        if GetYOnly:
            return(Xpos , Ypos)
        if GetColor:
            return(Xpos, pixelColor)
        return(Xpos)
    if GetYOnly: #Checks if we should get Only Y (def options) the command to do this would be GetKeyInfos("Click To get X ONLY",False, True)
        if GetXOnly:
            return(Xpos , Ypos)
        if GetColor:
            return(Ypos, pixelColor) 
        return(Ypos)
    if GetColor:
        return(pixelColor) #Checks 
    return(Xpos, Ypos)
# getKeyinfos("Anything here without any other guidelines will give u x and y only on right click")



#Fastest Left Click
def FastLeftclick(x,y):
    try:
        import win32api, win32con
    except ModuleNotFoundError:
        print("win32api not found, to install do pip install pywin32")
    import time
    win32api.SetCursorPos((x,y)) #Set the cursor positions to x and y giving in function options
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) #clicks left button down
    time.sleep(0.1) #This pauses the script for 0.1 seconds so that it doesnt bug
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0) #left button up



    
def add_or_sub(add=False, subtract=True, Num1=1, Num2=1):
    if add:
        if subtract:
            print("you have choosen both")
            return('Choose both')
            quit()
        x =  Num1 + Num2
        return (x)
    

    if subtract:
        if add:
            print("you have choosen both")
            return('Choose both')
            quit()
        xS =  Num1 - Num2
        return (xS)



class PrintColor: #old
    '''
    args are what to print which is just what do you want to print? color well ye
    '''
    
    
    def __init__(self, Whattoprint='Text', Color=''):
        self.color = Color
        self.whattoprint = Whattoprint
        
        

    def TermColorPrint(self):
            try:
                from termcolor import colored
            except ModuleNotFoundError:
                print("win32api not found, to install do pip install pywin32")
                
            """Colorize text.

            Available text colors:
            red, green, yellow, blue, magenta, cyan, white."""
            
            print(colored(self.whattoprint, self.color))
#Without class cause in case idk
def DTermColorPrint(whattoprint, color): #direct print
    try:
        from termcolor import colored
    except ModuleNotFoundError:
        print("termcolor not found")
        
    """Colorize text.

    Available text colors:
    red, green, yellow, blue, magenta, cyan, white."""
    
    print(colored(whattoprint, color))
def TermColorPrint(whattoprint, color): #doesnt print directly retuns instead
    try:
        from termcolor import colored
    except ModuleNotFoundError:
        print("win32api not found, to install do pip install pywin32")
        
    """Colorize text.

    Available text colors:
    red, green, yellow, blue, magenta, cyan, white."""
    
    print(colored(whattoprint, color)) 
def DColoromaprint(whattoprint, color): #direct print
    '''
    suported colors = red, green, blue, magenta, cyan, white, black, yellow
    '''
    try:
        from colorama import Fore, Back, Style
    except ModuleNotFoundError:
        print("You dont have colorama please install it by doing pip install colorama in powershell")
        quit()
    
    
    newco = color.lower()
    
    if newco == 'red':
        print(Fore.RED + whattoprint)
    
    if newco == 'green':
        print(Fore.GREEN + whattoprint)
        
    if newco == 'blue':
        print(Fore.BLUE + whattoprint)
        
    if newco == 'black':
        print(Fore.BLACK + whattoprint)
    
    if newco == 'yellow':
        print(Fore.YELLOW + whattoprint)
    
    if newco == 'magenta':
        print(Fore.MAGENTA + whattoprint)
    
    if newco == 'cyan':
        print(Fore.CYAN + whattoprint)

    if newco == 'white':
        print(Fore.WHITE + whattoprint) 
        
    if newco == 'reset':
        print(Fore.RESET + whattoprint)        
def Coloromaprint(whattoprint, color): #doesnt print directly retunrs instead
    '''
    suported colors = red, green, blue, magenta, cyan, white, black, yellow
    '''
    try:
        from colorama import Fore, Back, Style
    except ModuleNotFoundError:
        print("You dont have colorama please install it by doing pip install colorama in powershell")
        quit()
    
    
    newco = color.lower()
    
    if newco == 'red':
        return(Fore.RED + whattoprint)
    
    if newco == 'green':
        return(Fore.GREEN + whattoprint)
        
    if newco == 'blue':
        return(Fore.BLUE + whattoprint)
        
    if newco == 'black':
        return(Fore.BLACK + whattoprint)
    
    if newco == 'yellow':
        return(Fore.YELLOW + whattoprint)
    
    if newco == 'magenta':
        return(Fore.MAGENTA + whattoprint)
    
    if newco == 'cyan':
        return(Fore.CYAN + whattoprint)

    if newco == 'white':
        return(Fore.WHITE + whattoprint) 
        
    if newco == 'reset':
        return(Fore.RESET + whattoprint)
            
def rainbowtext(text):
    try:
        from colorama import Fore, Back, Style
    except ModuleNotFoundError:
        print("Coloroma not found please install it using pip")
        
    colors = ['\u001b[31m', '\u001b[31;1m', '\u001b[33m', '\u001b[32m', '\u001b[34m', '\u001b[36m', '\u001b[35m']
    pos = 0
    colchar = ""
    for char in text:
        colchar = colchar + colors[pos] + char
        if pos==6:
            pos=0
        else:
            pos += 1
    return colchar

def rainbowtextq(text):
    try:
        from colorama import Fore, Back, Style
    except ModuleNotFoundError:
        print("Coloroma not found please install it using pip")
        
    colors = ['\u001b[31m', '\u001b[31;1m', '\u001b[33m', '\u001b[32m', '\u001b[34m', '\u001b[36m', '\u001b[35m']
    pos = 0
    colchar = ""
    for i, char in enumerate(text):
        colchar += colors[i%6] + char
        return colchar
    
def dumpjson(path='c:\Yourstuffhere.json', saveunder='scroessa1safa', subdomain='test sscores of my student', savewhat='20% = fail'):
    import json
    #so path is where u want to store the json file. other stuff i cant explain just look at results current stuff would be
    #{"scroessa1safa": [{"test sscores of my student": "20% = fail"}]} would be the output.
    data = {}
    data[f'{saveunder}'] = []
    data[f'{saveunder}'].append({
        f'{subdomain}': savewhat,
    })

    with open(f'{path}', 'w') as outfile:
        json.dump(data, outfile)

def readjson(path='c:\Yourstuffhere.json', saveunder='scroessa1safa', subdomain='test sscores of my student'):
    import json
    #output of this would be '20% = fail'
    with open(f'{path}') as json_file:
        data = json.load(json_file)
        for p in data[f'{saveunder}']:
            (p[f'{subdomain}'])

    
                
    return(p[f'{subdomain}'])