from django.shortcuts import render

# テスト用
def follow_user(request):
    data = {'success':0}
    return render(request,'follow/follow_user.html',{'data':data})

