# Dokumentasi Sistem Analisis Ekonomi Lapangan Migas

## Anggota Kelompok
- **Danang Adiwibowo** (123230143)
- **Gorga Doli L N** (123230147)

---

## Deskripsi Proyek

Sistem Analisis Ekonomi Lapangan Migas adalah aplikasi berbasis web yang dirancang untuk melakukan perhitungan ekonomi dan analisis cash flow pada proyek pengembangan lapangan minyak dan gas. Aplikasi ini membantu dalam evaluasi kelayakan ekonomi proyek migas dengan menghitung berbagai indikator ekonomi penting seperti Net Present Value (NPV), Pay Out Time (POT), dan Rate of Return (ROR).

Aplikasi ini dikembangkan sebagai tools bantu untuk mata kuliah Teknik Perminyakan, khususnya dalam analisis ekonomi petroleum. Dengan interface yang user-friendly dan visualisasi data yang informatif, aplikasi ini memudahkan mahasiswa dan praktisi dalam memahami aspek ekonomi dari pengembangan lapangan migas.

---

## Fitur Utama

### 1. Input Parameter Proyek
Aplikasi menerima input lengkap untuk analisis ekonomi:
- **Jangka Waktu Proyek**: Durasi proyek dalam tahun (minimal 7 tahun)
- **Investasi**: Capital dan Non-Capital Investment
- **Data Produksi**: Input produksi tahun 1-7 secara manual
- **Decline Rate**: Laju penurunan produksi per tahun (%)
- **Harga Minyak**: Harga rata-rata minyak per barrel
- **Opex**: Biaya operasional per tahun
- **Metode Depresiasi**: Pilihan 3 metode (Straight Line, Declining Balance, Unit of Production)
- **Tax Rate**: Persentase pajak
- **Discount Rate**: Tingkat diskonto untuk perhitungan NPV

### 2. Perhitungan Ekonomi Otomatis
Sistem melakukan perhitungan otomatis dengan formula:
- **Income** = Produksi × Harga Minyak
- **Depreciation (Di)** = Berdasarkan metode yang dipilih
- **Taxable Income** = Income - Opex - Depreciation
- **Tax** = Tax Rate × Taxable Income
- **NCF** = Taxable Income - Tax

### 3. Indikator Ekonomi
Menampilkan 4 indikator ekonomi utama:
- **NPV (Net Present Value)**: Nilai sekarang dari cash flow
- **POT (Pay Out Time)**: Waktu pengembalian modal
- **ROR (Rate of Return)**: Tingkat pengembalian investasi
- **Total NCF**: Total aliran kas bersih

### 4. Visualisasi Data
Tiga jenis grafik interaktif:
- **Profil Produksi**: Menampilkan tren produksi sepanjang waktu proyek
- **Tren Aliran Kas**: Perbandingan Pendapatan, Opex, dan NCF
- **NCF Kumulatif**: Analisis payback dengan visualisasi bar chart

### 5. Tabel Perhitungan Detail
Tabel lengkap berisi semua perhitungan per tahun dengan kolom:
- Year, Production, Income, Capital, Non-Capital, Opex, Depreciation, Taxable Income, Tax, NCF Undiscounted

### 6. Manajemen Proyek Database
- **Save Project**: Simpan parameter proyek ke database
- **Load Project**: Muat kembali proyek yang tersimpan
- **Update Project**: Otomatis update jika nama proyek sama
- **Delete Project**: Hapus proyek dari database
- **Dropdown**: Pilih proyek tersimpan dengan mudah

### 7. Export Data
- Download tabel perhitungan dalam format CSV untuk analisis lebih lanjut

---

## Tech Stack

### Frontend & Framework
- **Streamlit** (v1.28.0+): Framework web Python untuk membuat interface interaktif
- **HTML/CSS**: Untuk custom styling

### Data Processing & Calculation
- **Pandas** (v2.0.0+): Manipulasi dan analisis data tabular
- **NumPy** (v1.24.0+): Komputasi numerik dan perhitungan matematis

