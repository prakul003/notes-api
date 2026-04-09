from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# -------- DATABASE CONNECTION --------
def get_db():
    return sqlite3.connect('notes.db')

# -------- CREATE TABLE --------
def init_db():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT
    )
    ''')

    conn.commit()
    conn.close()

init_db()

# -------- CREATE NOTE --------
@app.route('/notes', methods=['POST'])
def create_note():
    data = request.json

    title = data.get('title')
    content = data.get('content')

    if not title or not content:
        return jsonify({"error": "Title and content required"}), 400

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    conn.close()

    return jsonify({"message": "Note created successfully"}), 201

# -------- GET ALL NOTES --------
@app.route('/notes', methods=['GET'])
def get_notes():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()

    conn.close()

    return jsonify(notes)

# -------- DELETE NOTE --------
@app.route('/notes/<int:id>', methods=['DELETE'])
def delete_note(id):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM notes WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Note deleted successfully"})

# -------- SEARCH NOTES --------
@app.route('/search', methods=['GET'])
def search_notes():
    query = request.args.get('q')

    if not query:
        return jsonify({"error": "Empty search query"}), 400

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM notes
        WHERE title LIKE ? OR content LIKE ?
    """, (f'%{query}%', f'%{query}%'))

    results = cursor.fetchall()
    conn.close()

    if not results:
        return jsonify({"message": "No matching results"}), 404

    return jsonify(results)

# -------- RUN SERVER --------
if __name__ == '__main__':
    app.run(debug=True)