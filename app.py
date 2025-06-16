
---

### 🧠 `app.py`
```python
import streamlit as st
from PIL import Image
from rag_engine import fetch_repair_suggestions
from repair_agent import chat_with_fashion_agent

st.set_page_config(page_title="FashionFix AI", layout="wide")
st.title("🧵 FashionFix AI – Your Wardrobe Repair Assistant")

option = st.radio("How do you want help?", ["🖼️ Upload an Outfit Image", "📝 Describe a Clothing Issue"])

if option == "🖼️ Upload an Outfit Image":
    uploaded = st.file_uploader("Upload a clothing image", type=["jpg", "png"])
    if uploaded:
        img = Image.open(uploaded)
        st.image(img, caption="Uploaded Item", use_column_width=True)
        suggestion = fetch_repair_suggestions("image_based_repair")  # simulated
        st.subheader("🧵 Repair/Upcycle Suggestions")
        st.markdown(suggestion)

else:
    issue = st.text_area("Describe your issue (e.g., torn sleeve, faded jeans):")
    if issue:
        suggestion = fetch_repair_suggestions(issue)
        st.subheader("🔧 Repair Tips")
        st.markdown(suggestion)

st.subheader("💬 Ask the AI Fashion Agent")
q = st.text_input("Ask for fashion help...")
if q:
    ans = chat_with_fashion_agent(q)
    st.markdown(ans)
