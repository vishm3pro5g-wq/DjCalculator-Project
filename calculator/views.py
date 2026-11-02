from django.views.generic import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from json import loads

@method_decorator(csrf_exempt, name='dispatch')
class AdditionView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)
        n1 = form_data.get("num1")
        n2 = form_data.get("num2")
        result = n1+n2

        #print(request_body)

        data = {
            "sum": result
        }

        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class SubtractionView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)
        n1 = form_data.get("num1")
        n2 = form_data.get("num2")
        result = n1-n2
        return JsonResponse(
            {"message":"subtraction API is working!",
            "differnce":result}
        )

@method_decorator(csrf_exempt, name='dispatch')
class MultiplicationView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)
        n1 = form_data.get("num1")
        n2 = form_data.get("num2")
        result = n1*n2
        return JsonResponse(
            {"message":"multiplication API is working!",
            "product":result}
        )

@method_decorator(csrf_exempt, name='dispatch')
class DivisionView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)
        n1 = form_data.get("num1")
        n2 = form_data.get("num2")
        result = n1/n2
        return JsonResponse(
            {"message":"division API is working!",
            "Quotient":result}
        )

@method_decorator(csrf_exempt, name='dispatch')
class ModulusView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)
        n1 = form_data.get("num1")
        n2 = form_data.get("num2")
        result = n1%n2
        return JsonResponse(
            {"message":"modulus API is working!",
            "Reminder":result}
        )

@method_decorator(csrf_exempt, name='dispatch')
class BmiView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)
        h = form_data.get("height")
        w = form_data.get("weight")
        bmi = w/(h**2)

        result={
            "height":h,
            "weight":w,
            "BMI":bmi
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt, name='dispatch')
class AgeView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)
        b = form_data.get("birth_year")
        c = form_data.get("current_year")
        age=c-b

        result={
            "Age":age
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt, name='dispatch')
class PercentageView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)
        obtained_mark = form_data.get("obtained_mark")
        total_mark = form_data.get("total_mark")
        percentage = obtained_mark / total_mark*100

        return JsonResponse(
            {
                "percentage" : percentage
            }
        )

@method_decorator(csrf_exempt, name='dispatch')
class AreaView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)
        length = form_data.get("length")
        breadth = form_data.get("bredth")

        area = length*breadth

        return JsonResponse(
            {
                "Area":area
            }
        )

@method_decorator(csrf_exempt, name='dispatch')
class SimpleinterestView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)
        p = form_data.get("principal")
        r = form_data.get("rate")
        t = form_data.get("time")

        simple_interest = (p*r*t)/100
        return JsonResponse(
            {
                "Simpleinterst":simple_interest
            }
        )

@method_decorator(csrf_exempt, name='dispatch')
class ElectricityBillView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)
        units = form_data.get("units")
        rate = form_data.get("rate")
        bill = unit*rate
        return JsonResponse({
            "Bill":bill
        })

@method_decorator(csrf_exempt, name='dispatch')
class DiscountCalculatorView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)
        price = form_data.get("price")
        discount_percentage = form_data.get("discount")