from tabulate import tabulate
from colorama import Fore, Style
from termcolor import colored # type: ignore
import pyinputplus as pyip # type: ignore
import re

program = [
    {'Contract ID' : 1, 'Group Name': 'COLDPLAY', 'Member Names': ['CHRIS MARTIN', 'JONNY BUCKLAND', 'GUY BERRYMAN', 'WILL CHAMPION'], 'Day of Show' :'FRI', 'Time of Show': '15:00-16:00', 'Hall': 1},
    {'Contract ID': 2, 'Group Name': 'RADIOHEAD', 'Member Names': ['THOM YORKE', 'JONNY GREENWOOD', 'COLIN GREENWOOD', 'ED O BRIEN', 'PHILIP SELWAY'], 'Day of Show': 'SAT', 'Time of Show': '15:30-16:30', 'Hall': 2},
    {'Contract ID': 3, 'Group Name': 'FOO FIGHTERS', 'Member Names': ['DAVE GROHL', 'NATE MENDEL', 'PAT SMEAR', 'CHRIS SHIFLETT'], 'Day of Show': 'SUN', 'Time of Show': '17:00-18:00', 'Hall': 3},
    {'Contract ID': 4, 'Group Name': 'RED HOT CHILI PEPPERS', 'Member Names': ['ANTHONY KIEDIS', 'FLEA', 'CHAD SMITH', 'JOHN FRUSCIANTE'], 'Day of Show': 'SUN', 'Time of Show': '18:00-19:00', 'Hall': 4},
    {'Contract ID': 5, 'Group Name': 'MUSE', 'Member Names': ['MATT BELLAMY', 'CHRIS WOLSTENHOLME', 'DOMINIC HOWARD'], 'Day of Show': 'FRI', 'Time of Show': '16:00-17:30', 'Hall': 5},
    {'Contract ID': 6, 'Group Name': 'MUSE', 'Member Names': ['MATT BELLAMY', 'CHRIS WOLSTENHOLME', 'DOMINIC HOWARD'], 'Day of Show': 'FRI', 'Time of Show': '18:00-19:30', 'Hall': 6},
    {'Contract ID': 7, 'Group Name': 'FOO FIGHTERS', 'Member Names': ['DAVE GROHL', 'NATE MENDEL', 'PAT SMEAR', 'CHRIS SHIFLETT'], 'Day of Show': 'SAT', 'Time of Show': '17:00-18:30', 'Hall': 8},
    {'Contract ID': 8, 'Group Name': 'TOTO', 'Member Names': ['STEVE LUKATHER', 'DAVID PAICH', 'JOSEPH WILLIAMS', 'SIMON PHILLIPS'], 'Day of Show': 'FRI', 'Time of Show': '18:00-19:00', 'Hall': 4},
    {'Contract ID': 9, 'Group Name': 'PROJECT POP', 'Member Names': ['OONK', 'GUGUM', 'TIKA', 'YOSI', 'UDJO', 'GEBBY'], 'Day of Show': 'SAT', 'Time of Show': '14:00-15:00', 'Hall': 10},
    {'Contract ID': 10, 'Group Name': 'RAN', 'Member Names': ['RAYI PUTRA', 'ASTONO ANDIKO', 'NINO KAYAM'], 'Day of Show': 'SUN', 'Time of Show': '15:00-16:00', 'Hall': 9},
    {'Contract ID': 11, 'Group Name': 'INCOGNITO', 'Member Names': ['JEAN-PAUL BLUEY MAUNICK', 'MOHAMMED NDIAYE', 'FRANCIS HILTON', 'MATT COOPER'], 'Day of Show': 'SUN', 'Time of Show': '16:30-17:30', 'Hall': 7},
    {'Contract ID': 12, 'Group Name': 'TRIBUTE WITH INDONESIAN SINGERS', 'Member Names': ['STEVE LUKATHER','JEAN-PAUL BLUEY MAUNICK','RAYI PUTRA', 'ASTONO ANDIKO', 'NINO KAYAM'], 'Day of Show': 'SUN', 'Time of Show': '16:00-17:30', 'Hall': 6}
]


print()

def add_show ():
    contract_ID = pyip.inputNum("\nInput Contract ID : ")

    for ID in program:
        if ID['Contract ID'] == contract_ID:
            print (colored(f"\nContract ID {contract_ID} is already registered. Please return to the main menu.","red"))
            return
                    
