from flask import Flask, render_template

app = Flask(__name__)


# Sample cloud storage data
files = [
    {
        "name": "Project Report",
        "type": "PDF",
        "size": "2.4 MB",
        "icon": "📄"
    },
    {
        "name": "College Photos",
        "type": "JPG",
        "size": "850 KB",
        "icon": "🖼️"
    },
    {
        "name": "Presentation",
        "type": "PPTX",
        "size": "1.2 MB",
        "icon": "📊"
    },
    {
        "name": "Study Notes",
        "type": "DOCX",
        "size": "780 KB",
        "icon": "📝"
    }
]


@app.route("/")
def home():

    storage_used = 3.2
    storage_total = 10

    storage_percentage = (storage_used / storage_total) * 100

    return render_template(
        "index.html",
        files=files,
        storage_used=storage_used,
        storage_total=storage_total,
        storage_percentage=storage_percentage
    )


if __name__ == "__main__":
    app.run(debug=True)
