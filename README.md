# blur-speed-estimator

# 🚗💨 Motion-Blur Speed Estimator

A **Streamlit** proof-of-concept that estimates the speed of a moving object (e.g., a car) from a single motion-blur photograph using user-drawn calibration and blur measurements.

> **Demo only**—no camera calibration profiles, no automated blur detection, and no production guarantees.  
> For enterprise-grade vision systems and accurate speed enforcement, [contact me](https://drtomharty.com/bio).

---

## 🔍 What it does

1. **Upload** a photograph with visible motion blur (`.jpg`, `.png`).  
2. **Draw** a **green line** over an object of known physical length (e.g., license plate, curb segment).  
3. **Draw** a **red line** along the motion-blur streak corresponding to the object’s path.  
4. **Enter** the real-world calibration length (in meters) and the camera shutter speed (in seconds).  
5. **Compute** the estimated speed in km/h:

   $$
   \text{meters\_per\_pixel} = \frac{\text{calibration\_length\_m}}{\text{calibration\_pixels}} \\
   \text{blur\_meters} = \text{blur\_pixels} \times \text{meters\_per\_pixel} \\
   \text{speed\_m/s} = \frac{\text{blur\_meters}}{\text{shutter\_seconds}} \\
   \text{speed\_km/h} = \text{speed\_m/s} \times 3.6
   $$

6. **Display** the annotated image and detailed calculation breakdown.  
7. **Share** or **download** the results for reporting.

---

## ✨ Key Features

- **Interactive drawing**: precise calibration and blur measurement with a draggable canvas.  
- **Customizable inputs**: define any calibration length and shutter speed.  
- **Instant feedback**: immediate speed estimation and calculation details.  
- **Single-file app** (`blur_speed_estimator.py`): no backend needed.  
- **Zero dependencies** on external services—runs 100% client-side in Streamlit.

---

## 🚀 Quick Start (Local)

```bash
git clone https://github.com/THartyMBA/blur-speed-estimator.git
cd blur-speed-estimator
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run blur_speed_estimator.py
```

1. Open **http://localhost:8501** in your browser.  
2. Upload your motion-blur photograph.  
3. Draw the calibration (green) and blur (red) lines.  
4. Enter the real-world length and shutter speed.  
5. Click **Estimate Speed** to see your result.

---

## ☁️ Deploy on Streamlit Community Cloud

1. Push this repo (public or private) under **THartyMBA** to GitHub.  
2. Visit [streamlit.io/cloud](https://streamlit.io/cloud) → **New app** → select your repo & branch → **Deploy**.  
3. Share your live URL—no additional configuration needed.

---

## 🛠️ Requirements

```text
streamlit>=1.32
streamlit-drawable-canvas
Pillow
numpy
```

*(All CPU-compatible; runs on the free tier.)*

---

## 🗂️ Repo Structure

```
blur-speed-estimator/
├─ blur_speed_estimator.py   ← single-file Streamlit app  
├─ requirements.txt         
└─ README.md                ← this file
```

---

## 📜 License

**CC0 1.0** – public-domain dedication. Attribution appreciated but not required.

---

### 🙏 Acknowledgements

- [Streamlit](https://streamlit.io) – rapid Python UIs  
- [streamlit-drawable-canvas](https://github.com/andfanilo/streamlit-drawable-canvas) – interactive drawing canvas  
- [Pillow](https://python-pillow.org) & [NumPy](https://numpy.org) – image handling  

Draw, measure, and calculate—speed estimation made visual! 🚀

