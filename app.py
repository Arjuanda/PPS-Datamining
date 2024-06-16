from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import pymysql
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)

def create_connection():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='dbpbl',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection
app.secret_key = 'e1842e8c4bde416b66e51224fe8864e9'

@app.route('/', methods=['GET'])
def login():
    return render_template('/auth/login.html')

@app.route('/verifikasi-login', methods=['POST'])
def verifikasiLogin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM admin WHERE email = %s AND password = %s', (email, password))
        admin = cursor.fetchone()
        cursor.close()

        connection.close()

        if admin:
            admin_session_data = {
                'id': admin['id_admin'],
                'email': admin['email']
            }
            session['id_admin'] = admin_session_data['id']
            flash('Login berhasil. Selamat datang!', 'success')
            return redirect('/dashboard')  # Sesuaikan dengan rute dashboard yang sesuai
        else:
            flash('Email atau password salah', 'error')
            return redirect('/')

@app.route('/register')
def register():
    return render_template('/auth/register.html')

def count_item_siswa():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) AS count FROM siswa")
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result['count']

def count_item_prodi():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) AS count FROM prodi")
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result['count']

def count_item_nilai():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) AS count FROM nilai")
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result['count']

def count_item_user():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) AS count FROM siswa")
    result_siswa = cursor.fetchone()
    cursor.execute("SELECT COUNT(*) AS count FROM admin")
    result_admin = cursor.fetchone()
    total_count = result_siswa['count'] + result_admin['count']
    cursor.close()
    connection.close()
    return total_count

def log_activity(id_admin, action):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO log (id_admin, action) VALUES (%s, %s)", (id_admin, action))
    connection.commit()
    cursor.close()
    connection.close()

@app.route('/dashboard', methods=['GET'])
def dashboard():
    if 'id_admin' in session:
        siswa = count_item_siswa()
        user = count_item_user()
        prodi = count_item_prodi()
        nilai = count_item_nilai()
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute('''
        SELECT log.id_log, admin.nama, log.action, log.timestamp
        FROM log
        JOIN admin ON log.id_admin = admin.id_admin
        ORDER BY log.timestamp DESC
        ''')
        logs = cursor.fetchall()
        cursor.close()
        connection.close()
        return render_template('dashboard.html', count_siswa=siswa, count_user=user, count_nilai=nilai, count_prodi=prodi, logs = logs)
    else:
        return redirect('/')
    


#User

@app.route('/user', methods=['GET'])
def data_user():
    if 'id_admin' in session:
        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute('SELECT id_admin, nama, email, password, nip, alamat, kontak, gambar FROM admin ORDER BY id_admin DESC')
        data_admin = cursor.fetchall()

        cursor.execute('SELECT id_siswa, nisn, nama, email, password, tempat_lahir, tanggal_lahir, jenis_kelamin, sekolah_asal, jurusan, kontak, alamat, gambar FROM siswa ORDER BY id_siswa DESC')
        data_siswa = cursor.fetchall()

        cursor.close()
        connection.close()

        return render_template('user/data-user.html', admin=data_admin, siswa=data_siswa)
    else:
        return redirect('/')


UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS  
 
def get_default_image():
    default_image = os.path.join(app.config['UPLOAD_FOLDER'], 'default.png')
    return default_image.replace('\\', '/')
def get_default_image2():
    default_image = os.path.join(app.config['UPLOAD_FOLDER'], 'default2.jpg')
    return default_image.replace('\\', '/')

# Siswa

