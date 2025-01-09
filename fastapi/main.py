from fastapi import FastAPI, Depends,  HTTPException, Header, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from Extend.searchip import ip_to_classroom

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
async def get_testser():
  
  result:dict ; result = {"status":"OK"}

  return result

@app.get("/upip/api/classroom", tags=["APIエンドポイント"], summary="接続元アドレスから教室を推定する")
async def get_classroom(request: Request,
    x_forwarded_for: str = Header(None, alias="X-Forwarded-For"),
    x_real_ip: str = Header(None, alias="X-Real-IP")
):
    #GetIP
    client_ip = x_real_ip or (x_forwarded_for.split(",")[0] if x_forwarded_for else request.client.host)

    result = ip_to_classroom(client_ip=client_ip, subnet=24)

    return {"client_ip":client_ip,"classroom":result["classroom"],"message":result["message"]}