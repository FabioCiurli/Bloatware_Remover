import subprocess


print("Bloatware_Remover-V1.0\n----------------------\n")


def start():
    value1 = input("Questo programma cancellerà i bloatware (programmi preinstallati in Windows 10)\nSei sicuro di voler continuare premi S/N:")
    if value1 == 's' or value1 == 'S':
        subprocess.call(["powershell.exe", "Import-Module -Name Appx"])
        program_select()
    elif value1 == 'n' or value1 == 'N':
        exit
    else:
        start()


def program_select():
    value2 = input("Che programma vuoi rimuovere o premi 1 per uscire:\n1) Exit\n2) Cortana\n3) ZuneMusic\n4) BingTravel\n5) BingFood&Drink\n6) People\n7) BingFinance\n8) 3DBuilder\n9) BingNews\n10) XboxApp\n11) BingSports\n12) Getstarted\n13) Office.OneNote\n14) MicrosoftOfficeHub\n15) Photos\n")
    if value2 == '1':
        exit
    elif value2 == '2':
        value3 = input("Sei sicuro di voler continuare S/N:")
        if value3 == 's' or value3 == 'S':
            subprocess.call(["powershell.exe","Get-AppxPackage -allusers Microsoft.549981C3F5F10 | Remove-AppxPackage"])
            program_select()
        elif value3 == 'n' or value3 == 'N':
            program_select()
        else:
            print("Non hai premuto S o N")
            program_select()

        
    elif value2 == '3':
        value3 = input("Sei sicuro di voler continuare S/N:")
        if value3 == 's' or value3 == 'S':
            subprocess.call(["powershell.exe","Get-AppxPackage -allusers Microsoft.ZuneMusic | Remove-AppxPackage"])
            program_select()
        elif value3 == 'n' or value3 == 'N':
            program_select()
        else:
            print("Non hai premuto S o N")
            program_select()
    elif value2 == '4':
        value3 = input("Sei sicuro di voler continuare S/N:")
        if value3 == 's' or value3 == 'S':
            subprocess.call(["powershell.exe","Get-AppxPackage -allusers Microsoft.BingTravel | Remove-AppxPackage"])
            program_select()
        elif value3 == 'n' or value3 == 'N':
            program_select()
        else:
            print("Non hai premuto S o N")
            program_select()
    elif value2 == '5':
        value3 = input("Sei sicuro di voler continuare S/N:")
        if value3 == 's' or value3 == 'S':
            subprocess.call(["powershell.exe","Get-AppxPackage -allusers Microsoft.BingFoodAndDrink | Remove-AppxPackage"])
            program_select()
        elif value3 == 'n' or value3 == 'N':
            program_select()
        else:
            print("Non hai premuto S o N")
            program_select()
    elif value2 == '6':
        value3 = input("Sei sicuro di voler continuare S/N:")
        if value3 == 's' or value3 == 'S':
            subprocess.call(["powershell.exe","Get-AppxPackage -allusers Microsoft.People | Remove-AppxPackage"])
            program_select()
        elif value3 == 'n' or value3 == 'N':
            program_select()
        else:
            print("Non hai premuto S o N")
            program_select()
    elif value2 == '7':
        value3 = input("Sei sicuro di voler continuare S/N:")
        if value3 == 's' or value3 == 'S':
            subprocess.call(["powershell.exe","Get-AppxPackage -allusers Microsoft.BingFinance | Remove-AppxPackage"])
            program_select()
        elif value3 == 'n' or value3 == 'N':
            program_select()
        else:
            print("Non hai premuto S o N")
            program_select()
    elif value2 == '8':
        value3 = input("Sei sicuro di voler continuare S/N:")
        if value3 == 's' or value3 == 'S':
            subprocess.call(["powershell.exe","Get-AppxPackage -allusers Microsoft.3DBuilder | Remove-AppxPackage"])
            program_select()
        elif value3 == 'n' or value3 == 'N':
            program_select()
        else:
            print("Non hai premuto S o N")
            program_select()
    elif value2 == '9':
        value3 = input("Sei sicuro di voler continuare S/N:")
        if value3 == 's' or value3 == 'S':
            subprocess.call(["powershell.exe","Get-AppxPackage -allusers Microsoft.BingNews | Remove-AppxPackage"])
            program_select()
        elif value3 == 'n' or value3 == 'N':
            program_select()
        else:
            print("Non hai premuto S o N")
            program_select()
    elif value2 == '10':
        value3 = input("Sei sicuro di voler continuare S/N:")
        if value3 == 's' or value3 == 'S':
            subprocess.call(["powershell.exe","Get-AppxPackage -allusers Microsoft.XboxApp | Remove-AppxPackage"])
            program_select()
        elif value3 == 'n' or value3 == 'N':
            program_select()
        else:
            print("Non hai premuto S o N")
            program_select()
    elif value2 == '11':
        value3 = input("Sei sicuro di voler continuare S/N:")
        if value3 == 's' or value3 == 'S':
            subprocess.call(["powershell.exe","Get-AppxPackage -allusers Microsoft.BingSports | Remove-AppxPackage"])
            program_select()
        elif value3 == 'n' or value3 == 'N':
            program_select()
        else:
            print("Non hai premuto S o N")
            program_select()
    elif value2 == '12':
        value3 = input("Sei sicuro di voler continuare S/N:")
        if value3 == 's' or value3 == 'S':
            subprocess.call(["powershell.exe","Get-AppxPackage -allusers Microsoft.Getstarted | Remove-AppxPackage"])
            program_select()
        elif value3 == 'n' or value3 == 'N':
            program_select()
        else:
            print("Non hai premuto S o N")
            program_select()
    elif value2 == '13':
        value3 = input("Sei sicuro di voler continuare S/N:")
        if value3 == 's' or value3 == 'S':
            subprocess.call(["powershell.exe","Get-AppxPackage -allusers Microsoft.Office.OneNote | Remove-AppxPackage"])
            program_select()
        elif value3 == 'n' or value3 == 'N':
            program_select()
        else:
            print("Non hai premuto S o N")
            program_select()
    elif value2 == '14':
        value3 = input("Sei sicuro di voler continuare S/N:")
        if value3 == 's' or value3 == 'S':
            subprocess.call(["powershell.exe","Get-AppxPackage -allusers Microsoft.MicrosoftOfficeHub | Remove-AppxPackage"])
            program_select()
        elif value3 == 'n' or value3 == 'N':
            program_select()
        else:
            print("Non hai premuto S o N")
            program_select()
    elif value2 == '15':
        value3 = input("Sei sicuro di voler continuare S/N:")
        if value3 == 's' or value3 == 'S':
            subprocess.call(["powershell.exe","Get-AppxPackage -allusers Microsoft.Windows.Photos | Remove-AppxPackage"])
            program_select()
        elif value3 == 'n' or value3 == 'N':
            program_select()
        else:
            print("Non hai premuto S o N")
            program_select()
    else:
        program_select()

start()