import json
import os

def handler(request, response):
    # Enable CORS for all origins
    response.headers["Access-Control-Allow-Origin"] = "*"

    # Path to JSON file containing marks data
    file_path = os.path.join(os.path.dirname(__file__), "..", "q-vercel-python.json")

    # Load marks data once (optional optimization: load outside handler if possible)
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Get all 'name' query parameters as a list
    names = request.query.getlist("name") if hasattr(request.query, "getlist") else []
    
    # Map names to marks, return None if not found
    result = {"marks": [data.get(name, None) for name in names]}

    # Send JSON response with status 200
    response.status_code = 200
    return response.json(result)
