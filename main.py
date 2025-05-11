from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from src.services.SearchCompany import get_company_info
from src.services.descriptionAnalysis import predict_startup_success
from src.config.settings import settings

app = FastAPI(
    title="Company KYC API",
    description="API for retrieving company information based on company name and location.",
    version="1.0.0"
)

@app.get("/api/company-info/{companyName}/{location}", summary="Retrieve company information based on company name and location")
async def get_company_info_endpoint(companyName: str, location: str):
    try:
        # 呼叫服務層
        result = get_company_info(companyName, location)
        return JSONResponse(content=result, status_code=200)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")
    

@app.get("/api/company-info/{companyDescription}", summary="Using starup description to identify risk")
async def company_risk_analysis(companyDescription: str):
    try:
        # 呼叫服務層
        result = predict_startup_success(companyDescription)
        return JSONResponse(content=result, status_code=200)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")

# 若非使用 uvicorn cli，才需保留以下區塊
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=settings.flask_env == "development")
