from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Menu
from django.core.paginator import Paginator


class IndexPageView(TemplateView):
	template_name = "index.html"


class AboutPageView(TemplateView):
	template_name = "about.html"


class ContactPageView(TemplateView):
	template_name = "contact.html"


# class GlassesPageView(ListView):
# 	model = Menu
# 	template_name = "glasses.html"


def GlassesPageView(request):
	obj = Menu.objects.all()
	page_n = request.GET.get('page',1)
	p = Paginator(obj,5)
	try:
		page = p.page(page_n)
	except Exception:
		page = p.page(1)
	context = {

		"page":page
	}

	return render(request,"glasses.html",context)














class ShopPageView(TemplateView):
	template_name = "shop.html"


# def testpageview(request):
# 	news = Menu.objects.all()
# 	context = {
# 					"news":news
# 	}

# 	return render(request,"test.html",context)
