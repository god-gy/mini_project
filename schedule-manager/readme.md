# Schedule Manager

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 소개

**Schedule Manager**는 일상적인 일정 관리를 돕기 위한 간단한 미니 프로젝트입니다. 사용자가 일정을 쉽게 추가, 조회, 수정, 삭제할 수 있도록 설계되었습니다. 콘솔 기반의 Python 애플리케이션으로, 데이터는 JSON 파일로 영속화되어 있습니다.

이 프로젝트는 초보 개발자를 위한 학습 목적으로 제작되었으며, 기본적인 CRUD(Create, Read, Update, Delete) 기능을 구현합니다.

## 기능

- **일정 추가**: 제목, 날짜, 설명을 입력하여 새로운 일정을 등록합니다.
- **일정 조회**: 모든 일정 목록을 출력하거나 특정 날짜의 일정을 필터링합니다.
- **일정 수정**: 기존 일정의 내용을 업데이트합니다.
- **일정 삭제**: 지정된 일정을 제거합니다.
- **데이터 저장**: 프로그램 종료 시 JSON 파일로 자동 저장됩니다.

## 요구 사항

- Python 3.8 이상
- `json` 모듈 (Python 내장)

## 설치 및 실행

1. **저장소 클론**:
   ```
   git clone https://github.com/god-gy/mini_project.git
   cd mini_project/schedule-manager
   ```

2. **실행**:
   ```
   python main.py
   ```

프로그램이 시작되면 메뉴가 표시되며, 숫자를 입력하여 기능을 선택할 수 있습니다.

## 사용 예시

```
=== Schedule Manager ===
1. 일정 추가
2. 일정 조회
3. 일정 수정
4. 일정 삭제
5. 종료

선택: 1
제목: 회의
날짜: 2025-11-26
설명: 팀 미팅
일정이 추가되었습니다!
```

## 프로젝트 구조

```
schedule-manager/
├── main.py          # 메인 실행 파일 (메뉴 및 로직)
├── schedule.json    # 일정 데이터 저장 파일
└── README.md        # 이 파일
```

## 기여

기여를 환영합니다! 버그 리포트나 기능 제안을 위해 [Issues](https://github.com/god-gy/mini_project/issues) 탭을 사용하세요. 풀 리퀘스트는 `main` 브랜치로 보내주세요.

## 라이선스

이 프로젝트는 [MIT License](LICENSE)로 배포됩니다. 자유롭게 사용하고 수정하세요.

## 연락처

- GitHub: [@god-gy](https://github.com/god-gy)
- Email: god-gy0321@gmail.com

---

⭐ 이 프로젝트가 도움이 되셨다면 스타를 눌러주세요!
