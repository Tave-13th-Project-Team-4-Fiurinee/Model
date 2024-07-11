import uvicorn
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from .flower_recommendation_re import recommender
from .color_flower import recommender

#라우터 객체 생성
router = APIRouter() #여러 엔드포인트(API 경로)를 그룹화하고 관리하는 데 사용

class RecommendRequest(BaseModel): #꽃 추천 모델
    user_input: str
    user_month: int

class FlowerColorRequest(BaseModel): #어울리는 색상 모델
    flower_name: str
    flower_mean: str


@router.post('/recommend') #꽃 추천 모델
def get_recommendations(request: RecommendRequest):
    try:
        recommendations = recommender.recommend(request.user_input, request.user_month)
        # result = recommendations.to_dict(orient='records')
        return {"recommendations": recommendations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/flower_color') #어울리는 색상 모델
def get_flowers_color_list(request: FlowerColorRequest):
    try:
        flower_color_list = recommender.result_flower(request.flower_name, request.flower_mean)
        return {"flower_color_list": flower_color_list}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))