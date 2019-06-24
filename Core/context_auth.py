from django.http import request
from .models import *


class ContextAuth():
    """class for get authorized context for logged in user"""

    def __init__(self, request):
        self.user = None
        self.personnel = None
        self.project_list = []
        self.assignment_list = []
        if request.user.is_authenticated:
            self.user = request.user
            self.personnel = UserPersonnel.objects.get(ID_User=self.user)
            self.assignment_list = ProjectAssignment.objects.all().filter(
                ID_Personnel=self.personnel)
            for asg in self.assignment_list:
                self.project_list.append(
                    Project.objects.get(ID_Project=asg.ID_Project))

    def get_context_auth(self):
        context = {}
        context['project_list'] = self.project_list
        context['personnel'] = self.personnel
        return context
