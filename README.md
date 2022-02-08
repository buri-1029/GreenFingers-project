# GreenFingers-project
> 반려식물 종합 관리 서비스 🌿 


## 프로젝트 개요
### 프로젝트 소개 [GreenFingers(그린핑거스)]
- **개발 기간** : 2021.04.12 ~ 2021.05.21
- **인원** : Backend(3), Frontend(3)
- **한 줄 소개** : 식물 분류 AI로 식물의 정보를 간편하게 등록, 방 별로 식물 관리, 식물마다 다이어리 작성, 물주기 알림, AR을 이용한 식물 배치와 같은 다양한 기능으로 식물을 체계적으로 관리할 수 있는 서비스

## 기술스택

![javascript](https://img.shields.io/badge/-Javascript-F7DF1E?logo=javascript&logoColor=white&style=flat) ![reactnative](https://img.shields.io/badge/-ReactNative-61DAFB?logo=react&logoColor=white&style=flat) ![Firebase](https://img.shields.io/badge/Firebase-FFCA28?logo=Firebase&logoColor=white&style=flat) ![android](https://img.shields.io/badge/-Android-3DDC84?logo=android&logoColor=white&style=flat) <br/>
![java](https://img.shields.io/badge/-Java-007396?logo=java&logoColor=white&style=flat) ![spring boot](https://img.shields.io/badge/-SpringBoot-6DB33F?logo=springboot&logoColor=white&style=flat) ![jpa](https://img.shields.io/badge/-JPA-gray?logoColor=white&style=flat) ![mysql](https://img.shields.io/badge/MySQL-4479A1?logo=Mysql&logoColor=white&style=flat) 
![python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat) ![flask](https://img.shields.io/badge/-Flask-000000?logo=flask&logoColor=white&style=flat) ![pytorch](https://img.shields.io/badge/-Pytorch-EE4C2C?logo=pytorch&logoColor=white&style=flat)  ![numpy](https://img.shields.io/badge/-Numpy-013243?logo=numpy&logoColor=white&style=flat) <br/>
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=flat&logo=Jenkins&logoColor=white)  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat&logo=Docker&logoColor=white&link="/> <img src="https://img.shields.io/badge/Amazon S3-569A31?style=flat&logo=Amazon%20S3&logoColor=white&link="/> <img src="https://img.shields.io/badge/Amazon AWS-232F3E?style=flat&logo=amazon%20AWS&logoColor=white&link="/>

## 아키텍처

## 주요기능 
> 한눈에 보기

![features](assets/img/features.png)


## 주요화면

![ui](assets/img/ui.png)


## 식물 분류 AI

![ai](assets/img/ai.png)

```
    1. 학습에 필요한 90가지 식물마다 500개 이미지 데이터 수집/전처리(구글, 네이버 크롤링)
    2. 가공된 학습 데이터를 사전 학습된 VGG16모델을 이용하여 학습
    3. 학습된 모델(정확도 76%) API 배포
```
