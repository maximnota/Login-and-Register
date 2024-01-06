from iPyQT import *


users = "users.txt"
choice = 0
new_user = ""
new_password = ""
words = []

def register():
    win.HideAll()
    userExists = False
    badSymbolExists = False
    maxCharLimit = False

    for character in win.getTextFieldValue(UsernameTextField):
        if character == ',':
            badSymbolExists = True
            break
        if character == ' ':
            badSymbolExists = True
            break

    for character in win.getTextFieldValue(PasswordTextField):
        if character == ',':
            badSymbolExists = True
            break
        if character == ' ':
            badSymbolExists = True
            break

    if len(win.getTextFieldValue(UsernameTextField)) >= 10:
        maxCharLimit = True
    if len(win.getTextFieldValue(PasswordTextField)) >= 10:
        maxCharLimit = True

    i = 0
    with open(users, "r", encoding="UTF-8") as file:
        for item in file:
            item = item.strip()
            item = item.split(',')
            if item[0] == win.getTextFieldValue(UsernameTextField) and userExists == False and badSymbolExists == False and maxCharLimit == False:
                win.addText("User Exists", 25, "Center-top")
                win.addButton("Retry", registerWindow)
                win.addButton("Return to main window", defaultWindow)
                userExists = True

        if userExists == False and badSymbolExists == False and maxCharLimit == False:
            with open(users, "a", encoding="UTF-8") as file:
                file.write("\n" + win.getTextFieldValue(UsernameTextField) + "," + win.getTextFieldValue(PasswordTextField))
            a = "Registered: " + win.getTextFieldValue(UsernameTextField) + "\n Password: " + win.getTextFieldValue(PasswordTextField)
            Text = win.addText(a, 25, "Center")
            button = win.addButton("Return to main window", defaultWindow)

        if badSymbolExists == True:
            win.HideAll()
            win.addText("Some symbols you inputted aren't supported or you have not entered anything into one of the options", 25, "Center-top")
            win.addButton("Retry", registerWindow)
            win.addButton("Return to main window", defaultWindow)

        if maxCharLimit == True:
            win.HideAll()
            win.addText("You have reached the maximum character limit", 25, "Center-top")
            win.addButton("Retry", registerWindow)
            win.addButton("Return to main window", defaultWindow)

def registerWindow():
    win.changeWindowTitle("Register")
    win.HideAll()
    Title = win.addText("Register", 50, "Center")
    UserNameText = win.addText("Username", 25, "Center-bottom")
    global UsernameTextField
    UsernameTextField = win.addTextField(20, 25,"Center-top")
    win.addText("Pasword", 25, "Center-top")
    global PasswordTextField
    PasswordTextField = win.addTextField(25,50,"Center-top")
    ContinueButton = win.addButton("Sign up", register)




def signIn():
    win.HideAll()
    wentWrong = False
    with open(users, "r", encoding="UTF-8") as file:
        try:
            for item in file:
                item = item.strip()
                words = item.split(',')
                if words[0] == win.getTextFieldValue(Username):
                    if win.getTextFieldValue(Password) == words[1]:
                        win.HideAll()
                        win.addText("You have logged in", 25, "Center-top")
                        win.addButton("Return to main window", defaultWindow)
                        break
                    else:
                        if wentWrong == False:
                            win.addText("Something went wrong", 25, "Center-top")
                            win.addButton("Retry", signInWindow)
                            win.addButton("Return to main window", defaultWindow)
                        wentWrong = True
                else:
                    if wentWrong == False:
                        win.addText("Something went wrong", 25, "Center-top")
                        win.addButton("Retry", signInWindow)
                        win.addButton("Return to main window", defaultWindow)       
                    wentWrong = True        
        except:
            if wentWrong == False:
                win.HideAll()
                win.addText("Something went wrong", 25, "Center-top")
                win.addButton("Retry", signInWindow)
                win.addButton("Return to main window", defaultWindow)                
            wentWrong = True


def signInWindow():
    win.HideAll()
    win.changeWindowTitle("Sign in")
    Title = win.addText("Sign In", 25, "Center-top")
    UsernameText = win.addText("Username:", 25, "Center-top")
    global Username
    Username = win.addTextField(25, 50, "Center-top")
    PasswordText = win.addText("Password:", 25, "Center-top")
    global Password
    Password = win.addTextField(25, 50, "Center-top")
    win.addButton("Sign in", signIn)
    


def defaultWindow():
    win.HideAll()
    win.changeWindowTitle("Main window")
    win.addButton("Register", registerWindow)
    win.addButton("Sign in", signInWindow)


win = CustomWindow(300, 350, "Main window")
win.create()
RegisterButton = win.addButton("Register", registerWindow)
win.addButton("Sign in", signInWindow)
win.init()