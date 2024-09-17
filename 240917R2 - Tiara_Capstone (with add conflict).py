from tabulate import tabulate
from colorama import Fore, Back, Style, init
from termcolor import colored # type: ignore
import pyinputplus as pyip # type: ignore
import re

program = [
    {'Contract ID' : 1, 'Nama Grup': 'COLDPLAY', 'Nama Anggota': ['CHRIS MARTIN', 'JONNY BUCKLAND', 'GUY BERRYMAN', 'WILL CHAMPION'], 'Hari Show' :'FRI', 'Waktu Show': '15:00-16:00', 'Hall': 1},
    {'Contract ID': 2, 'Nama Grup': 'RADIOHEAD', 'Nama Anggota': ['THOM YORKE', 'JONNY GREENWOOD', 'COLIN GREENWOOD', 'ED O BRIEN', 'PHILIP SELWAY'], 'Hari Show': 'SAT', 'Waktu Show': '15:30-16:30', 'Hall': 2},
    {'Contract ID': 3, 'Nama Grup': 'FOO FIGHTERS', 'Nama Anggota': ['DAVE GROHL', 'NATE MENDEL', 'PAT SMEAR', 'TAYLOR HAWKINS', 'CHRIS SHIFLETT'], 'Hari Show': 'SUN', 'Waktu Show': '17:00-18:00', 'Hall': 3},
    {'Contract ID': 4, 'Nama Grup': 'RED HOT CHILI PEPPERS', 'Nama Anggota': ['ANTHONY KIEDIS', 'FLEA', 'CHAD SMITH', 'JOHN FRUSCIANTE'], 'Hari Show': 'SUN', 'Waktu Show': '18:00-19:00', 'Hall': 4},
    {'Contract ID': 5, 'Nama Grup': 'MUSE', 'Nama Anggota': ['MATT BELLAMY', 'CHRIS WOLSTENHOLME', 'DOMINIC HOWARD'], 'Hari Show': 'FRI', 'Waktu Show': '16:00-17:30', 'Hall': 5},
    {'Contract ID': 6, 'Nama Grup': 'MUSE', 'Nama Anggota': ['MATT BELLAMY', 'CHRIS WOLSTENHOLME', 'DOMINIC HOWARD'], 'Hari Show': 'FRI', 'Waktu Show': '18:00-19:30', 'Hall': 6},
    {'Contract ID': 7, 'Nama Grup': 'FOO FIGHTERS', 'Nama Anggota': ['DAVE GROHL', 'NATE MENDEL', 'PAT SMEAR', 'TAYLOR HAWKINS', 'CHRIS SHIFLETT'], 'Hari Show': 'SAT', 'Waktu Show': '17:00-18:30', 'Hall': 8},
    {'Contract ID': 8, 'Nama Grup': 'TOTO', 'Nama Anggota': ['STEVE LUKATHER', 'DAVID PAICH', 'JOSEPH WILLIAMS', 'SIMON PHILLIPS'], 'Hari Show': 'FRI', 'Waktu Show': '18:00-19:00', 'Hall': 4},
    {'Contract ID': 9, 'Nama Grup': 'PROJECT POP', 'Nama Anggota': ['OONK', 'GUGUM', 'TIKA', 'YOSI', 'UDJO', 'GEBBY'], 'Hari Show': 'SAT', 'Waktu Show': '14:00-15:00', 'Hall': 10},
    {'Contract ID': 10, 'Nama Grup': 'RAN', 'Nama Anggota': ['RAYI PUTRA', 'ASTONO ANDIKO', 'NINO KAYAM'], 'Hari Show': 'SUN', 'Waktu Show': '15:00-16:00', 'Hall': 9},
    {'Contract ID': 11, 'Nama Grup': 'INCOGNITO', 'Nama Anggota': ['JEAN-PAUL BLUEY MAUNICK', 'MOHAMMED NDIAYE', 'FRANCIS HILTON', 'MATT COOPER'], 'Hari Show': 'SUN', 'Waktu Show': '16:30-17:30', 'Hall': 7},
    {'Contract ID': 12, 'Nama Grup': 'TRIBUTE WITH INDONESIAN SINGERS', 'Nama Anggota': ['STEVE LUKATHER','JEAN-PAUL BLUEY MAUNICK','RAYI PUTRA', 'ASTONO ANDIKO', 'NINO KAYAM'], 'Hari Show': 'SUN', 'Waktu Show': '16:00-17:30', 'Hall': 6}
]

