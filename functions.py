import qrcode 

from qrcode import QRCode

from PIL import Image
from telegram.ext import ContextTypes

from telegram import Update
# Qccode style 
qr = QRCode(version=1, box_size=10, border=10,error_correction=qrcode.constants.ERROR_CORRECT_H)



#define data variables to get data from user

#logo of user
picture_name = ""

#data of user
user_data = ""

#qrCode
QRCode = ""



#when user type /start
async def start(update:Update,context: ContextTypes.DEFAULT_TYPE):
    commands = '''
    /start : start bot\n/data your_data : write your data\n/nopicture : if you want to delete any picture you have upload it before\n/generate : generate your QRcode
    '''
    await  update.message.reply_text('Hello! Welcome to Qr-Code-Generator bot 🤖.')
    await  update.message.reply_text(commands)


#get picture from user (upload picture)
async def reply(update:Update, context: ContextTypes.DEFAULT_TYPE):
    global picture_name
    
    if not update.message.photo:
        
        await update.message.reply_text("No picture received")
        
    picture =  update.message.photo[-1]
    picture_id = picture.file_id
    
    file = await context.bot.get_file(picture_id)

    picture_name = f"{picture_id}.jpg"
    
    try:
        await file.download_to_drive(picture_name)
    except Exception as e:
        print("error",e)

#user type /data and write his data
async def data(update:Update, context: ContextTypes.DEFAULT_TYPE):     
    global user_data
    user_data = update.message.text

#generate QRcode
async def generate(update:Update, context: ContextTypes.DEFAULT_TYPE):
    global QRCode   
    # add data to qr code 
    qr.add_data(user_data)
    # Make the QR code
    qr.make(fit=True)
    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    # get user image if there is one
    if not picture_name:
         logo = Image.open("qrcode.jpg")
         # Resize the logo or image if needed
         logo = logo.resize((50, 50))
         img_w, img_h = img.size
         logo_w, logo_h = logo.size
         pos = ((img_w - logo_w) // 2, (img_h - logo_h) // 2)
         img.paste(logo, pos)
         img.save("qr_code.png")
         QRCode = "qr_code.png"
         await update.message.reply_photo(photo=open(QRCode, "rb"))
    else:
    #if user upload image get it     
        logo = Image.open(picture_name)
    # Resize the logo or image if needed
        logo = logo.resize((50, 50))
        img_w, img_h = img.size
        logo_w, logo_h = logo.size
        pos = ((img_w - logo_w) // 2, (img_h - logo_h) // 2)
        img.paste(logo, pos)
        img.save("qr_code.png")
        QRCode = "qr_code.png"
        with open(QRCode, "rb") as picture:
            await update.message.reply_photo(photo=picture)

#delete old picture if user want to generate another QR code without specifique logo
async def nopicture(update:Update, context: ContextTypes.DEFAULT_TYPE):
    global picture_name
    picture_name = ""
   