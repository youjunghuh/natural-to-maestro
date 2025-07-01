import openai
import os

def generate_maestro_yaml(user_input: str) -> str:
    prompt = f"""
다음은 모바일 앱 E2E 테스트를 위한 자연어 시나리오입니다.
해당 시나리오를 Maestro 프레임워크에서 사용하는 YAML 명령어로 변환해주세요.

[시나리오]
{user_input}

[Maestro YAML 결과]
- launchApp
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    return response['choices'][0]['message']['content']