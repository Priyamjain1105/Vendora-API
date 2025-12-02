from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def health_check():
		return "The Health Check is Successful!"