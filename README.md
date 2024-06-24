# Model

### 1️⃣ 탄생화, 꽃말 등을 통해서 가장 어울리는 꽃을 제공해주는 추천 시스템 구현 (3개의 꽃 추천)
- 데이터 구축: 최종 824개의 데이터 사용 </br>
</tab> - "농촌진흥청 국립원예특작과학원 오늘의 꽃"(open API), "순천만국가정원 탄생화"(pdf), “어니스트 플라워”의 꽃도감(웹크롤링) 데이터 사용 </br>
</tab> - 꽃 이름, 월, 계절, 꽃말, 설명(기념일 등 따로 추가) , 이미지(링크), 색상 칼럼 사용 </br>
</tab> - 상황(기념일) 검색해서 설명 칼럼에 추가 </br>
</tab> - 나무 데이터 삭제, 이미지 링크 변경 </br>
</tab> - 월을 통해 계절 추출 </br>
</tab> - **사용자 입력에 월이 나오지 않는 경우, 사용자 로그를 통해 월 추출(ing)** </br>

- 색상 추출 </br>
</tab> - PIL, 군집화를 통해 이미지에서 4개의 중심 색상 추출하여 가장 적합한 1개의 색상 선정 </br>
</tab> - HSV코드를 이용한 8개의 색상 군집화를 통해 색상 칼럼 생성

- 모델링(bert) </br>
</tab> 1. 전처리 </br>
</tab> 2. 토큰화, 벡터화(bert) </br>
</tab> 3. 사용자 입력 및 유사도 계산 </br>
</tab> 4. **파인튜닝**
- **서버에 업로드(ing)**

### 2️⃣ 생성형 모델을 통해 해당 꽃과 어울리는 멘트 생성(추천)
구현이 어려울 시, 지피티나 라마 등의 API를 가져와서 구현


### 3️⃣ 선정된 꽃과 어울리는 다른 꽃들도 추천 -> 꽃다발 제작
<U> </U>
색상 고려 (cv)
