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
                        gap1_weighted = gap1 * weights[0] * scenario
                        gap2_weighted = gap2 * weights[1] * scenario
                        gap3_weighted = gap3 * weights[2] * scenario
                        gap4_weighted = gap4 * weights[3] * scenario
                        total = gap1_weighted + gap2_weighted + gap3_weighted + gap4_weighted
                        weighted_results.append({
                            'year': year,
                            'type': '利率敏感性缺口',
                            'gap1': round(gap1, 2),
                            'gap2': round(gap2, 2),
                            'gap3': round(gap3, 2),
                            'gap4': round(gap4, 2),
                            'total': round(gap1 + gap2 + gap3 + gap4, 2)
                        })
                        weighted_results.append({
                            'year': year,
                            'type': '净利息收入',
                            'gap1': round(gap1_weighted, 2),
                            'gap2': round(gap2_weighted, 2),
                            'gap3': round(gap3_weighted, 2),
                            'gap4': round(gap4_weighted, 2),
                            'total': round(total, 2)
                        })
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
                        total = usd + hkd + other
                        # 添加净外汇敞口行
                        results.append({
                            'year': year,
                            'type': '净外汇敞口',
                            'USD': round(usd, 2),
                            'HKD': round(hkd, 2),
                            'other': round(other, 2),
                            'total': round(total, 2)
                        })
                        # 添加外币损益行
                        results.append({
                            'year': year,
                            'type': '外币损益',
                            'USD': round(usd * scenario, 2),
                            'HKD': round(hkd * scenario, 2),
                            'other': round(other * scenario, 2),
                            'total': round(total * scenario, 2)
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
                        total = invest1 + invest2 + invest3
                        # 添加持有股票资产行
                        results.append({
                            'year': year,
                            'type': '持有股票资产',
                            'invest1': round(invest1, 2),
                            'invest2': round(invest2, 2),
                            'invest3': round(invest3, 2),
                            'total': round(total, 2)
                        })
                        # 添加经济资本行（结果乘以-1，经济资本是为了覆盖可能的损失而预留的资金，只考虑不利变动（下跌）情况，经济资本为正）
                        results.append({
                            'year': year,
                            'type': '经济资本',
                            'invest1': round(invest1 * scenario * -1, 2),
                            'invest2': round(invest2 * scenario * -1, 2),
                            'invest3': round(invest3 * scenario * -1, 2),
                            'total': round(total * scenario * -1, 2)
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
    
    # 只生成负数情景（即下跌情景）
    for value in scenario_values:
        adjusted_value = base_value * value * (-1)  # 只使用 -1
        label = f"下降{abs(adjusted_value * 100):.2f}%"
        scenarios.append({'value': adjusted_value, 'label': label})
    
    # 按照跌幅从小到大排序
    scenarios.sort(key=lambda x: abs(x['value']))
    return JsonResponse({'scenarios': scenarios})

