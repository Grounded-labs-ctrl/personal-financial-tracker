#kita bikin template buat kategori nantinya, agar ga berubah ubah
def template_kategori(name, budget=0):
    return{
        "name" : name,
        "budget" : budget,
        "terpakai" : 0,
        "history" : []
    }