import json
import os
import random

def load_donation_data(json_folder):
    # JSON 파일 경로 목록 가져오기
    json_files = [os.path.join(json_folder, file) for file in os.listdir(json_folder) if file.endswith(".json")]

    # 모든 후원 이벤트 반응을 저장할 리스트
    all_reactions = []

    # 각 JSON 파일을 순회하며 후원 이벤트 반응 로드
    for json_file in json_files:
        with open(json_file, "r", encoding="utf-8") as json_data:
            data = json.load(json_data)
            reactions = data.get("donation_events", [])
            all_reactions.extend(reactions)

    return all_reactions

def get_donation_reaction(price, all_reactions):
    # 가격에 따라 필터링된 후원 이벤트 선택
    filtered_events = [event for event in all_reactions if event["donation_amount"] <= price]

    if filtered_events:
        # 무작위 후원 이벤트 선택
        random_event = random.choice(filtered_events)
        donor_name = random_event["donor_name"]

        # 후원 이벤트 반응 반환
        return random_event["reaction"].format(
            donor_name=donor_name,
            donation_amount=random_event["donation_amount"],
            donation_date=random_event["donation_date"]
        )
    else:
        return f"{price}원 이하의 후원 데이터가 없습니다."

if __name__ == "__main__":
    # JSON 폴더 경로 설정
    json_folder = "sponsor_files"

    # JSON 데이터 로드
    all_reactions = load_donation_data(json_folder)

    while True:
        # 사용자로부터 가격 입력 받기
        user_price_input = input("가격을 입력하세요 (종료하려면 'exit' 입력): ")

        if user_price_input.lower() == "exit":
            break

        # 입력된 가격을 정수로 변환 (입력이 없을 경우 기본값 0 설정)
        try:
            user_price = int(user_price_input)
        except ValueError:
            user_price = 0

        # 가격에 따른 후원 이벤트 반응 출력
        reaction = get_donation_reaction(user_price, all_reactions)
        print(reaction)