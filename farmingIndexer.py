from urllib import response
from fastapi import FastAPI, Request
import requests

app = FastAPI()

#get all farming pools filtered by request body params
@app.post("/farming_pools")
async def get_body(request: Request):
    json1 = await request.json()
    response = request.post("https://farming-pool-indexer-test.broxus.com/v1/farming_pools", json=json1)
    return response.json()

#get specific farming pool based on the pool's address
@app.post("/farming_pools/{farming_pool_address}")
async def get_body(request:Request, farming_pool_address: str):
    json1 = await request.json()
    response = requests.post("https://farming-pool-indexer-test.broxus.com/v1/farming_pools/" + farming_pool_address, json=json1)
    return response.json()

#get total value locked data based on timespan and timeframe
@app.post("/graphic/tvl")
async def get_body(request: Request):
    json1 = await request.json()
    response = request.post("https://farming-pool-indexer-test.broxus.com/v1/graphic/tvl", json=json1)
    return response.json()

#get annual percentage rate data based on timespan and timeframe
@app.post("/graphic/apr")
async def get_body(request: Request):
    json1 = await request.json()
    response = request.post("https://farming-pool-indexer-test.broxus.com/v1/graphic/apr", json=json1)
    return response.json()

#get all transactions filtered by request body params
@app.post("/transactions")
async def get_body(request: Request):
    json1 = await request.json()
    response = request.post("https://farming-pool-indexer-test.broxus.com/v1/transactions", json=json1)
    return response.json()