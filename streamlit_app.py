import streamlit as st

st.header("Smart Typography Demo")

st.markdown("""
This demo showcases the smart typography features integrated into Streamlit. 
Enter text in the box below to see how specific character sequences are automatically transformed.

Examples to try:
- Enter `->` to see it transform into a right arrow (→)
- Enter `<-` for a left arrow (←)
- Type `--` to get an em dash (—)
- Type `>=` for a greater than or equal to sign (≥)
- Type `<=` for a less than or equal to sign (≤)
- Use `~=` for approximately equal to (≈)
- Try `-->` for a long right arrow (⟶)
- Try `<--` for a long left arrow (⟵)
- Use `<->` for a left-right arrow (↔)
- Type `<-->` for a long left-right arrow (⟷)
""")

user_input = st.text_input('Enter some text to see smart typography in action:', placeholder='z <= x >= y <--> x ~= y')
st.markdown(user_input)
