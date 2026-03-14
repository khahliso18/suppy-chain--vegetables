import streamlit as st
import hashlib
from datetime import datetime

st.title("Blockchain Supply Chain Ledger")

if "blockchain" not in st.session_state:
    st.session_state.blockchain = []

def create_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

actor = st.text_input("Actor")
activity = st.text_input("Activity")
product = st.text_input("Product Name")
product_id = st.text_input("Product ID")

if st.button("Add Block"):

    block_number = len(st.session_state.blockchain) + 1
    timestamp = datetime.now()

    prev_hash = "0"
    if len(st.session_state.blockchain) > 0:
        prev_hash = st.session_state.blockchain[-1]["hash"]

    data = f"{block_number}{actor}{activity}{product}{product_id}{timestamp}{prev_hash}"

    current_hash = create_hash(data)

    block = {
        "number": block_number,
        "actor": actor,
        "activity": activity,
        "product": product,
        "product_id": product_id,
        "timestamp": timestamp,
        "prev_hash": prev_hash,
        "hash": current_hash
    }

    st.session_state.blockchain.append(block)

st.header("Blockchain Ledger")

for block in st.session_state.blockchain:
    st.write("### Block", block["number"])
    st.write("Actor:", block["actor"])
    st.write("Activity:", block["activity"])
    st.write("Product:", block["product"])
    st.write("Product ID:", block["product_id"])
    st.write("Timestamp:", block["timestamp"])
    st.write("Previous Hash:", block["prev_hash"])
    st.write("Current Hash:", block["hash"])
    st.write("---")
