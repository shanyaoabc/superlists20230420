from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
	# render函数，Django会自动在素有应用目录中搜索名为templates的文件夹，然后根据模板的内容构建一个HttpRespouse对象
	# 使用模版有时之一把python变量带入HTML文本
	return render(request, 'home.html', {'new_item_text': request.POST.get('item_text', ''),})
