from telegram.ext import Updater, CommandHandler,MessageHandler,Filters,CallbackQueryHandler,ConversationHandler
from function import *



conv_handler = ConversationHandler(
    entry_points = [
        CommandHandler('start',start)
    ],
    states = {
        'state_main_command':[
            CommandHandler('start',start),
            MessageHandler(Filters.text,main_command),
            
        ],
        'state_namaz_time':[
            CommandHandler('start',start),
            MessageHandler(Filters.text,namaz_time)
        ],
        'state_admin_back':[
            CallbackQueryHandler(admin_back)
        ],
        'state_local_back':[
            MessageHandler(Filters.text,local_back)
        ],
        'state_tasbeh':[
            CallbackQueryHandler(tasbeh_command)
        ],
        'state_tasbeh2':[
            CallbackQueryHandler(tasbeh_command2)
        ],
        'state_tasbeh3':[
            CallbackQueryHandler(tasbeh_command3)
        ],
        'state_command_admin':[
            CommandHandler('start',start),
            MessageHandler(Filters.text,admin_command)
        ],
        'state_admin_namaz_time':[
            CommandHandler('start',start),
            MessageHandler(Filters.text,admin_namaz_time)
        ],
        "state_namaz_time_name":[
            CommandHandler('start',start),
            MessageHandler(Filters.text,admin_namaz_time_name)
        ],
        "state_add_namaz_time":[
            CommandHandler('start',start),
            MessageHandler(Filters.photo,add_namaz_time)
        ],
        "state_namaz_time_name2":[
            CommandHandler('start',start),
            MessageHandler(Filters.text,admin_namaz_time_name2)
        ],
        "state_add_namaz_time2":[
            CommandHandler('start',start),
            MessageHandler(Filters.photo,add_namaz_time2)
        ],
        "state_get_answer":[
            CommandHandler('start',start),
            MessageHandler(Filters.all,get_answer)
        ],
        "state_add_juma_maruza":[
            CommandHandler('start',start),
            MessageHandler(Filters.text,add_juma_maruza)
        ],
        "state_add_juma_maruza_audio":[
            CommandHandler('start',start),
            MessageHandler(Filters.all,add_juma_maruza_audio)
        ],
        "state_send_reklama":[
            CommandHandler('start',start),
            MessageHandler(Filters.all,send_reklama)
        ],
        "state_send_answer":[
            CommandHandler('start',start),
            MessageHandler(Filters.text,send_answer_the_ques)
        ],
        "state_send_main_answer":[
            CommandHandler('start',start),
            MessageHandler(Filters.all,send_main_answer)
        ],
        "state_ok_get_ans":[
            CallbackQueryHandler(ok_button)
        ]


    },

    fallbacks = [
        CommandHandler('start',start)
    ]
)
#o'zgarish_7
token = 'Your Token Here'
updater = Updater(token)
updater.dispatcher.add_handler(conv_handler)


updater.start_polling()
updater.idle()  