def lev(typo, bener):
    typo = "#" + typo
    bener = "#" + bener
    matriks = [[0 for i in range(len(bener))]for j in range(len(typo))]
    for i in range(len(typo)):
        for j in range(len(bener)):
            if(min(i,j) == 0):
                matriks[i][j] = max(i,j)
            else:
                a = matriks[i-1][j] + 1
                b = matriks[i][j-1] + 1
                c = matriks[i-1][j-1]
                if(typo[i] != bener[j]):
                    c+=1
                matriks[i][j] = min(a,b,c)
    distance = matriks[len(typo)-1][len(bener)-1]
    return distance / max(len(typo)-1, len(bener)-1)
    
def reccomendWord(kalimat):
    daftar = ["deadline", "semua", "sejauh", "hari ini", "tugas", "undur", "maju", "update", "selesai", "delete", "apa", "lakukan", "bisa"]
    kalimat = kalimat.split()
    similar = [[0 for i in range(len(kalimat))] for j in range(len(daftar))]
    for i in range(len(daftar)):
        for j in range(len(kalimat)):
            similar[i][j] = lev(daftar[i],kalimat[j])
    solusi  = 1
    for j in range(len(kalimat)):
        for i in range(len(daftar)):
            a = min(solusi, similar[i][j])
            if a != solusi:
                kalimat[j] = daftar[i]
                solusi = a
    return "Maaf, pesan tidak dikenali\nMungkin maksud Anda:\n" + " ".join(kalimat)