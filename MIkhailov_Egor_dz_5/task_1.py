
def write_in_file(text):
    with open("file_for_task1.txt", 'w', encoding='utf-8') as f:
        f.write(f'{text}\n')

user_text =True
while user_text:
    user_text = input('введите текст \n')
    if user_text:
        write_in_file(user_text)
    # else:
    #     print(user_text)