def menambah_show ():
    contract_ID = pyip.inputNum("\nMasukkan Contract ID : ")

    for ID in program:
        if ID['Contract ID'] == contract_ID:
            print (colored(f"\nContract ID {contract_ID} sudah terdaftar. Silahkan kembali ke menu utama.","red"))
            return
                    
### tambah nama grup
    while True:
        nama_grup = pyip.inputStr("\nMasukkan Nama Grup :  ").strip().upper()
        for grup in program:
            if grup['Nama Grup'].strip().upper() == nama_grup:
                grup_sama = pyip.inputYesNo(prompt=(colored(f"\nGrup {nama_grup} sudah terdaftar. Yakin ingin ditambahkan? (Y/N) : ","red"))).strip()        
                if grup_sama == "yes":
                    break
                elif grup_sama == "no":
                    break             
        else:
            break
        if grup_sama == "yes" :
            break
### tambah jumlah anggota
    jumlah_anggota = pyip.inputNum("\nMasukkan Jumlah Anggota (1-25): ", min=1, max=25)
  
### tambah nama anggota    
    anggota_baru = []
    for i in range(1,jumlah_anggota+1):
        input_anggota = pyip.inputStr(f"\nMasukkan Nama Anggota {i}: ").strip().upper()
        
        anggota_exist = False
        for grup in program:
            if input_anggota in [anggota.strip().upper() for anggota in grup ['Nama Anggota']]:
                anggota_exist = True
                break
        
        if anggota_exist == True:
            confirm = pyip.inputYesNo(prompt=f"\nNama {input_anggota} sudah terdaftar. Yakin ingin ditambahkan? (Y/N): ")            
            if confirm == 'no':
                print(colored(f"{input_anggota} tidak ditambahkan.","red"))
                continue 

        anggota_baru.append(input_anggota) 
    print (colored(f"\nAnggota yang ditambahkan : {", ".join(anggota_baru)}.","green"))

## tambah hari show
    hari_show = pyip.inputChoice(['Fri','Sat','Sun'], prompt= "\nMasukkan Hari Show (Fri/Sat/Sun): ").strip().upper()
   
## tambah waktu show   
    while True:
        waktu_show = pyip.inputStr("\nMasukkan Waktu Show (HH:MM-HH:MM, contoh: 15:00-16:00): ").strip()
        if re.match(r'^\d{2}:\d{2}-\d{2}:\d{2}$', waktu_show):
            break
        else:
            print(colored("\nFormat waktu tidak valid. Silahkan coba lagi.", "red"))

## tambah hall show
    hall_show = pyip.inputNum("\nMasukkan Nomor Hall Show (1-10): ", min=1, max=10)

## append semua ke program    
    program.append({
        'Contract ID': contract_ID,
        'Nama Grup': nama_grup,
        'Nama Anggota': anggota_baru,
        'Hari Show': hari_show,
        'Waktu Show' : waktu_show,
        'Hall': hall_show
    })
    print(colored(f"\nShow berhasil di tambahkan ke dalam program","green"))

