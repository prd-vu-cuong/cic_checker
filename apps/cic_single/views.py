from django.shortcuts import render
from django.http import HttpResponse
import openpyxl
from django.template import loader

# Create your views here.
from apps.cic_single.services.single import SingleService


def home(request):
    return render(
        request,
        "cic_single/index.html",
        context=SingleService().get_init_data(),
    )


def import_data(request):
    file_imports = request.FILES
    excel_file = file_imports.get("excel_file")

    wb = openpyxl.load_workbook(excel_file)
    work_sheet = wb["Sheet1"]
    response = list()
    for row in work_sheet.iter_rows():
        row_data = list()
        for cell in row:
            row_data.append(str(cell.value))
        response.append(row_data)

    template = loader.get_template("cic_single/_import.html")
    data = {"excel_data": response}
    return HttpResponse(
        template.render(data, request),
        content_type="text/html",
    )


def customer(request):
    return HttpResponse("customer")
