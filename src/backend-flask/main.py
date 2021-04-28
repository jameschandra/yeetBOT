from flask import Flask, request, jsonify
from command import *
from tanggal import *
from database import *
import sqlite3
import json


app = Flask("__main__")

@app.route("/")
def my_index():
    return "Hello world!"

@app.route("/chat")
def chat_conditionals():
    # connect to db
    conn = create_connection("tasks.db")
    cursor = conn.cursor()

    # get message
    message = request.get_json()["message"] 

    # inisialisasi variabel awal
    tanggal = matkul = tugas = topik = None

    # pencarian tanggal pada message
    if (temp := findTanggal(message)):
        tanggal = temp
    # pencarian matkul pada message
    if (temp := findMatkul(message)):
        matkul = temp
    # pencarian jenis tugas pada message
    if (temp := findTask(message)):
        tugas = temp
    # pencarian topik pada message
    if (temp := findTopik(message)):
        topik = temp


    # test untuk POST tanggal, matkul, tugas dan topik
    if (tanggal and matkul and tugas and topik):
        insert_task = """INSERT INTO tasks (tanggal, matkul, tugas, topik)
                         VALUES (?, ?, ?, ?)"""
        cursor = conn.execute(insert_task, (tanggal[0], matkul[0].upper(), tugas, topik[0]))
        conn.commit()

        return f"[TASK BERHASIL DICATAT]\n(ID: {cursor.lastrowid}) {tanggal[0]} - {matkul[0].upper()} - {tugas} - {topik[0]}"
    
    # test untuk GET (harus ada kata deadline)
    elif (findWord(message, "deadline")):
        # test untuk GET all
        if (findWord(message, "semua") or findWord(message, "sejauh")):
            # kasus terdapat filter task
            if (tugas):
                get_deadline = """SELECT * FROM tasks
                                  WHERE tugas = ?"""
                cursor = conn.execute(get_deadline, [tugas])
            else: # tidak ada filter tugas
                get_deadline = """SELECT * FROM tasks"""
                cursor = conn.execute(get_deadline)
        # test untuk GET between 2 tanggal
        elif (tanggal and len(tanggal) == 2):
            # kasus terdapat filter task
            if (tugas):
                get_deadline = """SELECT * FROM tasks
                                  WHERE tugas = ? AND tanggal >= ? AND tanggal <= ?"""
                cursor = conn.execute(get_deadline, [tugas, tanggal[0], tanggal[1]])
            else: # tidak ada filter tugas
                get_deadline = """SELECT * FROM tasks
                                  WHERE tanggal >= ? AND tanggal <= ?"""
                cursor = conn.execute(get_deadline, [tanggal[0], tanggal[1]])

        results = cursor.fetchall()                
        retString = ""

        for i in range(len(results)):
            retString += f"\n{i+1}. (ID: {results[i][0]}) {results[i][1]} - {results[i][2]} - {results[i][3]} - {results[i][4]}"

        return f"[Daftar Deadline]{retString}"
    
    # close connection to db
    conn.close()

    return ""

if __name__ == "__main__":
    app.run(debug=True)