from telegram import Update,ReplyKeyboardRemove
from telegram.ext import CallbackContext
from database import *
from button import *
import time


def start(update:Update,context:CallbackContext):
    #O'zgarish_1
    admins = ["Adminlarning telegram idlari"]

    if update.effective_user.id in admins:
        update.message.reply_text(f"<b>{update.effective_user.first_name} siz adminsiz 👇</b>", reply_markup = admin_panel_button(),parse_mode = "HTML")
        return "state_command_admin"
    else:
        update.message.reply_text(f"<b>Assalomu Alaykum {update.effective_user.first_name} botimizga xush kelibsiz. O'zingizga kerakli tugmalardan birini tanlang 👇</b>",reply_markup = main_button(),parse_mode = 'HTML')
        if get_user_id(update.effective_user.id):
            return 'state_main_command'
        else:
            insert_table_user(update.effective_user.id,update.effective_user.first_name)
            return 'state_main_command'








#### Asosiy Menu
def main_command(update:Update,context:CallbackContext):
    data = update.message.text

    if data == 'Namoz vaqtlari 🕔':
        update.message.reply_text('<b>Quyidagi tugmalardan birini tanlang 🔢↙️</b>',reply_markup = namaz_time_button(),parse_mode= 'HTML')
        return 'state_namaz_time'
            
    elif data == 'Savol yuborish❓':
        # update.message.reply_text("<b>Savol yuborish vaqtincha to'xtatilgan ❌</b>",parse_mode = "HTML")
        # return "state_main_command"
        update.message.reply_text('<b>Savolingizni matn ko\'rinishida yuboring</b>',parse_mode = 'HTML')
        context.user_data['user_id'] = update.effective_user.id
        return "state_get_answer"

    elif data=='Tasbeh 📿':
        update.message.reply_text('33 <-- سبحان الله. SubhanAllah',reply_markup = tasbeh_button1())
        context.user_data['soni'] = 0
        return 'state_tasbeh'

    elif data == 'Juma maruzasi mp3🎧':
        id = 1
        try:
            name = get_juma_maruza(id)[1]
            update.message.reply_text("Fayl yuklanguncha biroz kuting...")
            update.message.reply_audio(open(f"audio/{name}.mp3","rb"),caption = f"{name}.Juma maruzasi")
            return "state_main_command"
        except:
            update.message.reply_text("Audio fayl hali qo'shilmadi ❌")
            return "state_main_command"

    elif data =='Masjid haqida 💡':
        #O'zgarish_2
        xabar = f"""<b>Tekst uchun </b>"""
        # context.bot.send_message(chat_id=update.message.chat_id, text="<a href='https://www.google.com/'>Google</a>",parse_mode='HTML')
        update.message.reply_text(xabar,reply_markup = local_button(),parse_mode = "HTML")
        return 'state_local_back'
        

        
    elif data =='Ijtimoiy tarmoqlar 🌐':
        update.message.reply_text('<b>Ijtimoiy tarmoqlarimiz</b>',reply_markup = admin_button(), parse_mode = 'HTML')
        return 'state_admin_back'

### Asosiy menu








### Namoz Vaqtlari 
def namaz_time(update:Update,context:CallbackContext):
    data = update.message.text 
    if data == 'O\'zbekiston bo\'yicha 🇺🇿':
        try:
            photo_name1 = select_namaztime_uzb()[1]
            xabar2 = "O'zbekiston bo'yicha 🇺🇿"
            update.message.reply_photo(open(f"uzb_photos/{photo_name1}.jpg",'rb'),caption = f"<b>{xabar2}\n{photo_name1} kungi namoz vaqtlari</b>",parse_mode = "HTML")
        except:
            photo_name1 = select_namaztime_uzb()[1]
            xabar2 = "O'zbekiston bo'yicha 🇺🇿"
            update.message.reply_text(f"<b>{xabar2}\n{photo_name1} kungi namoz vaqtlari</b>",parse_mode = "HTML")
                
    elif data == 'Poshshopirim masjidi 🕌':
        try:
            photo_name2 = select_namaztime_posh()[1]
            xabar = "Poshshopirim masjidi  🕌"
            update.message.reply_photo(open(f"posh_photos/{photo_name2}.jpg",'rb'),caption = f"<b>{xabar}\n{photo_name2} kungi namoz vaqtlari</b>",parse_mode = "HTML")
        except:
            photo_name2 = select_namaztime_posh()[1]
            xabar = "Poshshopirim masjidi  🕌"
            update.message.reply_text(f"<b>{xabar}\n{photo_name2} kungi namoz vaqtlari</b>",parse_mode = "HTML")
    elif data=="Orqaga 🔙":
        update.message.reply_text("<b>Kerakli tugmalardan birini tanlang 👇</b>",reply_markup = main_button(),parse_mode = "HTML")
        return 'state_main_command'
    






