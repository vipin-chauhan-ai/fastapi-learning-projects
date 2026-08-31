from fastapi import APIRouter, UploadFile,File,HTTPException

ALLOWED_TYPE = ["applicaiton/pdf","image/png"]
ALLOWEED_EXTENSIONS = [".pdf",".jpg",".png"]
MAX_FILE_SIZE = 5*1024*1024  # check file size

router = APIRouter()

@router.post("/upload")

def upload_file(file:UploadFile=File(...)):
    # check for file type
    if file.content_type not in ALLOWED_TYPE:
        raise HTTPException(
            status_code = 404,
            detail="only PDF,jpg,png allowed"
        )
    file_extenstion = os.path.splitext(file.filename[1].lower())
     # check for file extenstion
    if file_extenstion not in ALLOWEED_EXTENSIONS:
        raise HTTPException(
            status_code = 404,
            detail= "inavalid file type"
        ) 
    os.makedirs("uploads",exit_ok =True)
    #Get file path
    file_path = os.path.join("upload",file.filename)
    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)       
    return{
        "message" : "File Uploaded Successfully",
        "filename" : file.filename,
        "content_type":file.content_type
    }