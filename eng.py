import random
from colorama import Fore, Style
import os

clear = lambda: os.system('cls')
# clear()
file_path = 'vocab.txt'  
data_dict = {}
with open(file_path, 'a', encoding='utf-8') as file:
                    file.write("\n")
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        parts = line.strip().split(':')
        if len(parts) == 2:
            key, value = parts
            data_dict[key.strip().lower()] = value.strip().lower()

while True:
    print("\n" + Fore.CYAN + "------------------------------")
    print("|            " + Fore.YELLOW + "MENU" + Fore.CYAN + "            |")
    print("------------------------------")
    print(Fore.RED + "| " + Style.RESET_ALL + "1. Tra cứu & thêm từ vựng" + " " * 2 + Fore.RED + "|")
    print(Fore.RED + "| " + Style.RESET_ALL + "2. Dò bài" + " " * 18 + Fore.RED + "|")
    print(Fore.RED + "| " + Style.RESET_ALL + "3. Sắp xếp, lưu & thoát" + " " * 4 + Fore.RED + "|")
    print("------------------------------")
    choice = input(Style.RESET_ALL + "Chọn chức năng (1-3): ")
    
    if choice == '1':
        while True:
            input_word = input("Nhập từ (Nhấn " + Fore.RED + "ENTER " + Style.RESET_ALL + "để dừng): ").lower()
            if not input_word:
                print("Trở lại Menu chính.")
                break

            matched_word = None
            for word in data_dict:
                if input_word in word or word in input_word:
                    matched_word = word
                    break

            if matched_word:
                print("Nghĩa của từ " + Fore.GREEN + matched_word + Fore.WHITE + " là: " + Fore.YELLOW + data_dict[matched_word] + Style.RESET_ALL + "\n(" + Fore.RED + "nhập 1 để xóa từ này, " + Fore.GREEN + "ENTER để tiếp tục" + Style.RESET_ALL + "): ")
                
                # Thêm lựa chọn xóa từ
                delete_choice = input().lower()
                
                if delete_choice == '1':
                    # Xóa từ khỏi từ điển
                    del data_dict[matched_word]
                    
                    # Cập nhật lại file sau khi xóa từ
                    sorted_data = sorted(data_dict.items())
                    
                    with open(file_path, 'w', encoding='utf-8') as file:
                        for key, value in sorted_data:
                            file.write(f"{key}: {value}\n")

                    print("Từ " + Fore.RED + matched_word + Style.RESET_ALL + " đã được xóa khỏi từ điển.")
                    print("\n==============================\n")
                else:
                    print("==============================\n")

            else:
                input_meaning = input("Từ " + Fore.RED + input_word + Style.RESET_ALL + " không có trong từ điển. Bạn có muốn thêm từ này vào từ điển không?:\n(" + Style.RESET_ALL + Fore.GREEN + "ENTER thêm từ," + Fore.RED +" 1 thoát): " + Style.RESET_ALL)
                
                if input_meaning.lower() == '1':
                    print("Từ " + Fore.RED + input_word + Style.RESET_ALL +" không được thêm vào từ điển.")
                    print("\n==============================\n")

                else:  # enter - thêm từ
                    input_meaning = input("Vui lòng nhập nghĩa của từ " + Fore.GREEN + input_word + Style.RESET_ALL + " (để trống = huỷ thêm):")
                    
                    if not input_meaning.strip():  # Kiểm tra nếu nghĩa để trống
                        print("Từ " + Fore.RED + input_word + Style.RESET_ALL +" không được thêm vào từ điển.")
                        print("\n==============================\n")
                    else:
                        data_dict[input_word] = input_meaning

                        # Sắp xếp từ điển theo từ khóa
                        sorted_data = sorted(data_dict.items())

                        # Ghi đè toàn bộ từ điển đã sắp xếp vào file
                        with open(file_path, 'w', encoding='utf-8') as file:
                            for key, value in sorted_data:
                                file.write(f"{key}: {value}\n")

                        print("Từ " + Fore.GREEN + input_word + Style.RESET_ALL + " đã được thêm vào từ điển và file đã được sắp xếp.")
                        print("\n==============================\n")

    

    elif choice == '2':
        while True:
            random_word = random.choice(list(data_dict.keys()))
            print("Từ: " + Fore.GREEN + random_word + Style.RESET_ALL + " có nghĩa là gì? \n(" + Fore.GREEN + "Enter đã nhớ," + Fore.YELLOW + " 1 không nhớ, " + Fore.RED + " 2 xóa từ, " + Fore.BLUE + "3 THOÁT): " + Style.RESET_ALL, end='')
            know_meaning = input()

            if know_meaning == '3':
                print("Thoát chức năng Random từ vựng.")
                print("\n==============================\n")
                break

            elif know_meaning == '1':
                print("\n" + Fore.GREEN + f"{random_word}: " + Fore.YELLOW + data_dict[random_word] + Style.RESET_ALL)
                print("\n==============================\n")
                continue

            if know_meaning == '2':
                # Hỏi xác nhận trước khi xóa
                confirm_delete = input("Bạn có chắc muốn xóa từ " + Fore.GREEN + random_word + Style.RESET_ALL +" không? (y/n): ").lower()
                if confirm_delete == 'y':
                    # Xóa từ đã nhớ khỏi file
                    with open(file_path, 'r+', encoding='utf-8') as file:
                        lines = file.readlines()
                        file.seek(0)
                        for line in lines:
                            if not line.startswith(random_word + ":"):
                                file.write(line)
                        file.truncate()
                    print("Từ " + Fore.RED + random_word + Style.RESET_ALL +" đã được loại khỏi danh sách từ điển.")
                    print("\n==============================\n")
                else:
                    print("Từ " + Fore.GREEN + random_word + Style.RESET_ALL +" không bị xóa.")
                    print("\n==============================\n")
                continue

            else:
                continue

            
    elif choice == '3':
        sorted_data = sorted(data_dict.items())
        with open(file_path, 'w', encoding='utf-8') as file:
            for key, value in sorted_data:
                file.write(f"{key}: {value}\n")

        print("Dữ liệu đã được sắp xếp và ghi lại vào file.")
        print("\n==============================\n")
        break

    
    else:
        print(Fore.RED + "Lựa chọn không hợp lệ. Vui lòng chọn lại." + Style.RESET_ALL)
