# NAS 서버 및 웹페이지 프로젝트

[![EN](https://img.shields.io/badge/lang-en-blue.svg)](README.en.md) 
[![KR](https://img.shields.io/badge/lang-kr-red.svg)](README.md)

이 프로젝트는 Django를 사용하여 구축된 개인 NAS(Network Attached Storage) 서버 및 웹페이지입니다. 파일 저장, 관리 및 접근에 대한 안전하고 효율적인 솔루션을 제공합니다. 이 서버는 쉽게 배포할 수 있도록 설계되었으며, Docker를 사용하여 컨테이너화하여 배포 및 확장성을 간소화할 계획입니다.

## 프로젝트 목표

- **안전한 파일 저장**: 모든 파일이 적절한 인증 및 접근 제어를 통해 안전하게 저장되도록 보장합니다.
- **사용자 인증**: 인증된 사용자만 접근할 수 있도록 강력한 사용자 인증을 구현합니다.
- **확장성**: Docker를 사용하여 애플리케이션을 컨테이너화하고, 배포 및 확장성을 용이하게 합니다.
- **웹 인터페이스**: 파일 관리 및 접근을 위한 깨끗하고 사용자 친화적인 웹 인터페이스를 제공합니다.
- **확장 가능성**: 향후 기능 확장 및 통합을 위해 모듈화된 확장 가능한 아키텍처를 구축합니다.

## 사용된 기술

- **프레임워크**: Django (v3.2.25) - 빠른 개발과 깨끗하고 실용적인 설계를 장려하는 고수준 Python 웹 프레임워크입니다.
- **데이터베이스**: SQLite (기본 내장), MySQL 또는 PostgreSQL을 프로덕션 환경에 사용할 수 있습니다.
- **프론트엔드**: 기본 HTML/CSS 템플릿 (향후 개선 예정).
- **환경 관리**: `virtualenv` 또는 `conda`를 사용한 종속성 및 환경 관리.
- **컨테이너화**: Docker - 컨테이너화를 통해 배포 및 확장성을 지원합니다.
- **보안**: SSL/TLS 지원 및 암호화를 위해 Python의 `cryptography` 및 `pyOpenSSL` 라이브러리 사용.
- **환경 변수**: `python-dotenv`를 사용하여 환경 변수를 안전하게 관리합니다.
- **확장 기능**: 추가 개발 도구를 위한 Django Extensions.

## 설치 및 설정

### 필수 조건

- Python 3.7+
- 패키지 관리용 pip 또는 conda
- Docker (컨테이너화를 위한 선택사항)

### 설치

1. **리포지토리 클론:**

    ```bash
    git clone https://github.com/dongkoony/NAS-Server.git
    cd NAS-Server
    ```

2. **환경 설정:**

    `virtualenv` 사용 시:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    또는 `conda` 사용 시:

    ```bash
    conda create -n nas python=3.7
    conda activate nas
    ```

3. **필수 패키지 설치:**

    ```bash
    pip install -r requirements.txt
    ```

4. **환경 변수 설정:**

    프로젝트 루트 디렉토리에 `.env` 파일을 생성하고 다음 변수를 추가합니다:

    ```plaintext
    DJANGO_SECRET_KEY=<Your_Secret_Key>
    DJANGO_ALLOWED_HOSTS=<Your_IP>
    DJANGO_DEBUG=True <True / False>
    ```

5. **애플리케이션 실행:**

    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

    `http://127.0.0.1:8000`에서 애플리케이션에 접근할 수 있습니다.

### Docker Container (예정)

이 프로젝트는 Docker를 사용하여 컨테이너화될 예정입니다. 이를 통해 배포 및 확장성을 간소화할 수 있습니다. 다음 단계가 추가될 예정입니다:

- **Dockerfile**: Docker 이미지를 정의하기 위한 Dockerfile 생성.
- **Docker Compose**: 필요 시, 다중 컨테이너 애플리케이션 관리를 위한 Docker Compose 사용.
- **CI/CD 파이프라인**: GitHub Actions or Jenkins와 같은 도구를 사용하여 테스트 및 배포 자동화를 위한 CI/CD 파이프라인 구현.

## 버전 관리

이 프로젝트는 [Semantic Versioning](https://semver.org/)을 사용하여 버전 관리를 진행합니다.

## 기여

기여는 언제든지 환영합니다! 리포지토리를 포크하고, Pull Request를 제출해 주세요.

1. 리포지토리 포크.
2. 기능 브랜치 생성 (`git checkout -b feature-branch`).
3. 변경사항 커밋 (`git commit -m '새 기능 추가'`).
4. 브랜치에 푸시 (`git push origin feature-branch`).
5. Pull Request 생성.

## 라이센스

이 프로젝트는 MIT 라이센스에 따라 라이센스가 부여됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하십시오.

## 연락처

문의 사항이 있으면 [shin.dh922@gmail.com](mailto:shin.dh922@gmail.com)으로 연락해 주세요.
