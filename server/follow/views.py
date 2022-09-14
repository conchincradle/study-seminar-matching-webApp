from django.shortcuts import render

##### テスト用 ####
test_data = {
    'test_arr': range(6),
}

def following(request):
    data = {'success':0}
    return render(request,'follow/following.html', test_data)

def followers(request):
    data = {'success':0}
    return render(request,'follow/followers.html', test_data)
#### テスト用 ここまで ####