#### Orqaga qismlari         
def admin_back(update:Update,context:CallbackContext):
    query = update.callback_query
    data = query.data
    try:
        if data== 'admin_back':
            query.message.delete()
            query.message.reply_text("<b>Kerakli tugmalardan birini tanlang 👇</b>",reply_markup = main_button(),parse_mode = "HTML")
            return 'state_main_command'
    except:
        update.message.reply_text("Noto'g'ri xabar ❌")
        return "state_admin_back"

def local_back(update:Update,context:CallbackContext):
    data = update.message.text
    if data == 'Orqaga 🔙':
        update.message.reply_text("<b>Kerakli tugmalardan birini tanlang 👇</b>",reply_markup = main_button(),parse_mode = "HTML")
        return 'state_main_command'
    







#### Tasbeh Bo'limi 
def tasbeh_command(update:Update,context:CallbackContext):
    query = update.callback_query
    data = query.data
    try:
        if data == 'tasbeh_back1':
            query.message.delete()
            query.message.reply_text("<b>Kerakli tugmalardan birini tanlang 👇</b>",reply_markup = main_button(),parse_mode = "HTML")
            return 'state_main_command'
        elif data=='zikr1' :  
            soni = context.user_data['soni']+1
            context.user_data['soni'] = soni
            query.message.edit_reply_markup(reply_markup = tasbeh_button1(soni))
            if context.user_data['soni']==33:
                query.message.delete()
                query.message.reply_text("33 <-- الحمد لله Alhamdulillah",reply_markup = tasbeh_button2())
                return 'state_tasbeh2'
        context.user_data['soni2'] = 0
    except:
        update.message.reply_text("Noto'g'ri xabar ❌")
        return "state_tasbeh"
delete_uzb
def tasbeh_command2(update:Update,context:CallbackContext):
    query = update.callback_query
    data = query.data
    try:
        if data == 'tasbeh_back2':
            query.message.delete()
            query.message.reply_text("<b>Kerakli tugmalardan birini tanlang 👇</b>",reply_markup = main_button(),parse_mode = "HTML")
            return 'state_main_command'
        elif data =='zikr2':
            soni = context.user_data['soni2']+1
            context.user_data['soni2'] = soni
            query.message.edit_reply_markup(reply_markup = tasbeh_button2(soni))
            if context.user_data['soni2']==33:
                query.message.delete()
                query.message.reply_text("33 <-- الله أكبر Allohu Akbar",reply_markup = tasbeh_button3())
                return 'state_tasbeh3'
        context.user_data['soni3'] = 0
    except:
        update.message.reply_text("Noto'g'ri xabar ❌")
        return "state_tasbeh2"


def tasbeh_command3(update:Update,context:CallbackContext):
    query  = update.callback_query
    data = query.data
    try:
        if data == 'tasbeh_back3':
            query.message.delete()
            query.message.reply_text("<b>Kerakli tugmalardan birini tanlang 👇</b>",reply_markup = main_button(),parse_mode = "HTML")
            return 'state_main_command'
        elif data == 'zikr3':
            soni = context.user_data['soni3']+1
            context.user_data['soni3'] = soni
            query.message.edit_reply_markup(reply_markup = tasbeh_button3(soni))
            if context.user_data['soni3'] == 33:
                query.message.delete()
                query.message.reply_text("<b>La ilaha illallohu vahdahu la sharika lah, lahul mulku va lahul hamd. Va huva 'ala kulli shayin qodir.</b>",reply_markup = main_button(),parse_mode = 'HTML')
                return 'state_main_command'
    except:
        update.message.reply_text("Noto'g'ri xabar ❌")
        return "state_tasbeh3"
####Tasbeh bo'limi




        


### Admin Panel ###

