import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    HOME_BUTTONURL_UPDATES = environ.get("HOME_BUTTONURL_UPDATES", 'https://tnlink.in/ref/KarthikUK')
    START_TXT = environ.get("START_TXT", '''<b>Hello ๐๐ป {} โฅ๏ธ,\nI'm an Star Movies Tamil's Official Auto Filter Bot (Movie Search Bot) Maintained by <a href=https://t.me/Star_Moviess_Tamil><b></b>Star Movies Tamil</a>. We are Providing Tamil and Tamil Dubbed Movies. More Languages Coming Soon. Keep me Join to Our Official Channel to Receive Bot & Movies Updates in <a href=https://t.me/Star_Moviess_Tamil><b></b>Star Movies Tamil</a>. Check "๐ About" Button.</b>''')
    HELP_TXT = """<b>Hello ๐๐ป {} โฅ๏ธ,
I have that Features.
Create One Link This :
ยป I will Create For One Bot You. But Paid
ยป Contact Me <a href=https://t.me/HMTD_Karthik><b>Karthik</b></a></b>"""
    ABOUT_TXT = """<b><i>๐ค My Name : <a href=https://t.me/Star_Moviess_Bot><b>Star Movies Bot</b></a>\n
๐ง๐ปโ๐ป Developer : <a href=https://t.me/HMTD_Karthik><b>Karthik</b></a>\n
๐ Language : Pyrogram\n
๐ Framework : Python3\n
๐ก Hosted on : VPS\n
๐ข Updates Channel : <a href=https://t.me/Star_Moviess_Bot><b></b><b>Star Movies Tamil</a></b>\n</i>"""
    SOURCE_TXT = """<b>Create One Like This :</b>
ยป I will Create One Bot For You. But Paid<b>
ยป Contact Me</b> <a href=https://t.me/HMTD_Karthik><b>Karthik</b></a>"""
    MANUELFILTER_TXT = """<b>Help :</b> <b>Filters</b>

<b>- Filter is the feature were users can set automated replies for a particular keyword and Search Bot will respond whenever a keyword is found the message</b>

<b>NOTE :</b>
<b>1. Search Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.</b>

<b>Commands and Usage :</b>
<b>โข /filter - add a filter in chat
โข /filters - list all the filters of a chat
โข /del - delete a specific filter in chat
โข /delall - delete the whole filters in a chat (chat owner only)</b>"""
    BUTTON_TXT = """<b>Help :</b> <b>Buttons</b>

<b>- Search Bot Supports both url and alert inline buttons.</b>

<b>NOTE :</b>
<b>1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Search Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format</b>

<b>URL buttons :</b>
<code>[Button Text](buttonurl:https://t.me/HMTD_Karthik)</code>

<b>Alert buttons :</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """<b>Help :</b> <b>Auto Filter</b>

<b>NOTE :</b>
<b>1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db.</b>"""
    CONNECTION_TXT = """<b>Help :</b> <b>Connections</b>

<b>- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.</b>

<b>NOTE :</b>
<b>1. Only admins can add a connection.
2. Send</b> <code>/connect</code> <b>for connecting me to ur PM</b>

<b>Commands and Usage :</b>
<b>โข /connect  - connect a particular chat to your PM
โข /disconnect  - disconnect from a chat
โข /connections - list all your connections</b>"""
    EXTRAMOD_TXT = """<b>Help :</b> <b>Extra Modules</b>

<b>NOTE :</b>
<b>these are the extra features of Auto Filter Bot (Movie Search Bot)</b>

<b>Commands and Usage :</b>
<b>โข /id - get id of a specified user.
โข /info  - get information about a user.
โข /imdb  - get the film information from IMDb source.
โข /search  - get the film information from various sources.</b>"""
    ADMIN_TXT = """<b>Help :</b> <b>Admin mods</b>

<b>NOTE :</b>
<b>This module only works for my admins</b>

<b>Commands and Usage :</b>
<b>โข /logs - to get the rescent errors
โข /stats - to get status of files in db.
โข /delete - to delete a specific file from db.
โข /users - to get list of my users and ids.
โข /chats - to get list of the my chats and ids 
โข /leave  - to leave from a chat.
โข /disable  -  do disable a chat.
โข /ban  - to ban a user.
โข /unban  - to unban a user.
โข /channel - to get list of total connected channels
โข /broadcast - to broadcast a message to all users</b>"""
    STATUS_TXT = """<b>๐๏ธ Total Files :</b> <code>{}</code> <b>Files</b>\n
<b>๐ฉ๐ปโ๐ป Total Users :</b> <code>{}</code> <b>Users</b>\n
<b>๐ฅ Total Groups :</b> <code>{}</code> <b>Groups</b>\n
<b>๐พ Used Storage :</b> <code>{}</code>\n
<b>๐ Free Storage :</b> <code>{}</code>"""
    LOG_TEXT_G = """<b>#New_Group</b>
    
<b>แโบ Group โชผ {}(<code>{}</code>)</b>
<b>แโบ Total Members โชผ <code>{}</code></b>
<b>แโบ Added By โชผ {}</b>
"""
    LOG_TEXT_P = """<b>#New_User</b>
    
<b>แโบ ID - <code>{}</code></b>
<b>แโบ Name - {}</b>
"""
M_NT_FND = """<b>This Movie Not Found my Database or Not Released This Movie \n\nRequest to Admin</b>"""

