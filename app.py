# blur_speed_estimator.py
"""
Motion-Blur Speed Estimator  🚗💨
────────────────────────────────────────────────────────────────────────────
Estimate the speed of a moving object from a single motion-blur photo:
1. Upload an image with visible motion blur.
2. Draw a **calibration line** over an object of known real-world length.
3. Draw a **blur line** along the length of the motion blur streak.
4. Enter the real-world calibration length (meters) and camera shutter speed (seconds).
5. The app computes estimated speed (km/h) = (blur_length_m / exposure_s) × 3.6.

*Proof-of-concept only.* No production-grade CV or EXIF parsing.  
For enterprise computer-vision pipelines, [contact me](https://drtomharty.com/bio).
"""

import math
from PIL import Image
import numpy as np
import streamlit as st
from streamlit_drawable_canvas import st_canvas

# ────────────────────────────────────────────────────────────────────────────
st.set_page_config(page_title="Motion-Blur Speed Estimator", layout="wide")
st.title("🚗💨 Motion-Blur Speed Estimator")

st.info(
    "🔔 **Demo Notice**  \n"
    "Draw calibration & blur lines, input real length & shutter speed, and get an estimated speed.  \n"
    "For calibrated, robust vision systems, [contact me](https://drtomharty.com/bio).",
    icon="💡"
)

# ───────────────────────── Upload & display ──────────────────────────────────
uploaded = st.file_uploader("📷 Upload a motion-blur image", type=["jpg","jpeg","png"])
if not uploaded:
    st.stop()

img = Image.open(uploaded).convert("RGB")
w, h = img.size
disp_w = min(700, w)
disp_h = int(h * disp_w / w)

st.subheader("Original Image")
st.image(img, use_column_width=False, width=disp_w)

# ───────────────────────── Calibration line ─────────────────────────────────
st.subheader("1️⃣ Calibration")
st.markdown("Draw a **green line** over an object of **known length** (e.g., license plate).")
canvas_calib = st_canvas(
    fill_color="rgba(0,0,0,0)",
    stroke_width=2,
    stroke_color="#00FF00",
    background_image=img,
    drawing_mode="line",
    key="calib_canvas",
    width=disp_w,
    height=disp_h
)

# ───────────────────────── Blur line ────────────────────────────────────────
st.subheader("2️⃣ Blur Measurement")
st.markdown("Draw a **red line** along the motion-blur streak.")
canvas_blur = st_canvas(
    fill_color="rgba(0,0,0,0)",
    stroke_width=2,
    stroke_color="#FF0000",
    background_image=img,
    drawing_mode="line",
    key="blur_canvas",
    width=disp_w,
    height=disp_h
)

# ───────────────────────── Inputs & compute ─────────────────────────────────
st.subheader("3️⃣ Inputs")
calib_len_m  = st.number_input("Real-world calibration length (meters)", min_value=0.01, value=0.5, step=0.01)
shutter_s    = st.number_input("Camera shutter speed (seconds)", min_value=1e-4, value=1/60, format="%.5f")

if st.button("🚀 Estimate Speed"):
    try:
        # extract first line from each canvas
        obj_cal = canvas_calib.json_data["objects"][0]["points"]
        obj_blur= canvas_blur.json_data["objects"][0]["points"]
    except:
        st.error("Please draw both a calibration and a blur line.")
        st.stop()

    # pixel distances
    (x0,y0),(x1,y1) = obj_cal
    pix_cal = math.hypot(x1-x0, y1-y0)
    (u0,v0),(u1,v1) = obj_blur
    pix_blur= math.hypot(u1-u0, v1-v0)

    # compute
    m_per_px = calib_len_m / pix_cal
    blur_m   = pix_blur * m_per_px
    speed_m_s= blur_m / shutter_s
    speed_kmh= speed_m_s * 3.6

    st.success(f"Estimated speed: **{speed_kmh:.1f} km/h**")
    # show details
    st.markdown(f"- Calibration: {pix_cal:.1f} px ⇒ {calib_len_m:.3f} m ⇒ {m_per_px:.6f} m/px")
    st.markdown(f"- Blur length: {pix_blur:.1f} px ⇒ {blur_m:.3f} m")
    st.markdown(f"- Shutter speed: {shutter_s:.5f} s")
    st.markdown(f"- Speed: {blur_m:.3f} m / {shutter_s:.5f} s × 3.6 = **{speed_kmh:.1f} km/h**")

