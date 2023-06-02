from django.shortcuts import render
from django.views import generic

from board.forms import TodoForm
from board.models import TodoList
from datetime import datetime

from django.http import JsonResponse


class Todo_board(generic.TemplateView):
    # get 방식으로 받았을 때, index.html로 이동
    def get(self, request, *args, **kwargs):
        template_name = 'board/todo_list.html'
        # 기한 없는 일정, 마감 x
        todo_list_no_end_date = TodoList.objects.all() \
            .filter(end_date__isnull=True, is_complete=0) \
            .order_by('priority')
        # 기한 있고, 마감 x
        todo_list_end_date_non_complete = TodoList.objects.all() \
            .filter(end_date__isnull=False, is_complete=0) \
            .order_by('priority')
        # 마감
        todo_list_end_date_complete = TodoList.objects.all() \
            .filter(is_complete=1) \
            .order_by('end_date')
        today = datetime.now()

        # end_date가 가까움
        close_end_day = []
        # end_date가 이미 지남
        over_end_day = []

        # 기한이 있는데 마감이 안된 것들 중
        for i in todo_list_end_date_non_complete:
            e_day = str(i.end_date).split("-")
            end_day = datetime(int(e_day[0]), int(e_day[1]), int(e_day[2]))
            if (end_day - today).days < -1:
                over_end_day.append(i.title)
            if -1 <= (end_day - today).days < 3:
                close_end_day.append(i.title)

        return render(request, template_name, {"todo_list_endDate_non_complete": todo_list_end_date_non_complete,
                                               "todo_list_endDate_complete": todo_list_end_date_complete,
                                               "todo_list_no_endDate": todo_list_no_end_date,
                                               'close_end_day': close_end_day, 'over_end_day': over_end_day})


def check_post(request):
    template_name = 'board/succeed.html'

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            message = "일정을 추가하였습니다."
            todo = form.save(commit=False)
            todo.todo_save()
            return render(request, template_name, {"message": message})
    template_name = 'board/insert.html'
    form = TodoForm(initial={"is_complete": 0})
    return render(request, template_name, {"form": form})


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
        form = self.get_form(TodoForm)

        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)


class Board_delete(generic.DeleteView):
    model = TodoList
    success_url = '/board/'
    context_object_name = 'todo'


def update_complete(request):
    if request.method == 'POST':
        pk = request.POST.get('pk')
        is_complete = request.POST.get('is_complete')

        try:
            todo_item = TodoList.objects.get(no=pk)
            todo_item.is_complete = True if is_complete == 'true' else False
            todo_item.save()

            return JsonResponse({'success': True})
        except TodoList.DoesNotExist:
            return JsonResponse({'success': False, 'error': '일정을 찾을 수 없습니다.'})

    return JsonResponse({'success': False, 'error': '올바른 요청이 아닙니다.'})

