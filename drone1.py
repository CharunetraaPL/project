

import streamlit as st
import time
import plotly.graph_objects as go
from telemetry_simulator import generate_telemetry

st.set_page_config(layout="wide", page_title="Drone Telemetry")

st.title("🚁 Real-time Drone Telemetry Dashboard")
placeholder = st.empty()

battery_history = []
altitude_history = []
time_stamps = []

while True:
    telemetry = generate_telemetry()

    # Update history for plotting
    battery_history.append(telemetry['battery_voltage'])
    altitude_history.append(telemetry['imu']['altitude'])
    time_stamps.append(time.strftime('%H:%M:%S'))

    if len(battery_history) > 20:
        battery_history.pop(0)
        altitude_history.pop(0)
        time_stamps.pop(0)

    with placeholder.container():
        st.subheader("🔋 Battery & Connection Status")
        col1, col2 = st.columns(2)
        col1.metric("Battery Voltage", f"{telemetry['battery_voltage']} V")
        col2.metric("Connection Health", telemetry['connection_health'])

        st.subheader("📐 IMU Sensor Data")
        col3, col4, col5 = st.columns(3)
        col3.metric("Roll (°)", telemetry['imu']['roll'])
        col4.metric("Pitch (°)", telemetry['imu']['pitch'])
        col5.metric("Yaw (°)", telemetry['imu']['yaw'])

        st.subheader("🌡️ Environmental Data")
        col6, col7 = st.columns(2)
        col6.metric("Temperature (°C)", telemetry['imu']['temperature'])
        col7.metric("Altitude (m)", telemetry['imu']['altitude'])

        st.subheader("📊 Live Charts")
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=time_stamps, y=battery_history, mode='lines+markers', name='Battery Voltage (V)'))
        fig.add_trace(go.Scatter(x=time_stamps, y=altitude_history, mode='lines+markers', name='Altitude (m)'))
        fig.update_layout(height=400, xaxis_title="Time", yaxis_title="Values", title="Battery and Altitude Over Time")
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("🛰️ GPS Location")
        st.map(data={"lat": [telemetry['gps']['latitude']], "lon": [telemetry['gps']['longitude']]})
        st.write(f"🌍 Latitude: {telemetry['gps']['latitude']} | Longitude: {telemetry['gps']['longitude']} | Altitude: {telemetry['gps']['altitude']} m")

    time.sleep(1)