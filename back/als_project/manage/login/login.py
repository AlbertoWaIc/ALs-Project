"""
ログイン関係の処理を記載
・メールアドレスの照合
・パスワードの照合
・ログイン処理（ログ取得）
"""
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def test_login(requests):
    # テスト
    print("test_login")
    print(requests)
    param = json.loads(requests.body)
    print(param)
    mail = param.get('mail', '')
    print(mail)
    context = {}
    context = {"error": mail}
    return JsonResponse(context, safe=False)