### Add Group Name
    while True:
        group_name = pyip.inputStr("\nInput Group Name :  ").strip().upper()
        for group in program:
            if group['Group Name'].strip().upper() == group_name:
                group_similar = pyip.inputYesNo(prompt=(colored(f"\nGroup {group_name} is already registered. Are you sure you want to add it? (Y/N) : ","red"))).strip()        
                if group_similar == "yes":
                    break
                elif group_similar == "no":
                    break             
        else:
            break
        if group_similar == "yes" :
            break
### Add Number of Members
    number_of_members = pyip.inputNum("\nInput Number of Members (1-25): ", min=1, max=25)
  
### Add Member Names    
    new_member = []
    for i in range(1,number_of_members+1):
        input_member = pyip.inputStr(f"\nInput Member's Name {i}: ").strip().upper()
        
        member_exist = False
        for group in program:
            if input_member in [member.strip().upper() for member in group ['Member Names']]:
                member_exist = True
                break
        
        if member_exist == True:
            confirm = pyip.inputYesNo(prompt=f"\nMember {input_member} is already registered. Are you sure you want to add it? (Y/N): ")            
            if confirm == 'no':
                print(colored(f"{input_member} is not added.","red"))
                continue 

        new_member.append(input_member) 
    print (colored(f"\nMember added : {", ".join(new_member)}.","green"))

## Add Day of Show
    day_show = pyip.inputChoice(['Fri','Sat','Sun'], prompt= "\nInput Day of Show (Fri/Sat/Sun): ").strip().upper()
   
## Add Time of Show   
    while True:
        time_show = pyip.inputStr("\nInput Time of Show (HH:MM-HH:MM, example: 15:00-16:00): ").strip()
        if re.match(r'^\d{2}:\d{2}-\d{2}:\d{2}$', time_show):
            break
        else:
            print(colored("\nTime format invalid. Please try again.", "red"))

## Add Hall Show
    hall_show = pyip.inputNum("\nInput Hall Number (1-10): ", min=1, max=10)

## Append to Program
    program.append({
        'Contract ID': contract_ID,
        'Group Name': group_name,
        'Member Names': new_member,
        'Day of Show': day_show,
        'Time of Show' : time_show,
        'Hall': hall_show
    })
    print(colored(f"\nThe show has been successfully added to the program","green"))

def display_show():

    while True:
        print(colored("\n📌 Choose options to display show :", "blue"))
        print("1. Display show based on Group")
        print("2. Display show based on Day")
        print("3. Display show based on Hall")
        print("4. Display All")
        print("5. Back to Main Menu")
        
        option = pyip.inputNum(colored("\nEnter option 1-5 : ", "blue"), min=1, max=5)

        table_data = []

        if option == 1:
            group = pyip.inputStr("\nDisplay show for Group: ").strip().upper()
            headers_1 = [Fore.BLUE + "group", "member names", "day", "time", "hall" + Style.RESET_ALL]

            for show in program:
                if show['Group Name'].strip().upper() == group:
                    table_data.append([show['Group Name'], '\n'.join(show['Member Names']), show['Day of Show'], show['Time of Show'],show['Hall']])        
            if not table_data:
                print(f"\nGroup Name {group} is not registered.")
            else:
                print(tabulate(table_data, headers_1, tablefmt="mixed_grid"))
            
        elif option == 2:
            day = pyip.inputChoice(['Fri','Sat','Sun'], prompt= "\nDisplay show on (Fri/Sat/Sun) : ").strip().upper()
            headers_2 = [Fore.BLUE + "day", "group", "member names", "time", "hall" + Style.RESET_ALL]
            for show in program:
                if show['Day of Show'].strip().upper() == day:
                    table_data.append([show['Day of Show'], show['Group Name'], '\n'.join(show['Member Names']), show['Time of Show'], show['Hall']])            
            table_data.sort(key=lambda x: x[3])
            print(tabulate(table_data, headers_2, tablefmt="mixed_grid")) 

        elif option == 3:
            hall = pyip.inputNum("\nDisplay show on Hall Number : ", min=1, max=10)
            headers_3 = [Fore.BLUE + "hall", "group", "member names", "day", "time" + Style.RESET_ALL]
            for show in program:
                if show['Hall'] == hall:
                    table_data.append([show['Hall'], show['Group Name'], '\n'.join(show['Member Names']), show['Day of Show'], show['Time of Show']])                                                                        
            table_data.sort(key=lambda x: x[1])
            print(tabulate(table_data, headers_3, tablefmt="mixed_grid"))        
       
        elif option == 4:
            headers_4 = [Fore.BLUE + "Contract ID", "group", "Member Names", "day", "time", "Hall" + Style.RESET_ALL]
            for show in program:
                table_data.append([show['Contract ID'], show['Group Name'], '\n'.join(show['Member Names']), show['Day of Show'], show['Time of Show'],show['Hall']])  
            table_data.sort(key=lambda x: x[1])
            print(tabulate(table_data, headers_4, tablefmt="mixed_grid"))    

        elif option == 5:
            break 

