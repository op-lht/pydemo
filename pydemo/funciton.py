# from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def count(request):
    # print("统计的字数:", len(request.GET['area1']))
    user_text = request.GET['area1']
    # 文字的总字数
    total_count = len(user_text)
    # 统计文本中出现字数最多的字
    word_dict = {}
    for word in user_text:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

    # 排序排列数据
    sort_dict = sorted(word_dict.items(), key=lambda w: w[1], reverse=True)
    # 要返回给页面显示的数据
    data = {
        'text': user_text,
        'count': total_count,
        'word_dict': word_dict,
        'sorted': sort_dict,
    }
    return render(request, 'count.html', data)


def about(request):
    return render(request, 'about.html')
