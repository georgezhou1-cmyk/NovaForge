import streamlit as st
import matplotlib.pyplot as plt
from design import optimize_design
from engine import Engine
from orbit import simulate_orbit

st.write("🚀 系统启动中...")

st.title("🚀 AI航天器设计系统")

task = st.text_input("输入飞行任务：")
if not task:
    st.stop()

if st.button("开始设计"):

    st.write("🔁 AI正在设计飞行器...")

    best_design, best_score = optimize_design(task)

    st.subheader("🏆 最优设计")
    st.json(best_design)

    st.write("📊 评分：", best_score)

    # 发动机
    engine = Engine(best_design["propulsion_system"])
    st.subheader("🚀 发动机参数")
    st.json(engine.info())

    # 轨道
    st.subheader("🛰 轨道模拟")

    traj = simulate_orbit()

    x = [p[0] for p in traj]
    y = [p[1] for p in traj]

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("Orbit Trajectory")

    st.pyplot(fig)