from flask import Flask, Response
import openpyxl
from io import BytesIO

app = Flask(__name__)

# Sample list of members
members = [
    {"id": 1, "name": "John Doe", "email": "johndoe@example.com"},
    {"id": 2, "name": "Jane Smith", "email": "janesmith@example.com"},
    {"id": 3, "name": "Sam Johnson", "email": "samjohnson@example.com"},
]

# Endpoint to generate Excel file
@app.route('/download-excel')
def download_excel():
    # Create a new workbook and worksheet
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Members List"

    # Set headers for the columns
    headers = ["ID", "Name", "Email"]
    ws.append(headers)

    # Add member data to the sheet
    for member in members:
        ws.append([member["id"], member["name"], member["email"]])

    # Save the workbook to a BytesIO buffer
    buffer = BytesIO()
    wb.save(buffer)
    buffer.seek(0)

    # Return the Excel file as a response with appropriate headers
    return Response(
        buffer,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        headers={"Content-Disposition": "attachment; filename=members_list.xlsx"}
    )

# Run the Flask app
if __name__ == '__main__':
    app.run(port=3000)
