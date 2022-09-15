from django.shortcuts import render
from django.views.generic import View

from accounts.models import AccountUser
from .models import FollowRelation




class followings(View):
    def get(self, request, *args, **kwargs):
        print("_____________________")
        print(self.kwargs['user_id'])
        target_user = AccountUser.objects.get(id=self.kwargs['user_id'])
        print(target_user.user_name)
        relations = FollowRelation(user=target_user)
        followings = relations.following.all()
        return render(request, "follow/followings.html", {'target_user': target_user, 'followings': followings})
    def post(self,request,pk,*args,**kwargs):
        return render(request,)



class followers(View):
    def get(self, request, *args, **kwargs):
        target_user = AccountUser.objects.get(id=self.kwargs['user_id'])
        followers = target_user.followed_by.all()
        tmp = followers
        followers = []
        for follower in tmp:
            followers.append(AccountUser.objects.get(id=follower.user.id))


        return render(request, "follow/followers.html", {'target_user': target_user, 'followers': followers})

