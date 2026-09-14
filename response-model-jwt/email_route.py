from fastapi import APIRouter,BackgroundTasks
from email_schema import EmailSchema
from fastapi_mail import ConnectionConfig,FastMail,MessageSchema,MessageType
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
    MAIL_SSL_TLS= os.getenv("MAIL_SSL_TLS")=='True',
    USE_CREDENTIALS = True
)

router = APIRouter()

#mail service code 
async def send_email_service(email:str,subject:str,body:str):
      message = MessageSchema(
            subject = subject,
            recipients = [email],
            body = body,
            subtype = MessageType.plain)
      fm =FastMail(conf)
      await fm.send_message(message)

#NOrmal send email function 
@router.post("/send-email")
async def send_email(email:EmailSchema,background_tasks: BackgroundTasks):
        background_tasks.add_task(send_email_service,email.email,
                                  "Fast API MAIL",
                                  """ 
                                              Hello User,
                                              
                                              
                                              This email from Fast API Function, Have a Nice day
                                              
                                              Thank You!
                                          """,
                                  
                                  )
      
        return {"Message" : "Email Send Successfully!"}
