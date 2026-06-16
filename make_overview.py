#!/usr/bin/env python3
"""Generate annotated feature-map images for the Ruelle app overview."""
from annotate import annotate

RAW = "/home/seongmin/development/screens/raw"
OUT = "/home/seongmin/development/screens"


def C(x1, y1, x2, y2, badge=None):
    return {"type": "circle", "box": [x1, y1, x2, y2], **({"badge": badge} if badge else {})}


# 1) FEED — exact coords from uiautomator dump
annotate(
    f"{RAW}/feed_light.png", f"{OUT}/anno_feed.png", "피드 (홈)",
    [
        {**C(820, 140, 962, 281, badge=[962, 150]), "num": 1, "label": "테마 전환 (라이트/다크/시스템)"},
        {**C(946, 140, 1080, 281, badge=[1000, 300]), "num": 2, "label": "프로필 검색"},
        {**C(24, 300, 200, 424, badge=[210, 360]), "num": 3, "label": "작성자 탭 → 캐릭터 프로필"},
        {**C(0, 430, 1080, 1510, badge=[540, 470]), "num": 4, "label": "이미지 탭 → 전체화면 뷰어 (좌우 스와이프)"},
        {**C(15, 1515, 153, 1653, badge=[90, 1480]), "num": 5, "label": "좋아요 (낙관적 업데이트)"},
        {**C(141, 1515, 279, 1653, badge=[300, 1480]), "num": 6, "label": "댓글/상세 화면 열기"},
        {**C(885, 1987, 1044, 2146, badge=[840, 2010]), "num": 7, "label": "새 포스트 작성 (이미지 압축 업로드)"},
        {**C(0, 2185, 1080, 2337, badge=[150, 2160]), "num": 8, "label": "하단 탭: 홈 · 메시지(DM) · 알림 · 프로필"},
    ],
)

# 2) LOGIN
annotate(
    f"{RAW}/login.png", f"{OUT}/anno_login.png", "로그인",
    [
        {**C(60, 860, 1020, 1010, badge=[1000, 880]), "num": 1, "label": "이메일 입력"},
        {**C(60, 1040, 1020, 1190, badge=[1000, 1060]), "num": 2, "label": "비밀번호 입력"},
        {**C(74, 1258, 1006, 1389, badge=[150, 1280]), "num": 3, "label": "이메일 로그인 (POST /auth/login)"},
        {**C(74, 1420, 1006, 1546, badge=[150, 1440]), "num": 4, "label": "비밀번호 재설정"},
        {**C(74, 1620, 1006, 1760, badge=[150, 1640]), "num": 5, "label": "Google 로그인 (SSO)"},
        {**C(74, 1788, 1006, 1918, badge=[150, 1808]), "num": 6, "label": "카카오 로그인 (SSO)"},
        {**C(560, 1935, 800, 2065, badge=[840, 1980]), "num": 7, "label": "회원가입 이동"},
        {**C(944, 150, 1072, 300, badge=[1000, 320]), "num": 8, "label": "테마 전환 (비로그인도 가능)"},
    ],
)

# 3) PROFILE VIEW (타인 프로필)
annotate(
    f"{RAW}/profile_view.png", f"{OUT}/anno_profile.png", "캐릭터 프로필",
    [
        {**C(400, 250, 680, 500, badge=[700, 300]), "num": 1, "label": "프로필 이미지 · 이름 · 상태"},
        {**C(60, 760, 1020, 1120, badge=[1000, 820]), "num": 2, "label": "소개(bio) · 상세 정보"},
        {**C(74, 1200, 1006, 1330, badge=[150, 1220]), "num": 3, "label": "메시지 보내기 → DM 채팅 열기"},
        {**C(0, 1380, 1080, 2200, badge=[540, 1420]), "num": 4, "label": "캐릭터 포스트 그리드 (3열)"},
    ],
)

# 4) POST DETAIL
annotate(
    f"{RAW}/post_detail.png", f"{OUT}/anno_post_detail.png", "포스트 상세",
    [
        {**C(24, 270, 700, 400, badge=[720, 300]), "num": 1, "label": "작성자 (탭 → 프로필)"},
        {**C(0, 430, 1080, 1430, badge=[540, 470]), "num": 2, "label": "이미지 (탭 → 전체화면 뷰어)"},
        {**C(20, 1470, 520, 1600, badge=[560, 1500]), "num": 3, "label": "좋아요 수 · 본문"},
        {**C(20, 1720, 1020, 2080, badge=[1000, 1740]), "num": 4, "label": "댓글 · 답글 (내 댓글은 삭제)"},
        {**C(20, 2240, 1020, 2360, badge=[1000, 2250]), "num": 5, "label": "댓글 입력 → 등록"},
    ],
)

print("done")
