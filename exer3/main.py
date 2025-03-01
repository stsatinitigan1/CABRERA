from fastapi import FastAPI, Request

import platform

app = FastAPI()

@app.get("/os") # Get OS
def get_os():
    os = platform.system()
    return {"os": os}

@app.get("/version") # Get OS version
def get_version():
    version = platform.version()
    return {"version": version}

@app.get("/ip") # Get IP of requestor
def get_ip(request: Request):
    ip = request.client.host
    return {"ip": ip}

@app.get("/os/version/ip") # Get all three (OS, OS version, IP)
def get_all(request: Request):
    os = platform.system()
    version = platform.version()
    ip = request.client.host
    return {"os": os, "version": version, "ip": ip}

# To run the program:
# To get OS, add "/os" to the URL
# To get OS version, add "/version" to the URL
# To get IP of requestor, add "/ip" to the URL
# To get all three, add "/os/version/ip" to the URL
