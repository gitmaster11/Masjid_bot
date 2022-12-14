from telegram import ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup

def admin_panel_button():
    button = [
        ['โ Namoz vaqti ๐',"โ Juma maruzasi mp3๐ง"],
        ['Reklama๐ฑ','Statistika ๐งฎ'],
        ['Asosiy menu','Savolga javob โ']
    ]
    return ReplyKeyboardMarkup(button,resize_keyboard = True,one_time_keyboard = True)


def namaz_time_button_admin():
    button = [
        ['Poshshopirim vaqti bo\'yicha ๐'],
        ['O\'zbekiston vaqti bo\'yicha ๐บ๐ฟ']
    ]
    return ReplyKeyboardMarkup(button,resize_keyboard = True)

def main_button():
    button = [
        ['Namoz vaqtlari ๐','Savol yuborishโ'],
        ["Juma maruzasi mp3๐ง",'Tasbeh ๐ฟ'],
        ['Masjid haqida ๐ก','Ijtimoiy tarmoqlar ๐']
       
        
    ]
    return ReplyKeyboardMarkup(button,resize_keyboard = True)


def namaz_time_button():
    button= [
        ['O\'zbekiston bo\'yicha ๐บ๐ฟ'],
        ['Poshshopirim masjidi ๐'],
        ['Orqaga ๐']
    ]
    return ReplyKeyboardMarkup(button,resize_keyboard =True,one_time_keyboard = False)


def admin_button():
    button = [
        [InlineKeyboardButton("Gavhar Tv ๐บ",url = "https://youtube.com/channel/UCG3PTy4VamJvxu5cwVK2Qlg"),InlineKeyboardButton("Poshshopirim.uz ๐ฒ",url = 'https://t.me/poshshopirmuz')],
        [InlineKeyboardButton("Islom Sohili ๐ฒ", url = "https://t.me/islom_sohili"),InlineKeyboardButton("BookStore",url = "https://t.me/Delivery_bookbot")],
        [InlineKeyboardButton('Admin ๐จ๐ปโ๐ป 1', url = 'https://t.me/sabr_uchun'),InlineKeyboardButton('Admin ๐จ๐ปโ๐ป 2', url = 'https://t.me/Premium_N11')],
        [InlineKeyboardButton('Orqaga ๐', callback_data = 'admin_back')]
    ]
    return InlineKeyboardMarkup(button)

def local_button():
    button = [
        ['Orqaga ๐']
    ]
    return ReplyKeyboardMarkup(button,resize_keyboard = True)


def tasbeh_button1(soni = '0'):
    button = [  
        [InlineKeyboardButton(f'SubhanAllah --> [{soni}]', callback_data = 'zikr1')],
        [InlineKeyboardButton('Orqaga ๐', callback_data = 'tasbeh_back1')]
    ]
    return InlineKeyboardMarkup(button)

def tasbeh_button2(soni = '0'):
    button = [  
        [InlineKeyboardButton(f'Alhamdulillah --> [{soni}]', callback_data = 'zikr2')],
        [InlineKeyboardButton('Orqaga ๐', callback_data = 'tasbeh_back2')]
    ]
    return InlineKeyboardMarkup(button)

def tasbeh_button3(soni = '0'):
    button = [  
        [InlineKeyboardButton(f'Allohu Akbar --> [{soni}]', callback_data = 'zikr3')],
        [InlineKeyboardButton('Orqaga ๐', callback_data = 'tasbeh_back3')]
    ]
    return InlineKeyboardMarkup(button)

def ans_button():
    button = [
        [InlineKeyboardButton("๐",callback_data = "ok")],
        [InlineKeyboardButton("Yana savol yuborish ๐",callback_data = "retry")]
    ]
    return InlineKeyboardMarkup(button)