def melihat_show():

    while True:
        print(colored("\n📌 Pilih opsi untuk melihat show :", "blue"))
        print("1. Lihat show per Grup")
        print("2. Lihat show per Hari")
        print("3. Lihat show per Hall")
        print("4. Lihat keseluruhan")
        print("5. Kembali ke Menu Utama")
        
        pilihan = pyip.inputNum(colored("\nMasukkan opsi 1-5: ", "blue"), min=1, max=5)

        table_data = []

        if pilihan == 1:
            grup = pyip.inputStr("\nLihat show untuk Grup: ").strip().upper()
            headers_1 = [Fore.BLUE + "Grup", "Nama Anggota", "Hari", "Waktu", "Hall" + Style.RESET_ALL]

            for show in program:
                if show['Nama Grup'].strip().upper() == grup:
                    table_data.append([show['Nama Grup'], '\n'.join(show['Nama Anggota']), show['Hari Show'], show['Waktu Show'],show['Hall']])        
            if not table_data:
                print(f"\nNama Grup {grup} tidak terdaftar.")
            else:
                print(tabulate(table_data, headers_1, tablefmt="mixed_grid"))
            
        elif pilihan == 2:
            day = pyip.inputChoice(['Fri','Sat','Sun'], prompt= "\nLihat show di Hari (Fri/Sat/Sun) : ").strip().upper()
            headers_2 = [Fore.BLUE + "Hari", "Grup", "Nama Anggota", "Waktu", "Hall" + Style.RESET_ALL]
            for show in program:
                if show['Hari Show'].strip().upper() == day:
                    table_data.append([show['Hari Show'], show['Nama Grup'], '\n'.join(show['Nama Anggota']), show['Waktu Show'], show['Hall']])            
            table_data.sort(key=lambda x: x[3])
            print(tabulate(table_data, headers_2, tablefmt="mixed_grid")) 

        elif pilihan == 3:
            hall = pyip.inputNum("\nLihat show di Hall nomor : ", min=1, max=10)
            headers_3 = [Fore.BLUE + "Hall", "Grup", "Nama Anggota", "Hari", "Waktu" + Style.RESET_ALL]
            for show in program:
                if show['Hall'] == hall:
                    table_data.append([show['Hall'], show['Nama Grup'], '\n'.join(show['Nama Anggota']), show['Hari Show'], show['Waktu Show']])                                                                        
            table_data.sort(key=lambda x: x[1])
            print(tabulate(table_data, headers_3, tablefmt="mixed_grid"))        
       
        elif pilihan == 4:
            headers_4 = [Fore.BLUE + "Contract ID", "Grup", "Nama Anggota", "Hari", "Waktu", "Hall" + Style.RESET_ALL]
            for show in program:
                table_data.append([show['Contract ID'], show['Nama Grup'], '\n'.join(show['Nama Anggota']), show['Hari Show'], show['Waktu Show'],show['Hall']])  
            table_data.sort(key=lambda x: x[1])
            print(tabulate(table_data, headers_4, tablefmt="mixed_grid"))    

        elif pilihan == 5:
            break 

def table_contractID (ID):
    table_data = [[ID['Contract ID'], ID['Nama Grup'], '\n'.join(ID['Nama Anggota']), ID['Hari Show'], ID['Waktu Show'], ID['Hall']]]
    headers_ubah_program = [Fore.BLUE + "Contract ID", "Nama Grup", "Nama Anggota", "Hari Show", "Waktu Show", "Hall" + Style.RESET_ALL]
    print(tabulate(table_data, headers_ubah_program, tablefmt = "mixed_grid"))