def admin_command(update:Update, context:CallbackContext):
    data = update.message.text
    #O'zgarish_3
    main_admin  = ["Adminlarning idlari"]
    if data == '➕ Namoz vaqti 🕔':
        if update.effective_user.id in main_admin:
            update.message.reply_text("<b>Manzilni tanlang</b> 👇",reply_markup = namaz_time_button_admin(),parse_mode = "HTML")
            return 'state_admin_namaz_time'
        else:
            update.message.reply_text("Photo is already added ✅ ")
            return "state_command_admin"

    elif data=="➕ Juma maruzasi mp3🎧":
        if update.effective_user.id in main_admin:
            update.message.reply_text("<b>Maruza sanasini yuboring.\n(kun.oy.yil)</b>",parse_mode = "HTML")
            return "state_add_juma_maruza"
        else:
            update.message.reply_text("File audio already added ✅")
            return "state_command_admin"

    elif data == "Reklama📱":
        update.message.reply_text("Reklama vaqtincha to'xtatilgan ❌")
        return "state_command_admin"
        # if update.effective_user.id in main_admin:
        #     update.message.reply_text("Reklama yuborishingiz mumkin.",reply_markup = ReplyKeyboardRemove())
        #     return "state_send_reklama"
        # else:
        #     update.message.reply_text("Reklama vaqtincha to'xtatilgan ❌")
        #     return "state_command_admin"
        

    elif data == "Statistika 🧮":
        users = count_users()
        update.message.reply_text(f"<b>Botdagi obunachilar soni {len(users)} ta </b>",parse_mode = 'HTML')

    elif data == "Asosiy menu":
        update.message.reply_text(f"<b>Assalomu Alaykum {update.effective_user.first_name} botimizga xush kelibsiz. O'zingizga kerakli tugmalardan birini tanlang 👇</b>",reply_markup = main_button(),parse_mode = 'HTML')
        if get_user_id(update.effective_user.id):
            return 'state_main_command'
        else:
            insert_table_user(update.effective_user.id,update.effective_user.first_name)
            return 'state_main_command'
    elif data == "Savolga javob ❓":
        ans_admin = [1306354017,5714569660]
        if update.effective_user.id in ans_admin:
            update.message.reply_text("<b>Javobni yuborish uchun foydalanuvchi ID sini yuboring </b>",parse_mode = 'HTML')
            return "state_send_answer"
        else:
            update.message.reply_text("Sizda javob yuborish yoqilmagan ❌")
            return "state_command_admin"




def admin_namaz_time(update:Update,context:CallbackContext):
    data = update.message.text
    try:
        if  data == 'Poshshopirim vaqti bo\'yicha 🕌':
            update.message.reply_text("<b>Namoz vaqtlarini sanasi yuboring (kun.oy.yil)</b>",parse_mode = "HTML")
            return "state_namaz_time_name"

        elif data=='O\'zbekiston vaqti bo\'yicha 🇺🇿':
            update.message.reply_text("<b>Namoz vaqtlarini sanasi yuboring (kun.oy.yil)</b>",parse_mode = "HTML")
            return "state_namaz_time_name2"
    except:
        update.message.reply_text("Noto'g'ri xabar ❌")
        return "state_admin_namaz_time"
        

# Poshshopirim vati bo'yicha namoz vaqtlarini qo'shish
def admin_namaz_time_name(update:Update,context:CallbackContext):
    text = str(update.message.text)
    try:
        if len(text) == 10 and int(text[:2]) < 31 and len((text[6:]))==4 and len(text[3:5])==2 and 0<int(text[3:5])<=12:
            context.user_data['sana'] = text
            update.message.reply_text("<b>Rasm yuborishingiz mumkin</b>",parse_mode = 'HTML')
            return "state_add_namaz_time"
        else:
            update.message.reply_text("Noto'g'ri formatdagi sana. Qaytadan yuboring\n(namuna:02.02.2022) (kun.oy.yil)")
            return "state_namaz_time_name"
    except:
        update.message.reply_text("Noto'g'ri xabar ❌")
        return "state_namaz_time_name"

def add_namaz_time(update:Update,context:CallbackContext):
    nums =1 
    delete_posh(nums)
    update.message.photo[-1].get_file().download(f"posh_photos/{context.user_data['sana']}.jpg")
    add_image_time_posh(context.user_data['sana'])
    update.message.reply_text('<b>Namoz vaqtlari muvaffaqiyatli qo\'shildi ✅</b>',reply_markup = admin_panel_button(),parse_mode = "HTML")
    return 'state_command_admin'

# O'zbekiston vaqti bo'yicha namoz vaqtlarini qo'shish
def admin_namaz_time_name2(update:Update,context:CallbackContext):
    dat = str(update.message.text)
    try:
        if len(dat) == 10 and int(dat[:2]) < 31 and len((dat[6:]))==4 and len(dat[3:5])==2 and 0<int(dat[3:5])<=12:
            context.user_data['sana2'] = dat
            update.message.reply_text("<b>Rasm yuborishingiz mumkin</b>",parse_mode = 'HTML')
            return "state_add_namaz_time2"
        else:
            update.message.reply_text("Noto'g'ri formatdagi sana. Qaytadan yuboring\n(namuna:02.02.2022) (kun.oy.yil)")
            return "state_namaz_time_name2"
    except:
        update.message.reply_text("Noto'g'ri xabar ❌")
        return "state_namaz_time_name2"

