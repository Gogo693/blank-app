import streamlit as st
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

st.title("EdenViaggi URL Modifier")

st.write(
    "Let's start changing URLs in a smart way! :D"
)

url_input = st.text_input(
    "Input URL",
    "https://static.edenviaggi.it/.rest/delivery/pages/edenviaggi-home/vacanze/italia/calabria"
)

url_output_template = st.text_input(
    "Output URL Template (use VALORE as placeholder)",
    "https://static.edenviaggi.it/.rest/delivery/edenviaggi/destination?@jcr:uuid=%22VALORE%22&lang=it"
)

def get_modified_url(url_in, url_out_template):
    try:
        response = requests.get(url_in, headers=headers)
        response.raise_for_status()
        json_response = response.json()
        destination = json_response.get("destination")
        if not destination:
            return None, "Key 'destination' not found in response."
        url_out = url_out_template.replace("VALORE", destination)
        return url_out, None
    except Exception as e:
        return None, f"Error: {e}"

if st.button("Generate Modified URL"):
    url, error = get_modified_url(url_input, url_output_template)
    if url:
        st.success("Modified URL:")
        st.code(url)
    else:
        st.error(error)