def mengubah_show():
    contract_ubah = pyip.inputNum("\nMasukkan Contract ID show yang akan di ubah: ")
   
    for ID in program:
        if ID['Contract ID'] == contract_ubah:
            table_contractID(ID)      
            break          
    else:
        print ("\nContract ID tidak terdaftar. Silahkan ke menu utama untuk menambahkan.")
        return #exit if the contract is not found. Exitnya whole function. Jadi balik ke function sebelum ini apa. 
           
    def tampilan_mengubah_program():
        while True:
            tampilupdate = pyip.inputYesNo(prompt=f"\nIngin tampilkan hasil perubahan? (Y/N) : ")     
            if tampilupdate == "yes":
                table_contractID(ID)
                break
            elif tampilupdate == "no":
                break        
    # menu ubah 
    while True:
        print(colored("\n📌 Pilih opsi untuk mengubah show :", "blue"))
        print ("\n1. Ubah Nama Grup")
        print ("2. Ubah Nama Anggota")
        print ("3. Ubah Hari Show")
        print ("4. Ubah Waktu Show")
        print ("5. Ubah Hall Show")
        print ("6. Kembali ke Menu Utama")

        menu_ubah = pyip.inputInt(prompt=colored("\nMasukkan opsi ubah 1-6: ","blue"), min=1, max=6)

        if menu_ubah == 1:
            grup_sekarang = ID['Nama Grup'].strip().upper()
            print (f"\nNama Grup saat ini : {grup_sekarang}")
            menu_ubah_1 = pyip.inputStr("\nMasukkan Nama Grup yang baru:  ").strip().upper()
            ID ['Nama Grup'] = menu_ubah_1
            print (colored(f"\nNama Grup berhasil diubah menjadi {menu_ubah_1}","green", attrs=["bold"]))  
            tampilan_mengubah_program()
                 
        elif menu_ubah == 2:
            anggota_sekarang = ID['Nama Anggota']
            print (f"\nNama Anggota saat ini : {anggota_sekarang}")
            menu_ubah_2 = pyip.inputStr("\nMasukkan Nama Anggota yang ingin di ubah :  ").strip().upper()       
            
            if menu_ubah_2 in [anggota.strip().upper() for anggota in anggota_sekarang]:
                anggota_baru = pyip.inputStr("Masukkan Nama Anggota yang baru:  ").strip().upper()
                #cari index dulu, soalnya list.
                index = [anggota.strip().upper() for anggota in anggota_sekarang].index(menu_ubah_2) 
                ID['Nama Anggota'][index] = anggota_baru            
                print(colored(f"Nama Anggota {menu_ubah_2} berhasil diubah menjadi {anggota_baru}.","green", attrs=["bold"]))  
                tampilan_mengubah_program()
              
            else: 
                print (f"\nNama Anggota {menu_ubah_2} belum terdaftar pada contract ID {ID['Contract ID']}")
    
        elif menu_ubah == 3:
            hari_sekarang = ID['Hari Show']
            print (f"\nGrup {ID['Nama Grup']} saat ini show di Hari : {hari_sekarang}")
            menu_ubah_3 = pyip.inputChoice(['Fri','Sat','Sun'], prompt= "\nMasukkan Hari Show yang baru (fri/sat/sun): ").strip().upper()
            ID ['Hari Show'] = menu_ubah_3
            print (colored(f"\nGrup {ID['Nama Grup']} berhasil diubah menjadi show di Hari {menu_ubah_3}","green", attrs=["bold"]))                        
            tampilan_mengubah_program()       

        elif menu_ubah == 4:
            waktu_sekarang = ID['Waktu Show']
            print (f"\nGrup {ID['Nama Grup']} saat ini show pada pukul : {waktu_sekarang}")
            menu_ubah_4 = pyip.inputStr("\nMasukkan Waktu Show yang baru (contoh: 15:00-16:00) : ").strip()
            ID ['Waktu Show'] = menu_ubah_4
            print (colored(f"\nGrup {ID['Nama Grup']} berhasil diubah menjadi show pada pukul {menu_ubah_4}","green", attrs=["bold"]))                        
            tampilan_mengubah_program()       

        elif menu_ubah == 5:
            hall_sekarang = ID['Hall']
            print (f"\nHall Show saat ini : Hall {hall_sekarang}")         
            menu_ubah_4 = pyip.inputNum("\nMasukkan Nomor Hall yang baru : ", min=1, max=10)
            ID ['Hall'] = menu_ubah_4
            print (colored(f"\nHall Show berhasil diubah menjadi Hall {menu_ubah_4}","green", attrs=["bold"]))            
            tampilan_mengubah_program()  
            
        elif menu_ubah == 6:
            return  