def add_namaz_time2(update:Update,context:CallbackContext):
    num=1
    delete_uzb(num)
    update.message.photo[-1].get_file().download(f"uzb_photos/{context.user_data['sana2']}.jpg")
    add_image_time_uzb(context.user_data['sana2'])
    update.message.reply_text('<b>Namoz vaqtlari muvaffaqiyatli qo\'shildi ✅</b>',reply_markup = admin_panel_button(),parse_mode = "HTML")
    return 'state_command_admin'


# Juma Maruzasini qo'shish
def add_juma_maruza(update:Update,context:CallbackContext):
    text = str(update.message.text)
    try:
        if len(text) == 10 and 0 < int(text[:2]) < 31 and len((text[6:]))==4 and len(text[3:5])==2 and 0<int(text[3:5])<=12:
            update.message.reply_text("Audio formatdagi faylni yuboring")
            context.user_data['date_juma'] = text
            return "state_add_juma_maruza_audio"
        else:
            update.message.reply_text("Noto'g'ri formatdagi sana.Qaytadan yuboring\n(namuna:02.02.2022) (kun.oy.yil)")
            return "state_add_juma_maruza"
    except:
        update.message.reply_text("Noto'g'ri xabar ❌")
        return "state_add_juma_maruza"

     

def add_juma_maruza_audio(update:Update,context:CallbackContext):
    delete_juma_maruza(1)
    update.message.audio.get_file().download(f"audio/{context.user_data['date_juma']}.mp3")
    add_juma_maruza_name(context.user_data['date_juma'])
    update.message.reply_text("Audio fayl muvaffaqiyatli qo'shildi ✅",reply_markup = admin_panel_button())
    return "state_command_admin"



#### Admin Panel ####








# savol javob bo'limi

def get_answer(update:Update,context:CallbackContext):
    answer  = update.message.text
    try:
        if answer=="Namoz vaqtlari 🕔" or answer =="Savol yuborish❓" or answer == "Juma maruzasi mp3🎧" or answer == "Tasbeh 📿" or answer == "Masjid haqida 💡" or answer == "Ijtimoiy tarmoqlar 🌐":
            update.message.reply_text("<b>Xato savol ❌.\nSavolni matn ko'rinishida yuboring</b>",parse_mode = "HTML")
            return "state_get_answer"
        else:
            #o'zgarish_4
            context.bot.send_message(chat_id = "ID",text = f"{answer}\nID:{context.user_data['user_id']}")
            context.bot.send_message(chat_id = "ID", text = f"{answer}\nID:{context.user_data['user_id']}")
            update.message.reply_text("<b>Savolingiz yuborildi\nboshqa savolingiz bo'lmasa OK tugmasini bosing 👇</b>",reply_markup = ans_button() ,parse_mode = 'HTML')
            return "state_ok_get_ans"
    except:
        update.message.reply_text("Xato savol ❌.\nSavolni matn ko'rinishida yuboring")

def send_answer_the_ques(update:Update,context:CallbackContext):
    text = update.message.text
    
    if text.isdigit():
        #o'zgarish_5
        context.bot.send_message(chat_id = "ID",text = "Endi javobingizni yuboring")
        context.bot.send_message(chat_id = "ID",text = "Javob yuborilmoqda...")
        context.user_data['id'] = text
        return "state_send_main_answer"
    else:
        update.message.reply_text("Noto'g'ri ID,qayta yuboring")
        return "state_send_answer"
    
        
def send_main_answer(update:Update,context:CallbackContext):
    msg = update.message
    try:
        #o'zgarish_6
        context.bot.forward_message(context.user_data['id'],update.effective_user.id,msg.message_id)
        context.bot.send_message(chat_id = "ID", text = "Javob yetkazildi")
        context.bot.send_message(chat_id = "ID", text = "Javob yuborildi")
        return "state_command_admin"
    except:
        update.message.reply_text("<b>Bunday ID ega User topilmadi ❌\nQaytadan yuboring</b>",parse_mode = "HTML")
        return "state_send_answer"

def ok_button(update:Update,context:CallbackContext):
    query = update.callback_query
    data = query.data
    query.message.delete()
    if data == "ok":
        context.bot.answerCallbackQuery(query.id,"Botimizdan foydalanganingiz uchun rahmat 🤗",show_alert = True)
        return "state_main_command"
    elif data == 'retry':
        query.message.reply_text('<b>Savolingizni matn ko\'rinishida yuboring</b>',parse_mode = 'HTML')
        return "state_get_answer"


####Reklama qismi

def send_reklama(update:Update,context:CallbackContext):
    message = update.message.photo
    soni = 0
    while True:
        try:
            soni += 1 
            user = count_users()[soni]
            context.bot.send_photo(user[1],update.effective_user.id,message.message_id)
            if soni == len(count_users()):
                break 
        except:
            print("Xatolik")
    update.message.reply_text("Reklama yuborildi ✅",reply_markup = admin_panel_button())
    return "state_command_admin"

    
    
