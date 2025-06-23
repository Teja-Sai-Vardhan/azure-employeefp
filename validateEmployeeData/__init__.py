import azure.functions as func
import csv
import io

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        file_bytes = req.get_body()
        file_stream = io.StringIO(file_bytes.decode('utf-8'))
        reader = csv.DictReader(file_stream)
        for row in reader:
            if not row.get('EmployeeID') or not row.get('Name'):
                return func.HttpResponse("Invalid Data", status_code=400)
        return func.HttpResponse("Validation Passed", status_code=200)
    except Exception as e:
        return func.HttpResponse("Invalid Data", status_code=400)