### Data Visualization
- **Plotly** (v5.17.0+): Library untuk membuat grafik interaktif dan dinamis

### Database
- **MySQL**: Database relational untuk menyimpan data proyek
- **mysql-connector-python** (v8.0.0+): Connector Python untuk MySQL

### Tools & Platform
- **Python** 3.8+: Bahasa pemrograman utama
- **XAMPP**: Local server (Apache + MySQL/phpMyAdmin)

---

## Requirements

### System Requirements
- **OS**: Windows, macOS, atau Linux
- **Python**: Version 3.8 atau lebih tinggi
- **RAM**: Minimal 4GB
- **Storage**: Minimal 100MB untuk aplikasi dan database

### Software Requirements
1. **Python 3.8+**
2. **XAMPP** (untuk MySQL dan phpMyAdmin)
3. **Browser Modern** (Chrome, Firefox, Edge, Safari)

### Python Dependencies
```
streamlit>=1.28.0
pandas>=2.0.0
plotly>=5.17.0
numpy>=1.24.0
mysql-connector-python>=8.0.0
```

---

## Instalasi & Setup

### Langkah 1: Install Python
1. Download Python dari [python.org](https://www.python.org/downloads/)
2. Install dengan mencentang "Add Python to PATH"
3. Verifikasi: `python --version`

### Langkah 2: Install XAMPP
1. Download XAMPP dari [apachefriends.org](https://www.apachefriends.org)
2. Install XAMPP
3. Start Apache dan MySQL dari XAMPP Control Panel

### Langkah 3: Setup Database
1. Buka browser, akses `http://localhost/phpmyadmin`
2. Klik tab "SQL"
3. Copy-paste isi file `database_schema.sql`
4. Klik "Go" untuk membuat database

### Langkah 4: Konfigurasi Database
Edit file `db_config.py`:
```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',           # Sesuaikan dengan user MySQL
    'password': '',           # Sesuaikan dengan password MySQL
    'database': 'oil_gas_projects'
}
```

### Langkah 5: Install Dependencies
Buka terminal/command prompt di folder proyek:
```bash
pip install -r requirements.txt
```

### Langkah 6: Jalankan Aplikasi
```bash
streamlit run app.py
```

Aplikasi akan terbuka otomatis di browser pada `http://localhost:8501`

---

## Cara Penggunaan

### A. Membuat Proyek Baru

1. **Pilih "-- Proyek Baru --"** dari dropdown di sidebar
2. **Isi Parameter Proyek**:
   - Jangka Waktu Proyek (minimal 7 tahun)
   - Investasi Capital dan Non-Capital
   - Data Produksi Tahun 1-7
   - Laju Penurunan Produksi (Decline Rate)
   - Harga Minyak rata-rata
   - Biaya Operasional (Opex)
   - Pilih Metode Depresiasi
   - Atur Tax Rate dan Discount Rate

3. **Lihat Hasil Perhitungan**:
   - 4 Indikator ekonomi ditampilkan di bagian atas
   - 3 Grafik analisis ditampilkan
   - Tabel detail perhitungan di bagian bawah

4. **Simpan Proyek** (opsional):
   - Scroll ke bawah sidebar
   - Masukkan nama proyek
   - Klik "Simpan Proyek"

### B. Memuat Proyek Tersimpan

1. **Pilih Nama Proyek** dari dropdown "Muat Proyek Tersimpan"
2. **Klik "Muat Proyek"**
3. Semua parameter otomatis terisi
4. Hasil perhitungan langsung ditampilkan

### C. Update Proyek yang Ada

1. **Muat proyek** yang ingin diupdate
2. **Edit parameter** yang diinginkan
3. **Pastikan nama proyek tetap sama**
4. **Klik "Simpan Proyek"** untuk update

### D. Menghapus Proyek

1. **Pilih proyek** dari dropdown
2. **Klik "Hapus Proyek"**
3. Proyek akan dihapus dari database

### E. Export Data

1. Scroll ke bawah setelah perhitungan selesai
2. Klik tombol **"Unduh Tabel Perhitungan (CSV)"**
3. File CSV akan terdownload

---

## Struktur File Proyek

```
AplikasiProjekMinyak/
│
├── app.py                      # File utama aplikasi Streamlit
├── db_config.py                # Konfigurasi dan fungsi database
├── requirements.txt            # Daftar dependencies Python
│
├── database_schema.sql         # SQL untuk membuat database & tabel
├── sample_data.sql             # Data sample untuk testing
│
├── README.md                   # Dokumentasi singkat
├── DOKUMENTASI_PROYEK.md       # Dokumentasi lengkap (file ini)
├── DATABASE_SETUP.md           # Panduan setup database detail
├── FITUR_SAVE_LOAD.md          # Dokumentasi fitur save/load
│
└── Contoh Kasus FM.docx        # Dokumen case study
```

---

## Metode Perhitungan

### 1. Straight Line Depreciation
Metode depresiasi garis lurus dengan nilai yang sama setiap tahun.
```
Di = Total Investment / Project Duration
```
**Contoh**: $21,000M / 20 tahun = $1,050M per tahun (konstan)

### 2. Declining Balance Depreciation
Metode depresiasi dengan nilai tinggi di awal dan menurun setiap tahun.
```
Rate = 2 / Project Duration
Di = Book Value × Rate
Book Value = Book Value - Di (update setiap tahun)
```
**Contoh**:
- Tahun 1: $21,000M × 10% = $2,100M
- Tahun 2: $18,900M × 10% = $1,890M (terus menurun)

### 3. Unit of Production Depreciation
Metode depresiasi berdasarkan proporsi produksi.
```
Di = (Total Investment / Total Production) × Production per Year
```
Depresiasi mengikuti pola produksi - produksi tinggi maka depresiasi tinggi.

### Perhitungan Indikator Ekonomi

**NPV (Net Present Value)**:
```
NPV = Σ [NCFt / (1 + r)^t]
```
dimana r = discount rate, t = tahun

**POT (Pay Out Time)**:
```
POT = Tahun dimana Cumulative NCF > 0 (pertama kali)
```

**ROR (Rate of Return)**:
```
ROR = (Total NCF / Total Investment) × 100%
```

---

## Database Schema

### Tabel: projects

| Kolom | Tipe Data | Deskripsi |
|-------|-----------|-----------|
| id | INT (PK, AI) | Primary key, auto increment |
| project_name | VARCHAR(255) | Nama proyek (unique) |
| project_duration | INT | Durasi proyek (tahun) |
| capital_investment | DECIMAL(15,2) | Investasi capital ($M) |
| non_capital_investment | DECIMAL(15,2) | Investasi non-capital ($M) |
| production_year_1 | DECIMAL(10,2) | Produksi tahun 1 (Mbbl) |
| production_year_2 | DECIMAL(10,2) | Produksi tahun 2 (Mbbl) |
| production_year_3 | DECIMAL(10,2) | Produksi tahun 3 (Mbbl) |
| production_year_4 | DECIMAL(10,2) | Produksi tahun 4 (Mbbl) |
| production_year_5 | DECIMAL(10,2) | Produksi tahun 5 (Mbbl) |
| production_year_6 | DECIMAL(10,2) | Produksi tahun 6 (Mbbl) |
| production_year_7 | DECIMAL(10,2) | Produksi tahun 7 (Mbbl) |
| decline_rate | DECIMAL(5,2) | Laju penurunan produksi (%) |
| oil_price | DECIMAL(10,2) | Harga minyak ($/bbl) |
| opex_per_year | DECIMAL(15,2) | Opex tahunan ($M) |
| depreciation_method | VARCHAR(50) | Metode depresiasi |
| tax_rate | DECIMAL(5,2) | Tax rate (%) |
| discount_rate | DECIMAL(5,2) | Discount rate (%) |
| created_at | TIMESTAMP | Waktu dibuat |
| updated_at | TIMESTAMP | Waktu update terakhir |

---

## Validasi & Error Handling

### Validasi Input
1. **Project Duration**: Minimal 7 tahun (karena membutuhkan data produksi tahun 1-7)
2. **Project Name**: Tidak boleh kosong saat save
3. **Numeric Values**: Hanya menerima angka positif untuk investasi, produksi, dll

### Error Messages
- **Jangka waktu < 7 tahun**: Warning di sidebar + error di main page
- **Nama proyek kosong**: Error message saat save
- **Database connection failed**: Error message dengan deskripsi masalah
- **Query failed**: Error message untuk operasi database gagal

---

## Troubleshooting

### Error: Can't connect to MySQL server
**Solusi**:
- Pastikan XAMPP MySQL sudah running
- Check port 3306 tidak dipakai aplikasi lain
- Periksa firewall

### Error: Access denied for user
**Solusi**:
- Periksa username dan password di `db_config.py`
- Pastikan user memiliki akses ke database

### Error: Unknown database 'oil_gas_projects'
**Solusi**:
- Jalankan `database_schema.sql` di phpMyAdmin
- Atau buat database manual lewat phpMyAdmin

### Aplikasi tidak jalan / error Python
**Solusi**:
- Pastikan semua dependencies terinstall: `pip install -r requirements.txt`
- Check versi Python: `python --version` (minimal 3.8)

---

## Tips Penggunaan

1. **Backup Data**: Export CSV secara berkala untuk backup data perhitungan
2. **Naming Convention**: Gunakan nama proyek yang deskriptif dan mudah diingat
3. **Testing Parameters**: Coba variasikan parameter untuk analisis sensitivitas
4. **Metode Depresiasi**: Pilih sesuai standar akuntansi perusahaan
5. **Sample Data**: Gunakan `sample_data.sql` untuk data testing

---

## Limitasi

1. Metode depresiasi Unit of Production disederhanakan (tidak memperhitungkan salvage value)
2. Tidak memperhitungkan inflasi
3. Tax dihitung flat rate (tidak progressive)
4. Opex diasumsikan konstan setiap tahun
5. Tidak ada perhitungan IRR (Internal Rate of Return) otomatis

---

## Future Enhancements (Pengembangan Masa Depan)

### Fitur yang Bisa Ditambahkan:
1. **Analisis Sensitivitas**: Otomatis test berbagai skenario parameter
2. **Comparison Mode**: Bandingkan 2 atau lebih proyek side-by-side
3. **IRR Calculator**: Perhitungan Internal Rate of Return
4. **Inflasi & Eskalasi**: Pertimbangkan inflasi dalam perhitungan
5. **Export PDF Report**: Generate laporan lengkap dalam PDF
6. **Multi-user Authentication**: Login system untuk multiple users
7. **Dashboard Analytics**: Summary dashboard untuk semua proyek
8. **API Integration**: Integrasi dengan sistem ERP perusahaan
9. **Mobile Responsive**: Optimasi tampilan untuk mobile device
10. **Advanced Charting**: Lebih banyak pilihan visualisasi data

---

## Referensi

### Dokumentasi Teknis:
- Streamlit Documentation: https://docs.streamlit.io
- Plotly Python: https://plotly.com/python
- MySQL Connector/Python: https://dev.mysql.com/doc/connector-python

### Konsep Petroleum Economics:
- SPE (Society of Petroleum Engineers) Resources
- Petroleum Economics Textbooks
- Case Study: Contoh Kasus FM.docx

---

## Lisensi & Penggunaan

Proyek ini dikembangkan untuk keperluan akademik Mata Kuliah Teknik Perminyakan.

**Diperbolehkan untuk**:
- Penggunaan edukasi dan pembelajaran
- Modifikasi untuk kebutuhan tugas kuliah
- Sharing dengan mahasiswa lain

**Tidak diperbolehkan untuk**:
- Penggunaan komersial tanpa izin
- Distribusi sebagai karya sendiri (plagiarisme)

---

## Kontak & Support

Untuk pertanyaan, bug report, atau saran pengembangan, silakan hubungi:

**Danang Adiwibowo** - 123230143  
**Gorga Doli L N** - 123230147

---

**Version**: 1.0.0  
**Last Updated**: 2026  
**Built with**: ❤️ dan Python