def menghapus_show():
    contract_ID_hapus = pyip.inputNum("Masukkan Contract ID show yang ingin di hapus : ")

    for ID in program:
        if ID['Contract ID'] == contract_ID_hapus:
            table_contractID(ID)
            confirm_hapus = pyip.inputYesNo(prompt=f"Yakin ingin menghapus show di atas? (Y/N): ")            
            if confirm_hapus == "yes":
                program.remove(ID)
                print(colored(f"\nShow dengan Contract ID {contract_ID_hapus} berhasil dihapus.\n","green"))
                break
            elif confirm_hapus == "no":
                print(colored(f"\nShow tidak dihapus. Silahkan kembali ke menu utama.\n", "red"))
                break
    else:
        print(f"\nContract ID {contract_ID_hapus} tidak terdaftar.")
        return
        
                        
def cek_konflik():
    print("\n📌 Menu ini digunakan untuk melihat apakah ada potensi konflik (show di waktu yang bersamaan) dari grup atau anggota tertentu.\n   Jika ada show yang berpotensi konflik, segera konfirmasi ke Artist Manager❗")

    while True:
        print("\n1. Cek Grup tertentu ")
        print("2. Cek Anggota tertentu")
        print("3. Cek Semua Grup")
        print("4. Cek Semua Anggota")
        print("5. Kembali ke Menu Utama")

        menu_konflik = pyip.inputNum(colored("\nMasukkan Opsi Cek Konflik (1-5) : ","blue"), min=1, max=5)
        headers = [Fore.BLUE + "Contract ID", "Nama Grup", "Nama Anggota", "Hari Show", "Waktu Show", "Hall" + Style.RESET_ALL]

        if menu_konflik == 1:               
            grup_cek = pyip.inputStr("\nMasukkan Nama Grup yang ingin di Cek : ").strip().upper()
            table_data = [] 
            grup_show_count = 0

            for grup in program:
                if grup['Nama Grup'].strip().upper() == grup_cek:
                    grup_show_count += 1
                    table_data.append([grup['Contract ID'], grup['Nama Grup'], '\n'.join(grup['Nama Anggota']), grup['Hari Show'], grup['Waktu Show'], grup['Hall']])                    
                    table_data.sort(key=lambda x: x[3])

            if grup_show_count == 0:
                print(f"\nNama Grup {grup_cek} tidak terdaftar dalam program.")
            else:
                print(tabulate(table_data, headers, tablefmt="mixed_grid"))
                print(f"\nNama Grup {grup_cek} memiliki {grup_show_count} show dalam program.")
                continue     

        if menu_konflik == 2:               
            anggota_cek = pyip.inputStr("\nMasukkan Nama Anggota yang ingin di Cek : ").strip().upper()
            table_data = [] 
            anggota_show_count = 0
            for anggota in program:
                if anggota_cek in [nama.strip().upper() for nama in anggota['Nama Anggota']]:
                    anggota_show_count += 1
                    table_data.append([anggota['Contract ID'], anggota['Nama Grup'], '\n'.join(anggota['Nama Anggota']), anggota['Hari Show'], anggota['Waktu Show'], anggota['Hall']])                    
                    table_data.sort(key=lambda x: x[3])
            if anggota_show_count == 0:
                print(f"\nNama Anggota {anggota_cek} tidak terdaftar dalam program.")
            else:
                print(tabulate(table_data, headers, tablefmt="mixed_grid"))
                print(f"\nNama Anggota {anggota_cek} memiliki {anggota_show_count} show dalam program.")
                continue

        # semua grup
        if menu_konflik == 3:
            grup_shows = {}
            for show in program:
                grup_upper = show['Nama Grup'].strip().upper()
                if grup_upper not in grup_shows:
                    grup_shows[grup_upper] = []  
                grup_shows[grup_upper].append({
                    'Contract ID' : show['Contract ID'],
                    'Nama Anggota': '\n'.join(show['Nama Anggota']),  
                    'Hari Show': show['Hari Show'],
                    'Waktu Show': show['Waktu Show'],
                    'Hall': show['Hall']
                })
            # pilih 2 or lebih show
            for grup, shows in grup_shows.items():
                if len(shows) >= 2:
                    table_data = []
                    for show in shows:
                        table_data.append([show['Contract ID'],grup, show['Nama Anggota'], show['Hari Show'], show['Waktu Show'], show['Hall']])
                        table_data.sort(key=lambda x: x[3])
                    headers_new_grup = [Fore.BLUE + "Contract ID", "Nama Grup", "Nama Anggota", "Hari Show", "Waktu Show", "Hall" + Style.RESET_ALL]
                    print(f"\nPotensi konflik pada Nama Grup: {grup}")
                    print(tabulate(table_data, headers_new_grup, tablefmt="mixed_grid"))

        #per nama anggota, all
        if menu_konflik == 4:               
            anggota_shows = {}
            for show in program:
                for anggota in show['Nama Anggota']:
                    anggota_upper = anggota.strip().upper()
                    if anggota_upper not in anggota_shows:
                        anggota_shows[anggota_upper] = []
                    anggota_shows[anggota_upper].append({
                        'Contract ID' : show['Contract ID'],
                        'Nama Grup': show['Nama Grup'],
                        'Hari Show': show['Hari Show'],
                        'Waktu Show': show['Waktu Show'],
                        'Hall': show['Hall']
                    })
            # anggota yg 2 or more
            for anggota, shows in anggota_shows.items():
                if len(shows) >= 2:  # Only show members who have 2 or more shows
                    table_data = []
                    for show in shows:
                        table_data.append([show['Contract ID'],anggota, show['Nama Grup'], show['Hari Show'], show['Waktu Show'], show['Hall']])
                        table_data.sort(key=lambda x: x[3])

                    headers_new = [Fore.BLUE + "Contract ID" , "Nama Anggota", "Nama Grup", "Hari Show", "Waktu Show", "Hall" + Style.RESET_ALL]
                    print(f"\nPotensi konflik untuk Nama Anggota: {anggota}")
                    print(tabulate(table_data, headers_new, tablefmt="mixed_grid"))
    
        if menu_konflik == 5:
            break               

