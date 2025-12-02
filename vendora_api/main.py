from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def health_check():
		return {
			"Message":"Welcome To Vendora API Connect",
            "Health Status":"OK"
		}