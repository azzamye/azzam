#By Omar ( @dev3mora )
#For More Bots ( @ToolsEgy )
from pyrogram import Client, filters 

#Data 
i = input("Type Api Id : ")
h = input("Type Api Hash : ")
t = input("Enter Token Bot : ")

#Start Message 
StartMsg = "اهلا بك .. انا بوت عمر ، يرجي الاشتراك في القناه لكي يصلك كل جديد "
Bot = Client('Telegram - @OmarrTech', 
		api_id = i, 
		api_hash = str(h), 
		bot_token = str(t) )

#First Command ..
@Bot.on_message(filters.command("start") & filters.private)
def OmarrTech(b, m):
	b.send_message(m.chat.id, StartMsg)



print("Done .. ( @OmarrTech )")
Bot.run()