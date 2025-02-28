from fastapi import FastAPI, Request

import platform

app = FastAPI()

@app.get("/os")
def get_os():
    os = platform.system()
    return {"os": os}

@app.get("/version")
def get_version():
    version = platform.version()
    return {"version": version}

@app.get("/ip")
def get_ip(request: Request):
    ip = request.client.host
    return {"ip": ip}

@app.get("/os/version/ip")
def get_all(request: Request):
    os = platform.system()
    version = platform.version()
    ip = request.client.host
    return {"os": os, "version": version, "ip": ip}