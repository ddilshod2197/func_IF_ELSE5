def transport_narxi(masofa, transport_turi):
    transport_turi = transport_turi.lower().strip()
    
    if masofa < 0:
        print("Xato: Masofa manfiy bo‘lishi mumkin emas!")
        return
    
    if transport_turi == "taksi":
        narx = 5000 + (masofa * 2000)
    elif transport_turi == "avtobus":
        narx = masofa * 3000
    elif transport_turi == "poezd":
        narx = 10000 + (masofa * 1500)
    else:
        print("Xato: Noto‘g‘ri transport turi! (taksi, avtobus, poezd)")
        return
    
    print(f"Narx: {narx} so‘m")

# Foydalanuvchidan input olish
print("Transport narxi hisoblagich")
masofa = float(input("Masofa (km): "))
transport = input("Transport turi (taksi/avtobus/poezd): ")

transport_narxi(masofa, transport)