def table_contractID (ID):
    table_data = [[ID['Contract ID'], ID['Group Name'], '\n'.join(ID['Member Names']), ID['Day of Show'], ID['Time of Show'], ID['Hall']]]
    headers_edit_program = [Fore.BLUE + "Contract ID", "Group Name", "Member Names", "Day of Show", "Time of Show", "Hall" + Style.RESET_ALL]
    print(tabulate(table_data, headers_edit_program, tablefmt = "mixed_grid"))

def edit_show():
    contract_edit = pyip.inputNum("\nEnter the Contract ID of the show to be modified: ")
   
    for ID in program:
        if ID['Contract ID'] == contract_edit:
            table_contractID(ID)      
            break          
    else:
        print ("\nContract ID not registered. Please go to the main menu to add it.")
        return #exit if the contract is not found.
           
    def display_edit_program():
        while True:
            display_update = pyip.inputYesNo(prompt=f"\nDo you want to display the changes? (Y/N) : ")     
            if display_update == "Y":
                table_contractID(ID)
                break
            elif display_update == "N":
                break        
    # menu ubah 
    while True:
        print(colored("\n📌 Choose an option to modify the show:", "blue"))
        print("\n1. Change Group Name")
        print("2. Change Member Names")
        print("3. Change Day of Show")
        print("4. Change Time of Show")
        print("5. Change Hall Show")
        print("6. Return to Main Menu")

        edit_menu = pyip.inputInt(prompt=colored("\nEnter option 1-6: ","blue"), min=1, max=6)

        if edit_menu == 1:
            group_current = ID['Group Name'].strip().upper()
            print (f"\nCurrent Group Name : {group_current}")
            edit_menu_1 = pyip.inputStr("\nEnter the new Group Name :  ").strip().upper()
            ID ['Group Name'] = edit_menu_1
            print (colored(f"\nGroup Name successfully changed to {edit_menu_1}","green", attrs=["bold"]))  
            display_edit_program()
                 
        elif edit_menu == 2:
            member_current = ID['Member Names']
            print (f"\nCurrent Member Names : {member_current}")
            edit_menu_2 = pyip.inputStr("\nEnter the Member Name you want to change :  ").strip().upper()       
            
            if edit_menu_2 in [member.strip().upper() for member in member_current]:
                new_member = pyip.inputStr("Enter the new Member Name :  ").strip().upper()
                index = [member.strip().upper() for member in member_current].index(edit_menu_2) 
                ID['Member Names'][index] = new_member            
                print(colored(f"Member Name {edit_menu_2} berhasil diubah menjadi {new_member}.","green", attrs=["bold"]))  
                display_edit_program()
              
            else: 
                print (f"\nMember Name {edit_menu_2} is not registered under the Contract ID {ID['Contract ID']}")
    
        elif edit_menu == 3:
            day_current = ID['Day of Show']
            print (f"\nGroup {ID['Group Name']} is currently scheduled to perform on day : {day_current}")
            edit_menu_3 = pyip.inputChoice(['Fri','Sat','Sun'], prompt= "\nEnter the new Day of Show (fri/sat/sun): ").strip().upper()
            ID ['Day of Show'] = edit_menu_3
            print (colored(f"\nGroup {ID['Group Name']} successfully updated to perform on day {edit_menu_3}","green", attrs=["bold"]))                        
            display_edit_program()       

        elif edit_menu == 4:
            time_current = ID['Time of Show']
            print (f"\nGroup {ID['Group Name']} is currently scheduled to perform at time : {time_current}")
            edit_menu_4 = pyip.inputStr("\nEnter the new Time of Show (example : 15:00-16:00) : ").strip()
            ID ['Time of Show'] = edit_menu_4
            print (colored(f"\nGroup {ID['Group Name']} successfully updated to perform at time {edit_menu_4}","green", attrs=["bold"]))                        
            display_edit_program()       

        elif edit_menu == 5:
            hall_current = ID['Hall']
            print (f"\nCurrent Hall Show : Hall {hall_current}")         
            edit_menu_4 = pyip.inputNum("\nEnter the new Hall Show : ", min=1, max=10)
            ID ['Hall'] = edit_menu_4
            print (colored(f"\nHall Show successfully updated to perform on Hall {edit_menu_4}","green", attrs=["bold"]))            
            display_edit_program()  
            
        elif edit_menu == 6:
            return  


