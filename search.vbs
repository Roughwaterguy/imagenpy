Dim objShell
Set objShell = WScript.CreateObject("WScript.Shell")

' Prompt the user for input
Dim userInput
userInput = InputBox("Enter search term ->")

' Execute the Python script with the user input as an argument
objShell.Run "python imagen.py " & userInput, 1, True

' Cleanup
Set objShell = Nothing