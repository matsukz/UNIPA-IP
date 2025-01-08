from fastapi import FastAPI, Depends,  HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

description = """
  学内LANのローカルアドレスから現在地を特定する
  """

app = FastAPI(
  title = "教室推定API - FastAPI",
  description=description
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.on_event("startup")
async def startup():
  pass

#終了時
@app.on_event("shutdown")
async def shutdown():
  pass

@app.get("/upip/api/", tags=["APIエンドポイント"], summary="テスト用")
async def get_classroom():
  
  result:dict ; result = {"status":"OK"}

  return result

@app.get("/upip/api/classroom", tags=["APIエンドポイント"], summary="接続元アドレスから教室を推定する")
async def get_classroom():
  
  result:dict ; result = {"status":"OK"}

  return result