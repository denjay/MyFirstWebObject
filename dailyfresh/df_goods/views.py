from django.shortcuts import render
from .models import GoodsInfo, TypeInfo
from django.core.paginator import Paginator


def index(request):
    typelist = TypeInfo.objects.all()
    type0_last = typelist[0].goodsinfo_set.order_by('-id')[0:4]
    type0_hot = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]
    type1_last = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    type1_hot = typelist[1].goodsinfo_set.order_by('-gclick')[0:4]
    type2_last = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    type2_hot = typelist[2].goodsinfo_set.order_by('-gclick')[0:4]
    type3_last = typelist[3].goodsinfo_set.order_by('-id')[0:4]
    type3_hot = typelist[3].goodsinfo_set.order_by('-gclick')[0:4]
    type4_last = typelist[4].goodsinfo_set.order_by('-id')[0:4]
    type4_hot = typelist[4].goodsinfo_set.order_by('-gclick')[0:4]
    type5_last = typelist[5].goodsinfo_set.order_by('-id')[0:4]
    type5_hot = typelist[5].goodsinfo_set.order_by('-gclick')[0:4]
    title = '首页'
    context = locals()
    return render(request, 'df_goods/index.html', context=context)


def detail(request, id):
    item = GoodsInfo.objects.get(id=id)
    item.gclick = item.gclick + 1
    context = {"item": item, "title": '商品详情'}
    return render(request, 'df_goods/detail.html', context=context)


def goods_list(request, id, page):
    all_goods = TypeInfo.objects.get(id=id).goodsinfo_set.order_by('-id')
    page_range = Paginator(all_goods, 15).page_range
    goods = Paginator(all_goods, 15).page(page)
    context = {"goods": goods, "page_range": page_range, "id": id, "title": '商品列表'}
    return render(request, 'df_goods/list.html', context=context)
