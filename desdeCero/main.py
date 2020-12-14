from fastapi import FastAPI

server = FastAPI()

@server.get("/rooms")
async def getRooms():
    return 66
