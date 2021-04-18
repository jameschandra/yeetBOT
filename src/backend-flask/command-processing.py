import string-matching

command = input("> ")

if ("""ada TANGGAL, MATKUL, JENIS, TOPIK"""):
    # nambah task baru
elif ("""ada APA, DEADLINE, ((DATE1 & DATE2)/(N & (HARI/MINGGU) & DEPAN)/HARI INI)/[jenis task]"""):
    # nampilin daftar task
elif ("""ada DEADLINE, MATKUL"""):
    # nampilin deadline tugas
elif ("""ada ID, UNDUR/MAJU, KODE MATKUL, TANGGAL"""):
    # memperbarui task
elif ("""ada SELESAI/BERES, ID TASK"""):
    # menandai task selesai
elif ("""ada ASSISTANT, BISA, APA"""):
    # menampilkan opsi help
else:
    print("Maaf, pesan tidak dikenali")