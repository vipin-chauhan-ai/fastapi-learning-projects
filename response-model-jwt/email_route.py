from fastapi import APIRouter
from email_schema import EmailSchema
from fastapi_mail import ConnectionConfig, FastMail,MessageSchema,MessageType
from dotenv import load_dotenv
import os
load_dotenv()
conf = ConnectionConfig(
        MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
        MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
        MAIL_FROM=os.getenv("MAIL_FROM"),
        MAIL_PORT=os.getenv("MAIL_PORT"),
        MAIL_SERVER=os.getenv("MAIL_SERVER"),
        MAIL_STARTTLS=os.getenv("MAIL_STARTTLS")=='True',
        MAIL_SSL_TLS=os.getenv("MAIL_SSL_TLS")=='True',
        USE_CREDENTIALS = True
    )
router = APIRouter()
@router.post("/send-email")
async def send_email(email:EmailSchema):
    message = MessageSchema(
        subject = "Fast Api Email",
        recipients = [email.email],
        body = """ 
            Hello User,
            
            
            This email from Fast API Function, Have a Nice day
            
            Thank You!
        """,
        subtype = MessageType.plain)
    fm =FastMail(conf)
    await fm.send_message(message)
    return {"Message" : "Email Send Successfully!"}