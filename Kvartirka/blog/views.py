import json

from django.shortcuts import render

from blog.models import Comments, Article


def instert_article(request):
    if request.method == "POST":
        print(json.loads(request.body)['content'])
        article = Article()
        article.content = json.loads(request.body)['content']
        article.save()


def instert_comments(request):
    if request.method == "POST":
        print(json.loads(request.body)['pk'])
        pk = json.loads(request.body)['pk']
        text = json.loads(request.body)['text']
        article = Article.objects.get(pk=pk)
        comments = Comments()
        comments.text = text
        comments.article = article
        comments.save()


def repost(request):
    if request.method == "POST":
        print(json.loads(request.body)['parent'])
        parent = json.loads(request.body)['parent']
        text = json.loads(request.body)['text']
        parent = Comments.objects.get(pk=parent)
        comments = Comments()
        comments.text = text
        comments.parent = parent
        comments.save()


def get_all_sub_comments(request):
    if request.method == "POST":
        pk = json.loads(request.body)['pk']
        comments = Comments.objects.get(pk=pk)
        print(get_all_levels(comments))


def get_all_levels(tree, level=0):
    if level > 50:
        return []
    return [json.dumps({"id": tree.id, "text": tree.text})] + [get_all_levels(x, level + 1) for x in tree.comments_set.all()]


def get_3_levels(tree, level=0):
    if level > 2:
        return []
    return ([] if level == 0 else [json.dumps({"id": tree.id, "text": tree.text})]) + [get_all_levels(x, level + 1) for x in tree.comments_set.all()]


def get_article_comments(request):
    if request.method == "POST":
        pk = json.loads(request.body)['pk']
        article = Article.objects.get(pk=pk)
        print(get_3_levels(article))
