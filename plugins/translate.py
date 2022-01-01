from deep_translator import GoogleTranslator
from pyrogram import Client, filters

# Filters sample
# async def testFilter(flt, client, msg):
#     if msg.text == 'سلام':
#         await msg.reply("سلام خوبی !")
#         return False
#     else:
#         return True

# filter_test = filters.create(testFilter)


async def check_member(_, client, message):
    try:
        user_id = message.from_user.id
        user = await client.get_chat_member('samyborder', user_id)
        if user.status in ['member', 'creator', 'administrator']:
            return True
    except:
        message.reply("""
                        
                        شما هنوز داخل من عضو نیستید اول باید عضو شوید 
                        
                        ❤ @samyBorder
                        
                        """)
        return False


check_member_filter = filters.create(check_member)


@Client.on_message(filters.private & (filters.text & check_member_filter), group=1)
async def translate(c, m):
    # مترجم ساختن
    translator = GoogleTranslator('auto', 'fa')
    translator_to_en = GoogleTranslator('auto', 'en')
    # ترجمه متن
    translated = translator.translate(m.text)
    translated_to_en = translator_to_en.translate(m.text)
    # ارسال ترجمه شده
    await m.reply_text(translated)
    await m.reply_text(translated_to_en)

# /tr_en hello
# سلام

# /tr_fa سلام
# hello
