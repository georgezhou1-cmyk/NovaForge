import os
from dotenv import load_dotenv
from openai import OpenAI

# 读取 .env 文件
load_dotenv()

# 初始化客户端
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 用户输入任务
task = input("输入飞行器任务：")

# 调用 AI
response = client.responses.create(
    model="gpt-5",
    input=f"""
You are an aerospace engineering system.

Design a spacecraft based on the mission.

Mission:
{task}

Return ONLY valid JSON with:
- vehicle_type
- propulsion_system
- crew_capacity
- fuel_type
- heat_protection
- reusability
"""
)

#物理因素影响
def physics_score(design):
    score = 100

    # 1. 推进系统合理性
    if design["propulsion_system"] == "ion":
        score -= 10  # 适合深空，但推力弱

    if design["propulsion_system"] == "chemical":
        score -= 0  # baseline

    # 2. 载人飞行器必须有热防护
    if design["crew_capacity"] > 0 and not design.get("heat_protection"):
        score -= 30

    # 3. 火星任务必须高Δv能力
    if design.get("mission_type") == "mars" and design.get("delta_v_estimate", 0) < 8000:
        score -= 40

    return max(score, 0)

# 输出结果
print("\n=== AI 设计结果 ===\n")
print(response.output_text)