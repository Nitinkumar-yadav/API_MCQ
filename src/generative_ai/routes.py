from .services.generating_mcq import generating_mcq
from .services.extract_pdf import extract_pdf
import requests
from .schema import Doc
from fastapi.routing import APIRouter
from utils.logger import logManager

logger = logManager()

router =APIRouter()

logger.info("Creating Sever")
@router.get('/generating_mcq')
def start():
     logger.info("Server in Running>>>")
     return "Welcome Team!"


@router.post('/generating_mcq')
async def generate_mcq_api(request:Doc):
        
        logger.info("server waiting for request")
        res= request.pdf_url
        
        file = requests.get(res)
        
        if file.status_code == 200:
          filename = res.split("/")[-1]
          with open(filename, 'wb') as f:
               f.write(file.content)
               logger.info("Pdf successfully download...")
        else:
          logger.error("Pdf url not get")
     
     #    filename ="iesc108-min.pdf"
        chunks =extract_pdf(filename)
        # return chunks
        mcq =generating_mcq(chunks)

        logger.info("successfully get response from post request")
        return mcq
