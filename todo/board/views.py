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


class Board_update(generic.UpdateView):
    model = TodoList
    fields = ('title', 'content', 'end_date')
    template_name = 'board/board_update.html'
    success_url = '/board/'

    def form_valid(self, form):
        form.save()
        return render(self.request, 'board/succeed.html', {"message": "일정을 업데이트 했습니다"})

    # 상세보기 -> 수정버튼 눌렀을 때 기존에 작성한 내용이 적용되어야함
    def get(self, request, *args, **kwargs):
        # 오브젝트를 받아와서 폼 클래스를 받아온 후 return
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)


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
