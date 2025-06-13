from datetime import date

from fastapi import FastAPI
import uvicorn




app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}

# [project.scripts]脚本执行入口
def main() -> None:
    print("Hello from uv-dependencie-demo!")
    print(date.today())
    uvicorn.run(app)

if __name__ == "__main__":
    main()

