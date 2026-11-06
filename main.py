import sys
import datetime

def main():
    print("=" * 50)
    print("🎉 GitHub에서 성공적으로 실행된 파이썬 애플리케이션입니다!")
    print(f"📌 Python 버전: {sys.version}")
    print(f"⏰ 실행 시각: {datetime.datetime.now(datetime.timezone.utc)}")
    print("=" * 50)

if __name__ == "__main__":
    main()
