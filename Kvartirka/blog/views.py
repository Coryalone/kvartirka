import json

from django.http import JsonResponse
from django.shortcuts import render

from blog.models import Comments, Article


def instert_article(request):
    if request.method == "POST":
        article = Article()
        article.content = json.loads(request.body)['content']
        article.save()
        return JsonResponse({'Ответ': 'Запись добавлена'})
    else:
        return JsonResponse({'Ответ': 'Пожалуйста, используй метод POST'})


def instert_comments(request):
    if request.method == "POST":
        pk = json.loads(request.body)['pk']
        text = json.loads(request.body)['text']
        article = Article.objects.get(pk=pk)
        comments = Comments()
        comments.text = text
        comments.article = article
        comments.save()
        return JsonResponse({'Ответ': 'Комментарий добавлен'})
    else:
        return JsonResponse({'Ответ': 'Пожалуйста, используй метод POST'})


def repost(request):
    if request.method == "POST":
        parent = json.loads(request.body)['parent']
        text = json.loads(request.body)['text']
        parent = Comments.objects.get(pk=parent)
        comments = Comments()
        comments.text = text
        comments.parent = parent
        comments.save()
        return JsonResponse({'Ответ': 'Ответ на комментарий добавлен'})
    else:
        return JsonResponse({'Ответ': 'Пожалуйста, используй метод POST'})


def get_all_sub_comments(request):
    if request.method == "GET":
        pk = request.GET.get('pk')
        comments = Comments.objects.get(pk=pk)
        list_of_comments = get_all_levels(comments)
        return JsonResponse({'Ответ': list_of_comments})
    else:
        return JsonResponse({'Ответ': 'Пожалуйста, используй метод GET'})


def get_all_levels(tree, level=0):
    if level > 50:
        return []
    return [json.dumps({"id": tree.id, "text": tree.text})] + [get_all_levels(x, level + 1) for x in tree.comments_set.all()]


def get_3_levels(tree, level=0):
    if level > 2:
        return []
    return ([] if level == 0 else [json.dumps({"id": tree.id, "text": tree.text})]) + [get_all_levels(x, level + 1) for x in tree.comments_set.all()]


def get_article_comments(request):
    if request.method == "GET":
        pk = request.GET.get('pk')
        article = Article.objects.get(pk=pk)
        list_of_comments = get_3_levels(article)
        return JsonResponse({'Ответ': list_of_comments})
    else:
        return JsonResponse({'Ответ': 'Пожалуйста, используй метод GET'})
