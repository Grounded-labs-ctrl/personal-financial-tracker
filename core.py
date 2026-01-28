# core.py
vault = {
    "pengeluaran": {},
    "pemasukan": {}
}

def tambah_kategori_pengeluaran(nama, pake_budget, nominal=0):
    # Logika untuk menyuntikkan data ke vault
    # Di sini lo tinggal fokus ke gimana data masuk
    if pake_budget:
        vault["pengeluaran"][nama] = {"budget": nominal, "terpakai": 0, "history": []}
    else:
        vault["pengeluaran"][nama] = {"budget": None, "terpakai": 0, "history": []}