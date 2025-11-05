# PBIXRay Flask Application

A secure, localhost-based web application for analyzing Power BI (.pbix) and Excel (.xlsx) files with PowerPivot models.

## Features

- **Secure Local Hosting**: Runs entirely on localhost (127.0.0.1:5000) - no data is sent to external servers
- **File Upload & Analysis**: Upload PBIX or XLSX files for comprehensive analysis
- **Model Metadata**: View Power BI configuration and model information
- **Size Metrics**: Display human-readable model sizes and table counts
- **Schema Viewer**: Explore data model schema with table and column types
- **Statistics**: Detailed column statistics (cardinality, dictionary size, hash index, data size)
- **Relationships**: Visualize table relationships
- **Power Query Code**: View M/Power Query expressions
- **M Parameters**: Display parameter values with modification timestamps
- **DAX Objects**: View calculated tables, measures, and columns
- **Table Preview**: Un-VertiPaq functionality to preview actual table data

## Security

This application is designed with security in mind:

- Runs only on localhost (127.0.0.1)
- Files are processed locally on your machine
- No external network requests
- Temporary file storage with automatic cleanup
- Session-based file management

## Installation

1. Ensure you have Python 3.8 or higher installed

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Linux/Mac

```bash
./run_app.sh
```

Or manually:
```bash
python3 app.py
```

### Windows

Double-click `run_app.bat` or run:
```cmd
python app.py
```

## Usage

1. Start the application using one of the methods above
2. Open your web browser and navigate to `http://127.0.0.1:5000`
3. Upload a PBIX or XLSX file
4. View the comprehensive analysis results
5. Use the "Un-VertiPaq" feature to preview table data
6. Click "Analyze Another File" to process additional files

## File Structure

```
pbixray_local/
├── app.py                 # Main Flask application
├── templates/             # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Upload page
│   ├── results.html      # Analysis results page
│   ├── table_preview.html # Table data preview page
│   └── error.html        # Error page
├── static/               # Static assets
│   └── style.css         # CSS styling
├── run_app.sh           # Linux/Mac launcher script
├── run_app.bat          # Windows launcher script
└── requirements.txt     # Python dependencies
```

## Dependencies

- Flask: Web framework
- PBIXRay: Core analysis engine
- pandas: Data manipulation
- kaitaistruct: Binary data parsing
- apsw: SQLite wrapper
- xpress9: Data decompression

## Troubleshooting

### Port Already in Use

If port 5000 is already in use, you can change it in `app.py`:

```python
app.run(host='127.0.0.1', port=5001, debug=True)  # Change to any available port
```

### File Upload Fails

- Ensure the file is a valid PBIX or XLSX file
- Check that the file size is under 500MB (configurable in `app.py`)
- Verify you have write permissions in your temp directory

### Dependencies Not Found

Run:
```bash
pip install -r requirements.txt --upgrade
```

## Comparison with Streamlit Version

The Flask version offers several advantages:

- **More Control**: Full control over HTML/CSS/JavaScript
- **Better Security**: Explicit localhost-only binding
- **Lighter Weight**: No need for Streamlit's additional features
- **Standard Web Interface**: Works with any modern browser
- **Easier Deployment**: Simple Python app with no special requirements

## Development

To run in development mode with auto-reload:

```python
app.run(host='127.0.0.1', port=5000, debug=True)
```

## License

MIT License - Same as PBIXRay core package

## Support

For issues or questions, please refer to the main PBIXRay repository.
