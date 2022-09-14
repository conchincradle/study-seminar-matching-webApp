from django.shortcuts import render
from django.views.generic import View

from accounts.models import AccountUser
from .models import FollowRelation




class followings(View):
    def get(self, request, *args, **kwargs):
        target_user = AccountUser.objects.get(id=self.kwargs['user_id'])
        relations = FollowRelation(user=target_user)
        followings = relations.following.all()
        return render(request, "follow/followings.html", {'user': target_user, 'followings': followings})

class followers(View):
    def get(self, request, *args, **kwargs):
        target_user = AccountUser.objects.get(id=self.kwargs['user_id'])
        followers = target_user.followed_by.all()
        return render(request, "follow/followers.html", {'user': target_user, 'followers': followers})

