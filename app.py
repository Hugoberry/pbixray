from flask import Flask, render_template, request, redirect, url_for, session
from pbixray.core import PBIXRay
import os
from werkzeug.utils import secure_filename
import tempfile
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # For session management
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500MB max file size
app.config['UPLOAD_FOLDER'] = tempfile.gettempdir()

ALLOWED_EXTENSIONS = {'pbix', 'xlsx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def sizeof_fmt(num, suffix="B"):
    """Convert bytes to human-readable format"""
    for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"

@app.route('/')
def index():
    """Main upload page"""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload and analysis"""
    if 'file' not in request.files:
        return redirect(url_for('index'))

    file = request.files['file']

    if file.filename == '':
        return redirect(url_for('index'))

    if file and allowed_file(file.filename):
        # Save the uploaded file temporarily
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        try:
            # Analyze the file with PBIXRay
            model = PBIXRay(filepath)

            # Prepare data for display
            results = {
                'filename': filename,
                'metadata': model.metadata,
                'size': sizeof_fmt(model.size),
                'size_bytes': model.size,
                'table_count': len(model.tables) if hasattr(model.tables, '__len__') else model.tables.size,
                'tables': model.tables.tolist() if hasattr(model.tables, 'tolist') else list(model.tables),
                'schema': model.schema.to_dict('records') if hasattr(model.schema, 'to_dict') else [],
                'statistics': model.statistics.to_dict('records') if hasattr(model.statistics, 'to_dict') else [],
                'relationships': model.relationships.to_dict('records') if model.relationships.size else [],
                'power_query': model.power_query.to_dict('records') if model.power_query.size else [],
                'm_parameters': model.m_parameters.to_dict('records') if model.m_parameters.size else [],
                'dax_tables': model.dax_tables.to_dict('records') if model.dax_tables.size else [],
                'dax_measures': model.dax_measures.to_dict('records') if model.dax_measures.size else [],
                'dax_columns': model.dax_columns.to_dict('records') if model.dax_columns.size else [],
            }

            # Store filepath in session for table preview
            session['current_file'] = filepath

            return render_template('results.html', results=results)

        except Exception as e:
            # Clean up the file
            if os.path.exists(filepath):
                os.remove(filepath)
            return render_template('error.html', error=str(e))

    return redirect(url_for('index'))

@app.route('/preview_table', methods=['POST'])
def preview_table():
    """Preview table data (Un-VertiPaq)"""
    table_name = request.form.get('table_name')
    filepath = session.get('current_file')

    if not filepath or not os.path.exists(filepath):
        return render_template('error.html', error='File not found. Please upload again.')

    try:
        model = PBIXRay(filepath)
        table_data = model.get_table(table_name)

        # Convert to dict for display
        table_dict = table_data.to_dict('records') if hasattr(table_data, 'to_dict') else []
        columns = list(table_data.columns) if hasattr(table_data, 'columns') else []

        return render_template('table_preview.html',
                             table_name=table_name,
                             table_data=table_dict,
                             columns=columns)
    except Exception as e:
        return render_template('error.html', error=str(e))

@app.route('/clear')
def clear():
    """Clear session and uploaded files"""
    filepath = session.get('current_file')
    if filepath and os.path.exists(filepath):
        try:
            os.remove(filepath)
        except:
            pass
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Run on localhost only for security
    app.run(host='127.0.0.1', port=5000, debug=True)
