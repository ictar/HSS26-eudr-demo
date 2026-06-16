import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import time

st.set_page_config(layout="wide", page_title="EUDR End-to-End Compliance Platform")

st.title("🌍 EUDR AI Compliance End-to-End Platform (MVP Demo)")

# Using Tabs to separate Farmer Interface and Enterprise Interface
tab1, tab2 = st.tabs(["📱 MVC 1: Farmer Minimalist Mapping (Mobile Simulation)", "🏢 MVC 2 & 3: Corporate Compliance & Anti-Greenwashing Engine"])

# ==========================================
# 📱 TAB 1: MVC 1 - The Farmer App
# ==========================================
with tab1:
    st.markdown("### 👨‍🌾 MVC 1 - User: Farmer")
    st.info("💡 Key Highlight: Farmers do not need to walk around the field. Click to locate, and cloud AI automatically generates field polygon boundaries.")
    
    # Simulate mobile screen width
    col_mobile, col_empty = st.columns([1, 2])
    with col_mobile:
        if st.button("📍 Step 1: Get Current Location", use_container_width=True):
            with st.spinner("AI is calling high-resolution satellite maps and segmenting plot boundaries..."):
                time.sleep(2) # Simulate AI inference time
                
            st.success("AI Identification Complete! Please confirm if this is your coffee farm.")
            
            # Render a map with a mock polygon
            m_farmer = folium.Map(location=[9.03, 38.74], zoom_start=16) # Simulate a location in Ethiopia
            # Mock AI-generated polygon boundary
            folium.Polygon(
                locations=[[9.031, 38.741], [9.031, 38.743], [9.029, 38.743], [9.029, 38.741]],
                color="yellow",
                fill=True,
                fill_color="yellow"
            ).add_to(m_farmer)
            st_folium(m_farmer, width=400, height=300)
            
            col_no, col_yes = st.columns(2)
            if col_yes.button("✅ Yes (Submit)", type="primary", use_container_width=True):
                st.toast("Data encrypted and uploaded! Heavy rain expected this week, please check drainage.")
            if col_no.button("❌ No", use_container_width=True):
                st.toast("Switched to manual mapping mode...")

# ==========================================
# 🏢 TAB 2: MVC 2 & 3 - Enterprise Interface
# ==========================================
with tab2:
    st.markdown("### 🏢 Corporate Interface: Bulk Verification & Anti-Greenwashing Engine")
    
    # Mock data including "Declared Volume" to demonstrate anti-greenwashing logic for MVC 3
    mock_data = pd.DataFrame({
        "Supplier": ["Cooperative A", "Farmer B", "Farmer C", "Middleman D"],
        "Lat": [9.03, 8.55, 9.12, 8.99],
        "Lon": [38.74, 39.01, 38.50, 39.12],
        "Area_ha": [2.0, 1.5, 3.0, 1.0], # Actual Area (Hectares)
        "Declared_Volume_tons": [2.8, 2.0, 4.0, 15.0] # Volume declared by supplier (Tons)
    })
    
    st.write("📥 Simulated Uploaded Supplier Data (Notice Middleman D's declared volume):")
    st.dataframe(mock_data, use_container_width=True)
    
    if st.button("🚀 Start AI Spatial Verification & Capacity Audit", type="primary"):
        with st.spinner("Retrieving 2020 satellite baseline and running Mass Balance model..."):
            time.sleep(3)
            
        # --- Core Risk Control Logic (Mock Logic) ---
        # 1. Simulate MVC 2 Deforestation Verification (Mock risk for Farmer B)
        mock_data['Deforestation_Risk'] = ["Safe", "Risk (2022 Deforestation)", "Safe", "Safe"]
        
        # 2. Simulate MVC 3 Anti-Greenwashing (Mass Balance) Logic
        # Assume max coffee yield per hectare is 1.5 tons. If declared volume > area * 1.5, it indicates illicit sourcing.
        MAX_YIELD_PER_HA = 1.5 
        mock_data['Max_Legal_Volume'] = mock_data['Area_ha'] * MAX_YIELD_PER_HA
        mock_data['Greenwash_Fraud'] = mock_data['Declared_Volume_tons'] > mock_data['Max_Legal_Volume']
        
        # Integrate Final Status
        def get_final_status(row):
            if row['Deforestation_Risk'] != "Safe":
                return "🔴 Deforestation Violation"
            if row['Greenwash_Fraud']:
                return "🔴 Volume Fraud (Greenwashing)"
            return "🟢 Compliant"
            
        mock_data['Final_Status'] = mock_data.apply(get_final_status, axis=1)
        
        # --- Data Dashboard Display ---
        st.markdown("### 📊 Audit Results")
        st.dataframe(mock_data[['Supplier', 'Deforestation_Risk', 'Max_Legal_Volume', 'Declared_Volume_tons', 'Final_Status']], use_container_width=True)
        
        # Render corporate macro map
        m_corp = folium.Map(location=[8.9, 38.8], zoom_start=8)
        for idx, row in mock_data.iterrows():
            color = "green" if row['Final_Status'] == "🟢 Compliant" else "red"
            folium.Marker(
                [row['Lat'], row['Lon']],
                popup=f"{row['Supplier']}<br>{row['Final_Status']}",
                icon=folium.Icon(color=color)
            ).add_to(m_corp)
        st_folium(m_corp, width=1000, height=400)
        
        # --- MVC 3: DDS Customs Export ---
        st.markdown("### 📑 One-Click Customs DDS Declaration")
        st.info("💡 The system has automatically excluded non-compliant and fraudulent data, packaging the compliant list into standard EU format.")
        safe_df = mock_data[mock_data['Final_Status'] == "🟢 Compliant"]
        st.download_button(
            label="📥 Download EU TRACES XML Declaration File (Compliant Data Only)",
            data=safe_df.to_csv(index=False).encode('utf-8'),
            file_name='eudr_dds_export.csv',
            mime='text/csv'
        )
