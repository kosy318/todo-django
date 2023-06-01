from django.shortcuts import render
from django.views import generic

from board.forms import TodoForm
from board.models import TodoList


class Todo_board(generic.TemplateView):
    # get 방식으로 받았을 때, index.html로 이동
    def get(self, request, *args, **kwargs):
        template_name = 'board/todo_list.html'
        todo_list = TodoList.objects.all()  # 모든 객체를 가져옴
        return render(request, template_name, {"todo_list": todo_list})


class Board_detail(generic.DetailView):
    model = TodoList
    template_name = 'board/board_detail.html'
    context_object_name = 'todo'


def check_post(request):
    if request.method == 'POST':
        template_name = 'board/succeed.html'
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.todo_save()
            message = "일정을 추가하였습니다"
            return render(request, template_name, {"message": message})
    else:
        template_name = 'board/insert.html'
        form = TodoForm
        return render(request, template_name, {"form": form})