def login_menu():
    while True:
        out_login = False
        admin_password = "2024"
        role = pyip.inputMenu(['Admin', 'Regular'], prompt=(colored("Welcome to Admin Portal PyFest 2024! Silahkan Log In.\n\nAnda akan login sebagai : \n","blue")), numbered = True)

        if role == 'Admin':
            while True:
                password_attempt = pyip.inputPassword(prompt=(colored("\nSilahkan masukkan password Admin : ","green")))
                if password_attempt == admin_password:
                    print("\nHalo Admin Program PyFest 2024!")
                    out_login = True
                    break
                else:
                    try_again = pyip.inputYesNo(prompt=(colored("\nPassword salah. Ingin mencoba lagi? (Y/N): \n","red")))
                    if try_again == "no":
                        break      
        else:
            out_login = True

        if out_login == True:
            break
    #after login/masukin role.
    while True:
        print(colored("\n🎉 Welcome to Py Music Festival 2024 🎉\n", "magenta"))        
        if role == 'Admin':
            print("1. Menambah Show")    
            print("2. Melihat Show")
            print("3. Mengubah Show")
            print("4. Menghapus Show")
            print("5. Cek Show Konflik")
            print("6. Keluar")
        else:
            print("1. Melihat Show")
            print("2. Cek Show Konflik")
            print("3. Keluar")
            
        if role == 'Admin':
            welcome = pyip.inputNum(colored("\nMasukkan pilihan menu 1-6: ","blue"), min=1, max=6)
        else:
            welcome = pyip.inputNum(colored("\nMasukkan pilihan menu 1-3: ","blue"), min=1, max=3)
        
        #untuk menu admin
        if role == 'Admin':
            if welcome == 1:
                menambah_show()
            elif welcome == 2:
                melihat_show()
            elif welcome == 3:
                mengubah_show()
            elif welcome == 4:
                menghapus_show()
            elif welcome == 5:
                cek_konflik()
            elif welcome == 6:
                print ("\nTerima kasih! Sampai jumpa 👋")
                return
        #untuk menu reguler
        else:
            if welcome == 1:
                melihat_show()
            elif welcome == 2:
                cek_konflik()
            elif welcome == 3:
                print ("\nTerima kasih! Sampai jumpa 👋")
                return
                
login_menu()