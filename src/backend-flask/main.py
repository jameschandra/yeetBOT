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

    # pencarian tanggal pada message
    if (temp := findTanggal(message)):
        tanggal = temp
    # pencarian jenis tugas pada message
    if (temp := findTask(message)):
        tugas = temp

    # test untuk POST tanggal, matkul, tugas dan topik
    if (temp and findMatkul(message) and findTask(message) and findTopik(message)):
        foundMatkul = findMatkul(message)[0]
        foundTask = findTask(message)
        foundTopik = findTopik(message)[0]

        insert_task = """INSERT INTO tasks (tanggal, matkul, tugas, topik)
                         VALUES (?, ?, ?, ?)"""
        cursor = conn.execute(insert_task, (tanggal[0], foundMatkul, foundTask, foundTopik))
        conn.commit()

        return f"[TASK BERHASIL DICATAT]\n(ID: {cursor.lastrowid}) {tanggal[0]} - {foundMatkul} - {foundTask} - {foundTopik}"
    # test untuk GET (harus ada kata deadline)
    elif (findWord("deadline")):
        # test untuk GET all
        if (findWord("apa")):
            # kasus terdapat filter task
            if (findTask(kalimat)):
                get_deadline = """SELECT tanggal FROM tasks
                                  WHERE """
                cursor = conn.execute(insert_task, (foundTanggal, foundMatkul, foundTask, foundTopik))


    return ""

if __name__ == "__main__":
    app.run(debug=True)