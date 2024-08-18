# NAS 웹 서버

이 프로젝트는 Python 3.7과 Django를 사용하여 웹 기반 네트워크 연결 저장소(NAS) 서버를 구축합니다.

## 주요 기능

- 웹 인터페이스를 통한 NAS 보안 접근
- 사용자 인증 시스템
- HTTPS 지원으로 암호화된 연결
- 파일 업로드 및 다운로드 기능
- 파일 및 폴더 관리

## 필요 조건

- Python 3.7
- Django
- Conda (가상 환경 관리용)
- Ubuntu (로컬 개발 환경)

## 설치 방법

1. 저장소 복제:
```
git clone https://github.com/dongkoony/nas-server.git
cd nas-project
```

2. Conda 가상 환경 생성 및 활성화:
```
conda create -n nas_env python=3.7
conda activate nas_env
```

3. 필요한 패키지 설치:
```
conda install django
```

4. 데이터베이스 마이그레이션 적용:
```
python manage.py migrate
```

5. 관리자 계정 생성:
```
python manage.py createsuperuser
```

## 배포

프로젝트 진행에 따라 실제 운영 환경 배포 지침을 추가할 예정입니다.

## 보안

이 프로젝트는 NAS 서버에 대한 안전한 접근을 위해 사용자 인증과 HTTPS를 구현합니다. 인증된 사용자만 NAS 리소스에 접근할 수 있습니다.

## 기여

이는 개인 프로젝트이지만, 제안과 개선사항은 환영합니다. 변경 제안을 논의하려면 이슈를 열어주세요.

## 라이선스

[MIT 라이선스](LICENSE)