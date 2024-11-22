from django.http import JsonResponse
from django.db import connections
import json

# Create your views here.

def get_companies_from_db(query_string, table_name):
    with connections['stress_testing'].cursor() as cursor:
        sql = f"SELECT DISTINCT `company` FROM `{table_name}` WHERE LOWER(`company`) LIKE %s"
        cursor.execute(sql, ['%' + query_string.lower() + '%'])
        result = cursor.fetchall()
        return [row[0] for row in result]

def interest_rate_risk_search(request):
    query_string = request.GET.get('company', '')
    companies = get_companies_from_db(query_string, 'interest_rate_risk')
    if not companies:
        return JsonResponse({"message": "公司名称不存在"}, status=404)
    return JsonResponse(companies, safe=False)

def interest_rate_risk_test(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            if data and 'company' in data and 'scenario' in data:
                company_name = data['company']
                scenario = data['scenario']
                with connections['stress_testing'].cursor() as cursor:
                    sql = """
                    SELECT `year`, `gap1`, `gap2`, `gap3`, `gap4`
                    FROM `interest_rate_risk`
                    WHERE `company` = %s
                    """
                    cursor.execute(sql, [company_name])
                    result = cursor.fetchall()
                    weights = [0.125, 0.625, 3, 6]
                    weighted_results = []
                    for row in result:
                        year, gap1, gap2, gap3, gap4 = row
                        weighted_sum = (gap1 * weights[0] + gap2 * weights[1] + gap3 * weights[2] + gap4 * weights[3]) * scenario
                        weighted_results.append({'year': year, 'weighted_sum': weighted_sum})
                    return JsonResponse(weighted_results, safe=False)
            else:
                return JsonResponse({"message": "测试出现问题"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def currency_risk_search(request):
    query_string = request.GET.get('company', '')
    companies = get_companies_from_db(query_string, 'currency_risk')
    if not companies:
        return JsonResponse({"message": "公司名称不存在"}, status=404)
    return JsonResponse(companies, safe=False)

def currency_risk_test(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            if data and 'company' in data and 'scenario' in data:
                company_name = data['company']
                scenario = data['scenario']
                with connections['stress_testing'].cursor() as cursor:
                    sql = """
                    SELECT `year`, `USD`, `HKD`, `other`
                    FROM `currency_risk`
                    WHERE `company` = %s
                    """
                    cursor.execute(sql, [company_name])
                    result = cursor.fetchall()
                    results = []
                    for row in result:
                        year, usd, hkd, other = row
                        results.append({
                            'year': year,
                            'weighted_sum': (usd + hkd + other) * scenario
                        })
                    return JsonResponse(results, safe=False)
            else:
                return JsonResponse({"message": "测试出现问题"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def stock_price_risk_search(request):
    query_string = request.GET.get('company', '')
    companies = get_companies_from_db(query_string, 'stock_price_risk')
    if not companies:
        return JsonResponse({"message": "公司名称不存在"}, status=404)
    return JsonResponse(companies, safe=False)

def stock_price_risk_test(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            if data and 'company' in data and 'scenario' in data:
                company_name = data['company']
                scenario = data['scenario']
                with connections['stress_testing'].cursor() as cursor:
                    sql = """
                    SELECT `year`, `invest1`, `invest2`, `invest3`
                    FROM `stock_price_risk`
                    WHERE `company` = %s
                    """
                    cursor.execute(sql, [company_name])
                    result = cursor.fetchall()
                    results = []
                    for row in result:
                        year, invest1, invest2, invest3 = row
                        results.append({
                            'year': year,
                            'weighted_sum': (invest1 + invest2 + invest3) * scenario
                        })
                    return JsonResponse(results, safe=False)
            else:
                return JsonResponse({"message": "测试出现问题"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def smart_interest_rate_risk(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            if isinstance(data, dict) and 'scenarios' in data:
                scenarios = data['scenarios']
                Shibor = 0.001
                improve = Shibor * 2.58
                for scenario in scenarios:
                    if scenario['value'] > 0:
                        scenario['value'] += improve
                    else:
                        scenario['value'] -= improve
                    scenario['label'] = f"{'上升' if scenario['value'] > 0 else '下降'}{abs(scenario['value'] * 100):.2f}%"
                return JsonResponse({'scenarios': scenarios})
            else:
                return JsonResponse({"message": "情景未正确传到后端"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def smart_currency_risk(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            if isinstance(data, dict) and 'scenarios' in data:
                scenarios = data['scenarios']
                p = 0.034
                improve = p * 2.58
                for scenario in scenarios:
                    if scenario['value'] > 0:
                        scenario['value'] += improve
                    else:
                        scenario['value'] -= improve
                    scenario['label'] = f"{'外币升值' if scenario['value'] > 0 else '外币贬值'}{abs(scenario['value'] * 100):.2f}%"
                return JsonResponse({'scenarios': scenarios})
            else:
                return JsonResponse({"message": "情景未正确传到后端"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def smart_stock_price_risk(request):
    p = 0.0953
    base_value = p * 2.58
    scenario_values = [0.75, 1.0, 1.25]
    scenarios = []
    for value in scenario_values:
        for sign in [1, -1]:
            adjusted_value = base_value * value * sign
            label = f"{'上升' if sign > 0 else '下降'}{abs(adjusted_value * 100):.2f}%"
            scenarios.append({'value': adjusted_value, 'label': label})
    scenarios.sort(key=lambda x: (x['value'] < 0, abs(x['value'])))
    return JsonResponse({'scenarios': scenarios})

