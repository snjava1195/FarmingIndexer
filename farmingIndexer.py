from urllib import response
from fastapi import FastAPI, Request
import requests

app = FastAPI()

@app.post("/farming_pools")
async def get_body(request: Request):
    json1 = await request.json()
    response = request.post("https://farming-pool-indexer-test.broxus.com/v1/farming_pools", json=json1)
    return response.json()

@app.post("/farming_pools/{farming_pool_address}")
async def get_body(request:Request, farming_pool_address: str):
    json1 = await request.json()
    response = requests.post("https://farming-pool-indexer-test.broxus.com/v1/farming_pools/" + farming_pool_address, json=json1)
    return response.json()

@app.post("/graphic/tvl")
async def get_body(request: Request):
    json1 = await request.json()
    response = request.post("https://farming-pool-indexer-test.broxus.com/v1/graphic/tvl", json=json1)
    return response.json()

@app.post("/graphic/apr")
async def get_body(request: Request):
    json1 = await request.json()
    response = request.post("https://farming-pool-indexer-test.broxus.com/v1/graphic/apr", json=json1)
    return response.json()

@app.post("/transactions")
async def get_body(request: Request):
    json1 = await request.json()
    response = request.post("https://farming-pool-indexer-test.broxus.com/v1/transactions", json=json1)
    return response.json()