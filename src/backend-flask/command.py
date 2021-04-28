import re
import kmp

def findWord(teks, pattern):
    kmptable = []
    
    if(kmp.kmp(teks.lower(), pattern.lower(), kmptable) == -1):
        return False
    else:
        return True

def findNumberAfterWord(text, word):
    return re.findall(r'%s\s(\d+)' % word, text.lower())

def findNumberBeforeWord(text, word):
    return re.findall(r'(\d+)\s%s' % word, text.lower())

def findMatkul(text):
    matkul = re.search('([a-zA-Z])+[0-9][0-9][0-9][0-9]', text)

    return matkul

def findTopik(text):
    topics = re.findall(r'"([^"]*)"', text)

    return topics

def findTask(kalimat):
    if (findWord(kalimat, "tubes")):
        return "Tubes"
    elif (findWord(kalimat, "tucil")):
        return "Tucil"
    elif (findWord(kalimat, "kuis")):
        return "Kuis"
    elif (findWord(kalimat, "ujian")):
        return "Ujian"
    elif (findWord(kalimat, "praktikum")):
        return "Praktikum"

# if ("""ada TANGGAL, MATKUL, JENIS, TOPIK"""):
#     # nambah task baru
# elif ("""ada APA, DEADLINE, ((DATE1 & DATE2)/(N & (HARI/MINGGU) & DEPAN)/HARI INI)/[jenis task]"""):
#     # nampilin daftar task
# elif ("""ada DEADLINE, MATKUL"""):
#     # nampilin deadline tugas
# elif ("""ada ID, UNDUR/MAJU, KODE MATKUL, TANGGAL"""):
#     # memperbarui task
# elif ("""ada SELESAI/BERES, ID TASK"""):
#     # menandai task selesai
# elif ("""ada ASSISTANT, BISA, APA"""):
#     # menampilkan opsi help
# else:
#     print("Maaf, pesan tidak dikenali")