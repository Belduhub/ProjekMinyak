import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from db_config import save_project, load_project, get_all_project_names, delete_project

# Konfigurasi halaman
st.set_page_config(
    page_title="Dashboard Ekonomi Lapangan Migas",
    page_icon="⬛",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #1a1a1a;
    }
    .stMetric {
        background-color: #2d2d2d;
        padding: 20px;
        border-radius: 8px;
        border: 1px solid #404040;
    }
    .stMetric label {
        color: #b0b0b0 !important;
        font-weight: 600;
    }
    .stMetric [data-testid="stMetricValue"] {
        color: #ffffff;
        font-size: 28px;
    }
    h1, h2, h3 {
        color: #ffffff;
    }
    .sidebar .sidebar-content {
        background-color: #2d2d2d;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align: center;'>Sistem Analisis Ekonomi Lapangan Migas</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #b0b0b0;'>Perhitungan Cash Flow & Indikator Ekonomi</h3>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar - Info kelompok
st.sidebar.markdown("### Kelompok")
st.sidebar.markdown("""
**Danang Adiwibowo**  
(123230143)

**Gorga Doli L N**  
(123230147)
""")
st.sidebar.markdown("---")

st.sidebar.subheader("Manajemen Proyek")

saved_projects = get_all_project_names()

selected_project = st.sidebar.selectbox(
    "Muat Proyek Tersimpan",
    options=["-- Proyek Baru --"] + saved_projects,
    key="project_selector"
)

if selected_project != "-- Proyek Baru --":
    if st.sidebar.button("Muat Proyek"):
        loaded_data = load_project(selected_project)
        if loaded_data:
            st.session_state['loaded_project'] = loaded_data
            st.sidebar.success(f"Proyek '{selected_project}' berhasil dimuat!")
            st.rerun()

if 'loaded_project' not in st.session_state:
    st.session_state['loaded_project'] = None

loaded = st.session_state['loaded_project']

st.sidebar.markdown("---")

project_duration = st.sidebar.number_input(
    "Jangka Waktu Proyek (tahun)", 
    min_value=1, 
    max_value=100, 
    value=int(loaded['project_duration']) if loaded else 20, 
    step=1
)

if project_duration < 7:
    st.sidebar.error("Jangka waktu proyek harus minimal 7 tahun!")
    st.sidebar.warning("Data produksi membutuhkan input untuk Tahun 1 sampai 7.")

st.sidebar.subheader("Investasi")
capital_investment = st.sidebar.number_input(
    "Investasi Capital ($M)", 
    min_value=0.0, 
    value=float(loaded['capital_investment']) if loaded else 13000.0, 
    step=100.0
)
non_capital_investment = st.sidebar.number_input(
    "Investasi Non-Capital ($M)", 
    min_value=0.0, 
    value=float(loaded['non_capital_investment']) if loaded else 8000.0, 
    step=100.0
)
total_investment = capital_investment + non_capital_investment

st.sidebar.subheader("Data Produksi (Tahun 1-7)")
production_year_1 = st.sidebar.number_input(
    "Produksi Tahun 1 (Mbbl)", 
    min_value=0.0, 
    value=float(loaded['production_year_1']) if loaded else 175.0, 
    step=1.0
)
production_year_2 = st.sidebar.number_input(
    "Produksi Tahun 2 (Mbbl)", 
    min_value=0.0, 
    value=float(loaded['production_year_2']) if loaded else 201.0, 
    step=1.0
)
production_year_3 = st.sidebar.number_input(
    "Produksi Tahun 3 (Mbbl)", 
    min_value=0.0, 
    value=float(loaded['production_year_3']) if loaded else 217.0, 
    step=1.0
)
production_year_4 = st.sidebar.number_input(
    "Produksi Tahun 4 (Mbbl)", 
    min_value=0.0, 
    value=float(loaded['production_year_4']) if loaded else 198.0, 
    step=1.0
)
production_year_5 = st.sidebar.number_input(
    "Produksi Tahun 5 (Mbbl)", 
    min_value=0.0, 
    value=float(loaded['production_year_5']) if loaded else 192.06, 
    step=1.0
)
production_year_6 = st.sidebar.number_input(
    "Produksi Tahun 6 (Mbbl)", 
    min_value=0.0, 
    value=float(loaded['production_year_6']) if loaded else 186.29, 
    step=1.0
)
production_year_7 = st.sidebar.number_input(
    "Produksi Tahun 7 (Mbbl)", 
    min_value=0.0, 
    value=float(loaded['production_year_7']) if loaded else 180.70, 
    step=1.0
)

decline_rate = st.sidebar.slider(
    "Laju Penurunan Produksi (%)", 
    min_value=0.0, 
    max_value=100.0, 
    value=float(loaded['decline_rate']) if loaded else 3.0, 
    step=0.1
)

oil_price = st.sidebar.number_input(
    "Harga Minyak Rata-rata ($/bbl)", 
    min_value=0.0, 
    value=float(loaded['oil_price']) if loaded else 32.0, 
    step=1.0
)

opex_per_year = st.sidebar.number_input(
    "Biaya Operasional per Tahun (Opex) ($M)", 
    min_value=0.0, 
    value=float(loaded['opex_per_year']) if loaded else 180.0, 
    step=10.0
)

depreciation_method = st.sidebar.selectbox(
    "Metode Depresiasi", 
    ["Straight Line", "Declining Balance", "Unit of Production"],
    index=["Straight Line", "Declining Balance", "Unit of Production"].index(loaded['depreciation_method']) if loaded else 0
)

tax_rate = st.sidebar.slider(
    "Tarif Pajak (%)", 
    min_value=0.0, 
    max_value=100.0, 
    value=float(loaded['tax_rate']) if loaded else 51.0, 
    step=0.5
) / 100

discount_rate = st.sidebar.slider(
    "Tingkat Diskonto untuk NPV (%)", 
    min_value=0.0, 
    max_value=100.0, 
    value=float(loaded['discount_rate']) if loaded else 10.0, 
    step=0.5
) / 100

# Simpan proyek
st.sidebar.markdown("---")
st.sidebar.subheader("Simpan Proyek")
project_name = st.sidebar.text_input("Nama Proyek", value=selected_project if selected_project != "-- Proyek Baru --" else "")

col_save, col_delete = st.sidebar.columns(2)
with col_save:
    if st.button("Simpan Proyek", use_container_width=True):
        if project_name.strip() == "":
            st.sidebar.error("Mohon masukkan nama proyek!")
        elif project_duration < 7:
            st.sidebar.error("Tidak bisa menyimpan! Jangka waktu proyek harus minimal 7 tahun.")
        else:
            project_data = {
                'project_name': project_name.strip(),
                'project_duration': project_duration,
                'capital_investment': capital_investment,
                'non_capital_investment': non_capital_investment,
                'production_year_1': production_year_1,
                'production_year_2': production_year_2,
                'production_year_3': production_year_3,
                'production_year_4': production_year_4,
                'production_year_5': production_year_5,
                'production_year_6': production_year_6,
                'production_year_7': production_year_7,
                'decline_rate': decline_rate,
                'oil_price': oil_price,
                'opex_per_year': opex_per_year,
                'depreciation_method': depreciation_method,
                'tax_rate': tax_rate * 100,
                'discount_rate': discount_rate * 100
            }
            if save_project(project_data):
                st.sidebar.success(f"Proyek '{project_name}' berhasil disimpan!")
                st.rerun()
            else:
                st.sidebar.error("Gagal menyimpan proyek!")

with col_delete:
    if st.button("Hapus Proyek", use_container_width=True):
        if selected_project != "-- Proyek Baru --":
            if delete_project(selected_project):
                st.sidebar.success(f"Proyek '{selected_project}' berhasil dihapus!")
                st.session_state['loaded_project'] = None
                st.rerun()
            else:
                st.sidebar.error("Gagal menghapus proyek!")
        else:
            st.sidebar.warning("Tidak ada proyek yang dipilih untuk dihapus!")


# Hitung produksi untuk tahun berikutnya
production_data = [
    production_year_1, production_year_2, production_year_3, production_year_4,
    production_year_5, production_year_6, production_year_7
]

if project_duration < 7:
    st.error("Kesalahan: Jangka waktu proyek harus minimal 7 tahun!")
    st.warning("Silakan sesuaikan jangka waktu proyek di panel samping untuk melanjutkan.")
    st.info("Input data produksi membutuhkan data dari Tahun 1 sampai Tahun 7 (minimal 7 tahun).")
    st.stop()

last_production = production_year_7
for year in range(8, project_duration + 1):
    next_production = last_production * (1 - decline_rate / 100)
    production_data.append(next_production)
    last_production = next_production

# Hitung depresiasi berdasarkan metode yang dipilih
if depreciation_method == "Straight Line":
    depreciation_per_year = [total_investment / project_duration] * project_duration
    
elif depreciation_method == "Declining Balance":
    rate = 2 / project_duration
    book_value = total_investment
    depreciation_per_year = []
    
    for year in range(project_duration):
        depreciation = book_value * rate
        if depreciation > book_value:
            depreciation = book_value
        depreciation_per_year.append(depreciation)
        book_value -= depreciation
        
else:
    total_production = sum(production_data)
    depreciation_per_year = []
    
    for prod in production_data:
        depreciation = (total_investment / total_production) * prod
        depreciation_per_year.append(depreciation)

# Buat tabel perhitungan
years = list(range(0, project_duration + 1))
data = {
    'Year': years,
    'Production (Mbbl)': [0] + production_data,
    'Income ($M)': [0] + [prod * oil_price for prod in production_data],
    'Capital ($M)': [capital_investment] + [0] * project_duration,
    'Non-Capital ($M)': [non_capital_investment] + [0] * project_duration,
    'Opex ($M)': [0] + [opex_per_year] * project_duration,
    'Depreciation ($M)': [0] + depreciation_per_year,
}

# Hitung taxable income, tax, dan NCF
taxable_income = []
tax = []
ncf = []

for i in range(len(years)):
    if i == 0:
        taxable_income.append(0)
        tax.append(0)
        ncf.append(-total_investment)
    else:
        ti = data['Income ($M)'][i] - data['Opex ($M)'][i] - data['Depreciation ($M)'][i]
        taxable_income.append(ti)
        
        t = ti * tax_rate if ti > 0 else 0
        tax.append(t)
        
        ncf_value = ti - t
        ncf.append(ncf_value)

data['Taxable Income ($M)'] = taxable_income
data['Tax ($M)'] = tax
data['NCF Undiscounted ($M)'] = ncf

df = pd.DataFrame(data)

# Hitung indikator ekonomi
total_ncf = sum(ncf)
npv = sum([ncf[i] / ((1 + discount_rate) ** i) for i in range(len(ncf))])

cumulative_ncf = np.cumsum(ncf)
pot = None
for i, cum_ncf in enumerate(cumulative_ncf):
    if cum_ncf > 0:
        pot = i
        break
if pot is None:
    pot = "N/A"

total_revenue = sum([data['Income ($M)'][i] for i in range(1, len(years))])
ror = ((total_ncf / total_investment) * 100) if total_investment > 0 else 0

# Tampilkan indikator ekonomi
st.subheader("Indikator Ekonomi Utama")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Net Present Value (NPV)", f"${npv:,.2f}M", delta=None)

with col2:
    st.metric("Pay Out Time (POT)", f"{pot} tahun" if pot != "N/A" else "N/A", delta=None)

with col3:
    st.metric("Rate of Return (ROR)", f"{ror:.2f}%", delta=None)

with col4:
    st.metric("Total NCF", f"${total_ncf:,.2f}M", delta=None)

st.markdown("---")

st.subheader("Analisis Teknis")

col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    fig_production = go.Figure()
    fig_production.add_trace(go.Scatter(
        x=df['Year'][1:],
        y=df['Production (Mbbl)'][1:],
        mode='lines+markers',
        name='Produksi',
        line=dict(color='#6c9bd1', width=2.5),
        marker=dict(size=6, color='#6c9bd1'),
        fill='tozeroy',
        fillcolor='rgba(108, 155, 209, 0.2)'
    ))
    
    fig_production.update_layout(
        title='Profil Produksi Sepanjang Waktu',
        xaxis_title='Tahun',
        yaxis_title='Produksi (Mbbl)',
        template='plotly_dark',
        plot_bgcolor='#1a1a1a',
        paper_bgcolor='#1a1a1a',
        font=dict(color='#ffffff'),
        title_font=dict(color='#ffffff', size=16),
        hovermode='x unified'
    )
    
    st.plotly_chart(fig_production, use_container_width=True)

with col_chart2:
    fig_cashflow = go.Figure()
    
    fig_cashflow.add_trace(go.Scatter(
        x=df['Year'][1:],
        y=df['Income ($M)'][1:],
        mode='lines',
        name='Pendapatan',
        line=dict(color='#7fb069', width=2.5)
    ))
    
    fig_cashflow.add_trace(go.Scatter(
        x=df['Year'][1:],
        y=df['Opex ($M)'][1:],
        mode='lines',
        name='Opex',
        line=dict(color='#d97373', width=2.5)
    ))
    
    fig_cashflow.add_trace(go.Scatter(
        x=df['Year'][1:],
        y=df['NCF Undiscounted ($M)'][1:],
        mode='lines+markers',
        name='NCF',
        line=dict(color='#e8c468', width=2.5),
        marker=dict(size=5)
    ))
    
    fig_cashflow.update_layout(
        title='Tren Aliran Kas',
        xaxis_title='Tahun',
        yaxis_title='Jumlah ($M)',
        template='plotly_dark',
        plot_bgcolor='#1a1a1a',
        paper_bgcolor='#1a1a1a',
        font=dict(color='#ffffff'),
        title_font=dict(color='#ffffff', size=16),
        hovermode='x unified',
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
    )
    
    st.plotly_chart(fig_cashflow, use_container_width=True)

st.subheader("Aliran Kas Bersih Kumulatif")
fig_cumulative = go.Figure()

cumulative_ncf_list = cumulative_ncf.tolist()
colors = ['#d97373' if x < 0 else '#7fb069' for x in cumulative_ncf_list]

fig_cumulative.add_trace(go.Bar(
    x=df['Year'],
    y=cumulative_ncf_list,
    marker=dict(
        color=colors,
        line=dict(color='#1a1a1a', width=1)
    ),
    name='NCF Kumulatif'
))

fig_cumulative.add_hline(y=0, line_dash="dash", line_color="#808080", line_width=2)

fig_cumulative.update_layout(
    title='Aliran Kas Bersih Kumulatif (Analisis Payback)',
    xaxis_title='Tahun',
    yaxis_title='NCF Kumulatif ($M)',
    template='plotly_dark',
    plot_bgcolor='#1a1a1a',
    paper_bgcolor='#1a1a1a',
    font=dict(color='#ffffff'),
    title_font=dict(color='#ffffff', size=16),
    showlegend=False
)

st.plotly_chart(fig_cumulative, use_container_width=True)

st.markdown("---")

st.subheader("Tabel Perhitungan Detail")

df_display = df.copy()
for col in df_display.columns:
    if col != 'Year':
        df_display[col] = df_display[col].apply(lambda x: f"{x:,.2f}")

st.dataframe(
    df_display,
    use_container_width=True,
    height=400
)

st.download_button(
    label="Unduh Tabel Perhitungan (CSV)",
    data=df.to_csv(index=False).encode('utf-8'),
    file_name='analisis_ekonomi_migas.csv',
    mime='text/csv',
)

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #808080;'>Sistem Analisis Ekonomi Lapangan Migas</p>",
    unsafe_allow_html=True
)