def delete_show():
    contract_ID_delete = pyip.inputNum("Enter the Contract ID you want to delete : ")

    for ID in program:
        if ID['Contract ID'] == contract_ID_delete:
            table_contractID(ID)
            confirm_deletion = pyip.inputYesNo(prompt=f"Are you sure you want to delete the show above? (Y/N): ")            
            if confirm_deletion == "yes":
                program.remove(ID)
                print(colored(f"\nShow with Contract ID {contract_ID_delete} has been successfully deleted.\n","green"))
                break
            elif confirm_deletion == "no":
                print(colored(f"\nShow was not deleted. Please return to the main menu.\n", "red"))
                break
    else:
        print(f"\nContract ID {contract_ID_delete} is not registered.")
        return
        
                        
def check_conflict():
    print("\n📌 This menu is used to display potential conflicts (shows scheduled at the same time) for a specific group or member. If there are any shows with potential conflicts, please confirm immediately with the Artist Manager❗")

    while True:
        print("\n1. Check a specific group")
        print("2. Check a specific member")
        print("3. Check all groups")
        print("4. Check all members")
        print("5. Return to Main Menu")

        menu_conflict = pyip.inputNum(colored("\nEnter option (1-5) : ","blue"), min=1, max=5)
        headers = [Fore.BLUE + "Contract ID", "Group Name", "Member Names", "Day of Show", "Time of Show", "Hall" + Style.RESET_ALL]

        if menu_conflict == 1:               
            check_group = pyip.inputStr("\nEnter the Group Name you want to check : ").strip().upper()
            table_data = [] 
            group_show_count = 0

            for group in program:
                if group['Group Name'].strip().upper() == check_group:
                    group_show_count += 1
                    table_data.append([group['Contract ID'], group['Group Name'], '\n'.join(group['Member Names']), group['Day of Show'], group['Time of Show'], group['Hall']])                    
                    table_data.sort(key=lambda x: x[3])

            if group_show_count == 0:
                print(f"\nGroup Name {check_group} is not registered.")
            else:
                print(tabulate(table_data, headers, tablefmt="mixed_grid"))
                print(f"\nGroup Name {check_group} has {group_show_count} shows in the program.")
                continue     

        if menu_conflict == 2:               
            check_member = pyip.inputStr("\nMasukkan Member Names yang ingin di Cek : ").strip().upper()
            table_data = [] 
            member_show_count = 0
            for member in program:
                if check_member in [nama.strip().upper() for nama in member['Member Names']]:
                    member_show_count += 1
                    table_data.append([member['Contract ID'], member['Group Name'], '\n'.join(member['Member Names']), member['Day of Show'], member['Time of Show'], member['Hall']])                    
                    table_data.sort(key=lambda x: x[3])
            if member_show_count == 0:
                print(f"\nMember Name {check_member} is not registered.")
            else:
                print(tabulate(table_data, headers, tablefmt="mixed_grid"))
                print(f"\nMember Name {check_member} has {member_show_count} shows in the program.")
                continue

        # all group
        if menu_conflict == 3:
            group_shows = {}
            for show in program:
                group_upper = show['Group Name'].strip().upper()
                if group_upper not in group_shows:
                    group_shows[group_upper] = []  
                group_shows[group_upper].append({
                    'Contract ID' : show['Contract ID'],
                    'Member Names': '\n'.join(show['Member Names']),  
                    'Day of Show': show['Day of Show'],
                    'Time of Show': show['Time of Show'],
                    'Hall': show['Hall']
                })
            # choose 2 or more shows
            for group, shows in group_shows.items():
                if len(shows) >= 2:
                    table_data = []
                    for show in shows:
                        table_data.append([show['Contract ID'],group, show['Member Names'], show['Day of Show'], show['Time of Show'], show['Hall']])
                        table_data.sort(key=lambda x: x[3])
                    headers_new_group = [Fore.BLUE + "Contract ID", "Group Name", "Member Names", "Day of Show", "Time of Show", "Hall" + Style.RESET_ALL]
                    print(f"\nPotential conflicts for Group Name : {group}")
                    print(tabulate(table_data, headers_new_group, tablefmt="mixed_grid"))

        #per Member Names, all
        if menu_conflict == 4:               
            member_shows = {}
            for show in program:
                for member in show['Member Names']:
                    member_upper = member.strip().upper()
                    if member_upper not in member_shows:
                        member_shows[member_upper] = []
                    member_shows[member_upper].append({
                        'Contract ID' : show['Contract ID'],
                        'Group Name': show['Group Name'],
                        'Day of Show': show['Day of Show'],
                        'Time of Show': show['Time of Show'],
                        'Hall': show['Hall']
                    })
            # members 2 or more
            for member, shows in member_shows.items():
                if len(shows) >= 2:  # Only show members who have 2 or more shows
                    table_data = []
                    for show in shows:
                        table_data.append([show['Contract ID'],member, show['Group Name'], show['Day of Show'], show['Time of Show'], show['Hall']])
                        table_data.sort(key=lambda x: x[3])

                    headers_new = [Fore.BLUE + "Contract ID" , "Member Names", "Group Name", "Day of Show", "Time of Show", "Hall" + Style.RESET_ALL]
                    print(f"\nPotensi konflik untuk Member Names: {member}")
                    print(tabulate(table_data, headers_new, tablefmt="mixed_grid"))
    
        if menu_conflict == 5:
            break               

