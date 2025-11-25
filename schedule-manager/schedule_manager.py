import pymysql

from pymysql.cursors import Cursor

def show_menu() -> str:
    print("1. 일정 추가")  # insert
    print("2. 일정 보기")  # select
    print("3. 일정 완료")  # update
    print("4. 종료")
    return get_user_choice()

def get_user_choice() -> str:
    return input("선택: ")

def get_db_connection() -> pymysql.Connection:
    try:
        return pymysql.connect(host="localhost", port=3307, user="root", password='1234', database='schedule_db')
    except Exception as e:
        print(f"데이터베이스 연결 실패: {e}")
        exit(1)

def add_schedule(cursor: Cursor):
    print("-------- 일정 추가 ---------")

    # 정보 입력
    title = input("타이틀: ")
    description = input("내용: ")
    start_datetime = input("시작 시간: ")
    end_datetime = input("종료 시간: ")

    # insert 쿼리 생성
    sql = """
          INSERT INTO schedules (title, description, start_datetime, end_datetime)
          VALUES (%s, %s, %s, %s)
    """

    # 쿼리 실행
    cursor.execute(sql, (title, description, start_datetime, end_datetime))

    print("-------- 일정 추가 완료 ---------")

def get_schedules(cursor: Cursor):
    print("-------- 일정 보기 ----------")

    sql = """
        SELECT * FROM schedules
    """
    cursor.execute(sql)
    schedules = cursor.fetchall()

    columns = [desc[0] for desc in cursor.description]

    for schedule in schedules:
        for column, value in zip(columns, schedule):
            if column == 'created_at':
                pass
            else:
                print(f"{column}: {value}")
        print("-" * 20)

def complete_schedule(cursor: Cursor):
    print("-------- 일정 완료 시키기 ----------")

    id = int(input("일정 아이디를 입력해 주세요: "))

    sql = """
          UPDATE schedules
          SET is_completed = true WHERE id = %s
      """

    cursor.execute(sql, id)
    print(f"-------- {id} 일정 완료 ----------")

def main():
    conn = get_db_connection()  # db 연결
    cursor = conn.cursor()

    try:
        while True: # 메뉴 루프
            choice = show_menu()    # 메뉴 출력 및 사용자 선택 입력 받기
            if choice == "1":   # 기능 실행
                add_schedule(cursor)
                conn.commit()
            elif choice == "2":
                get_schedules(cursor)
            elif choice == "3":
                complete_schedule(cursor)
                conn.commit()
            elif choice == "4":
                print("종료합니다.")
                break
            else:
                print("다시 선택해주세요")

    except Exception as e:
        print(f"프로그램 실행 중 오류 발생: {e}")

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    main()