@app.route('/siswa/tambah', methods=['GET', 'POST'])
def tambah_siswa():
    if 'id_admin' in session:
        if request.method == 'POST':
            nisn = request.form['nisn']
            nama = request.form['nama']
            email = request.form['email']
            password = request.form['password']
            tempat_lahir = request.form['tempat_lahir']
            tanggal_lahir = request.form['tanggal_lahir']
            jenis_kelamin = request.form['jenis_kelamin']
            sekolah_asal = request.form['sekolah_asal']
            jurusan = request.form['jurusan']
            kontak = request.form['kontak']
            alamat = request.form['alamat']
            gambar = None

            if 'gambar' in request.files:
                file = request.files['gambar']
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(file_path)
                    gambar = file_path
                    gambar = file_path.replace('\\', '/')


            if not gambar:
                gambar = get_default_image()

            connection = create_connection()
            cursor = connection.cursor()

            cursor.execute("INSERT INTO siswa (nisn, nama, email, password, tempat_lahir, tanggal_lahir, jenis_kelamin, sekolah_asal, jurusan, kontak, alamat, gambar) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                           (nisn, nama, email, password, tempat_lahir, tanggal_lahir, jenis_kelamin, sekolah_asal, jurusan, kontak, alamat, gambar))

            connection.commit()
            cursor.close()
            connection.close()

            id_admin = session['id_admin']
            action = f"Added: {nama}"
            log_activity(id_admin, action)
            flash('Data siswa berhasil ditambahkan!', 'success')
            return redirect(url_for('data_user'))
        
        else:
            return render_template('siswa/tambah-siswa.html')
    else:
        return redirect('/')

@app.route('/siswa/detail/<int:id>', methods=['GET'])
def detail_siswa(id):  
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM siswa WHERE id_siswa = %s', (id,))
    siswa = cursor.fetchone()
    if not siswa:
        return 'Student not found', 404
    return render_template('siswa/detail-siswa.html', siswa=siswa)
    
@app.route('/siswa/edit/<int:id>', methods=['GET', 'POST'])
def edit_siswa(id):
    if 'id_admin' in session:
        if request.method == 'POST':
            nisn = request.form['nisn']
            nama = request.form['nama']
            email = request.form['email']
            password = request.form['password']
            tempat_lahir = request.form['tempat_lahir']
            tanggal_lahir = request.form['tanggal_lahir']
            jenis_kelamin = request.form['jenis_kelamin']
            sekolah_asal = request.form['sekolah_asal']
            jurusan = request.form['jurusan']
            kontak = request.form['kontak']
            alamat = request.form['alamat']
            gambar = None

            if 'gambar' in request.files:
                file = request.files['gambar']
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(file_path)
                    gambar = file_path
                    gambar = file_path.replace('\\', '/')

            if not gambar and 'gambarLama' in request.form:
                gambar = request.form['gambarLama'].replace('\\', '/')
            else:
                gambar = get_default_image()

            connection = create_connection()
            cursor = connection.cursor()

            cursor.execute("""
                UPDATE siswa
                SET nisn = %s,  nama = %s, email = %s, password = %s, tempat_lahir = %s, tanggal_lahir = %s, jenis_kelamin = %s, sekolah_asal = %s, jurusan = %s, kontak = %s, alamat = %s, gambar = %s
                WHERE id_siswa = %s
            """, (nisn, nama, email, password, tempat_lahir, tanggal_lahir, jenis_kelamin, sekolah_asal, jurusan, kontak, alamat, gambar, id))

            connection.commit()
            cursor.close()
            connection.close()

            id_admin = session['id_admin']
            action = f"Editted: {nama}"
            log_activity(id_admin, action)
            flash('Data siswa berhasil diubah!', 'success')
            return redirect(url_for('data_user'))
        else:
            connection = create_connection()
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM siswa WHERE id_siswa = %s", (id,))
            data_siswa = cursor.fetchone()
            cursor.close()
            connection.close()

            if data_siswa and data_siswa['gambar']:
                data_siswa['gambar'] = data_siswa['gambar'].replace('\\', '/')


            return render_template('siswa/edit-siswa.html', siswa=data_siswa)
    else:
        return redirect('/')

@app.route('/siswa/delete/<int:id>', methods=['GET'])
def delete_siswa(id):
    if 'id_admin' in session:
        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute('SELECT nama FROM siswa WHERE id_siswa = %s', (id,))
        siswa = cursor.fetchone()
        if siswa:
            nama = siswa['nama']

            cursor.execute('DELETE FROM siswa WHERE id_siswa = %s', (id,))
            connection.commit()
            cursor.close()
            connection.close()

            id_admin = session['id_admin']
            action = f"Deleted: {nama}"
            log_activity(id_admin, action)
        flash('Data siswa berhasil dihapus!', 'success')
        return redirect(url_for('data_user'))
    else:
        return redirect('/')

#Admin

@app.route('/admin/tambah', methods=['GET', 'POST'])
def tambah_admin():
    if 'id_admin' in session:
        if request.method == 'POST':
            nip = request.form['nip']
            nama = request.form['nama']
            email = request.form['email']
            password = request.form['password']
            kontak = request.form['kontak']
            alamat = request.form['alamat']
            gambar = None

            if 'gambar' in request.files:
                file = request.files['gambar']
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(file_path)
                    gambar = file_path
                    gambar = file_path.replace('\\', '/')


            if not gambar:
                gambar = get_default_image()

            connection = create_connection()
            cursor = connection.cursor()

            cursor.execute("INSERT INTO admin (nip, nama, email, password, kontak, alamat, gambar) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                           (nip, nama, email, password, kontak, alamat, gambar))

            connection.commit()
            cursor.close()
            connection.close()

            id_admin = session['id_admin']
            action = f"Added: {nama}"
            log_activity(id_admin, action)
            flash('Data admin berhasil ditambahkan!', 'success')
            return redirect(url_for('data_user'))
        else:
            return render_template('admin/tambah-admin.html')
    else:
        return redirect('/')
    
@app.route('/admin/detail/<int:id>', methods=['GET'])
def detail_admin(id):  
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM admin WHERE id_admin = %s', (id,))
    admin = cursor.fetchone()
    if not admin:
        return 'Admin not found', 404
    return render_template('admin/detail-admin.html', admin=admin)
    
@app.route('/admin/edit/<int:id>', methods=['GET', 'POST'])
def edit_admin(id):
    if 'id_admin' in session:
        if request.method == 'POST':
            nip = request.form['nip']
            nama = request.form['nama']
            email = request.form['email']
            password = request.form['password']
            kontak = request.form['kontak']
            alamat = request.form['alamat']
            gambar = None

            if 'gambar' in request.files:
                file = request.files['gambar']
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(file_path)
                    gambar = file_path
                    gambar = file_path.replace('\\', '/')

            if not gambar and 'gambarLama' in request.form:
                gambar = request.form['gambarLama'].replace('\\', '/')
            else:
                gambar = get_default_image()

            connection = create_connection()
            cursor = connection.cursor()

            cursor.execute("""
                UPDATE admin
                SET nip = %s,  nama = %s, email = %s, password = %s, kontak = %s, alamat = %s, gambar = %s
                WHERE id_admin = %s
            """, (nip, nama, email, password, kontak, alamat, gambar, id))

            connection.commit()
            cursor.close()
            connection.close()

            id_admin = session['id_admin']
            action = f"Editted: {nama}"
            log_activity(id_admin, action)
            flash('Data admin berhasil diubah!', 'success')
            return redirect(url_for('data_user'))
        else:
            connection = create_connection()
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM admin WHERE id_admin = %s", (id,))
            data_admin = cursor.fetchone()
            cursor.close()
            connection.close()

            if data_admin and data_admin['gambar']:
                data_admin['gambar'] = data_admin['gambar'].replace('\\', '/')


            return render_template('admin/edit-admin.html', admin=data_admin)
    else:
        return redirect('/')

@app.route('/admin/delete/<int:id>', methods=['GET'])
def delete_admin(id):
    if 'id_admin' in session:
        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute('SELECT nama FROM admin WHERE id_admin = %s', (id,))
        admin = cursor.fetchone()
        if admin:
            nama = admin['nama']

            cursor.execute('DELETE FROM admin WHERE id_admin = %s', (id,))
            connection.commit()
            cursor.close()
            connection.close()

            id_admin = session['id_admin']
            action = f"Deleted: {nama}"
            log_activity(id_admin, action)

            flash('Data admin berhasil dihapus!', 'success')
            return redirect(url_for('data_user'))
    else:
        return redirect('/')
    
#Nilai

@app.route('/nilai', methods=['GET'])
def data_nilai():
    if 'id_admin' in session:
        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute('''
        SELECT nilai.id_nilai, siswa.nama, nilai.x1, nilai.x2, nilai.x3, nilai.x4, nilai.x5, nilai.x6, nilai.x7, nilai.x8, nilai.x9, nilai.x10
        FROM nilai
        JOIN siswa ON nilai.id_siswa = siswa.id_siswa
        ''')
        data_nilai = cursor.fetchall()

        cursor.close()
        connection.close()

        return render_template('nilai/data-nilai.html', nilai=data_nilai)
    else:
        return redirect('/')

@app.route('/nilai/edit/<int:id>', methods=('GET', 'POST'))
def edit_nilai(id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM nilai WHERE id_nilai = %s', (id,))
    nilai = cursor.fetchone()

    cursor.execute('SELECT nama FROM siswa WHERE id_siswa = %s', (nilai['id_siswa'],))
    siswa = cursor.fetchone()
    if siswa:
        nama = siswa['nama']
    else:
        nama = None

    if request.method == 'POST':
        x1 = request.form.get('x1')
        x2 = request.form.get('x2')
        x3 = request.form.get('x3')
        x4 = request.form.get('x4')
        x5 = request.form.get('x5')
        x6 = request.form.get('x6')
        x7 = request.form.get('x7')
        x8 = request.form.get('x8')
        x9 = request.form.get('x9')
        x10 = request.form.get('x10')

        x1 = x1 if x1 else 0
        x2 = x2 if x2 else 0
        x3 = x3 if x3 else 0
        x4 = x4 if x4 else 0
        x5 = x5 if x5 else 0
        x6 = x6 if x6 else 0
        x7 = x7 if x7 else 0
        x8 = x8 if x8 else 0
        x9 = x9 if x9 else 0
        x10 = x10 if x10 else 0

        cursor.execute('UPDATE nilai SET x1 = %s, x2 = %s, x3 = %s, x4 = %s, x5 = %s, x6 = %s, x7 = %s, x8 = %s, x9 = %s, x10 = %s WHERE id_nilai = %s', (x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, id))
        connection.commit()
        connection.close()

        id_admin = session['id_admin']
        action = f"Editted Nilai: {nama}"
        log_activity(id_admin, action)

        return redirect(url_for('data_nilai'))

    cursor.execute('SELECT * FROM siswa')
    siswa = cursor.fetchall()
    connection.close()

    return render_template('/nilai/edit-nilai.html', nilai=nilai, siswa=siswa)
    

#Prodi

@app.route('/prodi', methods=['GET'])
def data_prodi():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute('SELECT id_prodi, nama, kode, link, gambar FROM prodi ORDER BY id_prodi DESC')
    data_prodi = cursor.fetchall()
    cursor.close()

    connection.close()

    return render_template('/prodi/data-prodi.html', prodi=data_prodi)

@app.route('/prodi/tambah', methods=['GET', 'POST'])
def tambah_prodi():
    if request.method == 'POST':
        nama = request.form['nama']
        kode = request.form['kode']
        link = request.form['link']
        gambar = None

        if 'gambar' in request.files:
            file = request.files['gambar']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                gambar = file_path
                gambar = file_path.replace('\\', '/')


            if not gambar:
                gambar = get_default_image2()

        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute("INSERT INTO prodi (nama, kode, link, gambar) VALUES (%s, %s, %s, %s)",
                    (nama, kode, link, gambar))
        connection.commit()
        cursor.close()
        connection.close()

        id_admin = session['id_admin']
        action = f"Added: {nama}"
        log_activity(id_admin, action)

        flash('Program Studi berhasil ditambahkan!', 'success')
        return redirect(url_for('data_prodi'))
    else:
        return render_template('prodi/tambah-prodi.html')

@app.route('/prodi/edit/<int:id>', methods=['GET', 'POST'])
def edit_prodi(id):
    if request.method == 'POST':
        nama = request.form['nama']
        kode = request.form['kode']
        link = request.form['link']
        gambar = None

        if 'gambar' in request.files:
            file = request.files['gambar']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                gambar = file_path
                gambar = file_path.replace('\\', '/')

            if not gambar and 'gambarLama' in request.form:
                gambar = request.form['gambarLama'].replace('\\', '/')
            else:
                gambar = get_default_image2()

        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE prodi
            SET nama = %s, kode = %s, link = %s, gambar = %s
            WHERE id_prodi = %s
        """, (nama, kode, link, gambar, id))
        connection.commit()
        cursor.close()
        connection.close()

        id_admin = session['id_admin']
        action = f"Editted: {nama}"
        log_activity(id_admin, action)

        flash('Program Studi berhasil diubah!', 'success')
        return redirect(url_for('data_prodi'))
    else:
        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM prodi WHERE id_prodi = %s", (id,))
        data_prodi = cursor.fetchone()
        cursor.close()
        connection.close()

        return render_template('prodi/edit-prodi.html', prodi=data_prodi)

@app.route('/prodi/delete/<int:id>', methods=['GET'])
def delete_prodi(id):
    connection = create_connection()
    cursor = connection.cursor()
    
    cursor.execute('SELECT nama FROM admin WHERE id_admin = %s', (id,))
    admin = cursor.fetchone()
    if admin:
        nama = admin['nama']

        cursor.execute('DELETE FROM prodi WHERE id_prodi = %s', (id,))
        connection.commit()
        cursor.close()
        connection.close()

        id_admin = session['id_admin']
        action = f"Deleted: {nama}"
        log_activity(id_admin, action)

        flash('Program Studi berhasil dihapus!', 'success')
        return redirect(url_for('data_prodi'))


if __name__ == '__main__':
    app.run(debug=True, port=9999)