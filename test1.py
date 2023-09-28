import json
import random
import os

# JSON 파일을 저장한 폴더 경로 설정
json_folder = "json_files"

# JSON 파일 경로 목록을 가져오기
json_files = [os.path.join(json_folder, file) for file in os.listdir(json_folder) if file.endswith(".json")]

# 모든 JSON 파일의 반응을 저장할 리스트
all_reactions = []

# 각 JSON 파일을 순회하며 데이터 로드
for json_file in json_files:
    with open(json_file, "r", encoding="utf-8") as file:
        data = json.load(file)
        reactions = data.get('reactions', [])
        all_reactions.extend(reactions)

# 사용자 입력에 대한 랜덤 응답 챗봇 함수
def random_response(user_input):
    # 사용자 입력과 일치하는 채팅 메시지 반응 찾기
    matching_reactions = []
    for reaction in all_reactions:
        if reaction['message'].lower() in user_input.lower():
            matching_reactions.append(reaction['response'])

    # 랜덤 응답 선택
    if matching_reactions:
        selected_response = random.choice(matching_reactions)
        return selected_response
    else:
        return "챗봇: 이 채팅 메시지에 대한 반응을 찾을 수 없습니다."

# 대화 시작
print("챗봇: 안녕하세요! 테스트 시작합니다. 종료하려면 '종료'를 입력하세요.")

while True:
    user_input = input("사용자: ")

    if user_input == "종료":
        print("챗봇: 테스트 종료합니다.")
        break

    response = random_response(user_input)
    print("챗봇:", response)