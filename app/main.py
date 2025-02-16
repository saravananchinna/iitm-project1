from typing import Annotated
from fastapi import FastAPI, HTTPException, Query
import uvicorn

from app.services.format_service import find_no_of_wednesday, format_data, read_file



app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/run")
async def read_task(task : Annotated[str,Query()]):
        if 'format' in task:
            await format_data()
        elif 'wednesday' in task:
            task =  await find_no_of_wednesday()
        if task == 'not found':
             raise HTTPException(status_code=404, detail="Item not found")
        return task

@app.get("/read")
async def read_file_content(path : Annotated[str,Query()]):
     print("inside of read method")
     try:
          content=read_file("."+path)
          print(content)
     except FileNotFoundError:
          raise HTTPException(status_code=404)
     except:
          print("last exception")
          raise HTTPException(status_code=404)
     return content

if __name__ == '__main__':

    uvicorn.run('main:app')