def login_menu():
    while True:
        out_login = False
        admin_password = "2024"
        role = pyip.inputMenu(['Admin', 'Regular'], prompt=(colored("Welcome to Admin Portal PyFest 2024! Please Log In.\n\nYou will log in as : \n","blue")), numbered = True)

        if role == 'Admin':
            while True:
                password_attempt = pyip.inputPassword(prompt=(colored("\nPlease insert Admin password : ","green")))
                if password_attempt == admin_password:
                    print("\nHello Admin Program PyFest 2024!")
                    out_login = True
                    break
                else:
                    try_again = pyip.inputYesNo(prompt=(colored("\nPassword is wrong. Do you want to try again? (Y/N): \n","red")))
                    if try_again == "no":
                        break      
        else:
            out_login = True

        if out_login == True:
            break
    #after login/insert role.
    while True:
        print(colored("\n🎉 Welcome to Py Music Festival 2024 🎉\n", "magenta"))        
        if role == 'Admin':
            print("1. Add Show")
            print("2. Display Show")
            print("3. Modify Show")
            print("4. Delete Show")
            print("5. Check Show Conflicts")
            print("6. Exit")
        else:
            print("1. Display Show")
            print("2. Check Show Conflicts")
            print("3. Exit")
            
        if role == 'Admin':
            welcome = pyip.inputNum(colored("\nEnter menu option 1-6: ","blue"), min=1, max=6)
        else:
            welcome = pyip.inputNum(colored("\nEnter menu option 1-3: ","blue"), min=1, max=3)
        
        #for menu admin
        if role == 'Admin':
            if welcome == 1:
                add_show()
            elif welcome == 2:
                display_show()
            elif welcome == 3:
                edit_show()
            elif welcome == 4:
                delete_show()
            elif welcome == 5:
                check_conflict()
            elif welcome == 6:
                print ("\nThank you! See you next time! 👋")
                return
        #untuk menu reguler
        else:
            if welcome == 1:
                display_show()
            elif welcome == 2:
                check_conflict()
            elif welcome == 3:
                print ("\nThank you! See you next time!👋")
                return
                
login_menu()