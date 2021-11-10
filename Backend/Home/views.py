from django.http import HttpResponse
from django.shortcuts import render, redirect
from store.models import Product
from Account.models import Notification, NotificationCount, Updates, Testimony, LookingFor
import random
# Create your views here.


def index(request):
    subscribed = False
    notifs = []
    newNotif = None
    allproducts = []
    lookforpros = []
    if request.user.is_authenticated:
        try:
            subscribed = Updates.objects.get(user=request.user)
        except:
            pass
        notifc = NotificationCount.objects.get_or_create(user=request.user)[0]
        newNotif = not notifc.seen
        notifc = NotificationCount.objects.get_or_create(user=request.user)[0]
        notifications = Notification.objects.all()[::-1]
        notifs = list()
        for n in notifications:
            if n.user != request.user:
                if n.comment.reply:
                    if n.comment.reply.user == request.user:
                        notifs.append(n)
                        continue
                if n.post.user == request.user:
                    notifs.append(n)

        lf = LookingFor.objects.filter(user=request.user)
        try:
            u = Updates.objects.get(user=request.user)
            allpros = Product.objects.all()[::-1]
            for p in allpros:
                if p.timestamp:
                    if u.timestamp < p.timestamp:
                        if p.user != request.user:
                            allproducts.append(p)
        except:
            print("Unsubscribed")

        try:
            allpros = Product.objects.all()[::-1]
            if lf:
                for p in allpros:
                    if p.timestamp:
                        for l in lf:
                            if l.timestamp < p.timestamp:
                                if p.user != request.user and p.name.__contains__(l.product):
                                    lookforpros.append(p)
        except:
            print("Exception occured in looking for products")

    products = Product.objects.all()[::-1][:10]
    featuredProducts = Product.objects.all()
    negotiableProducts = Product.objects.filter(negotiation=True, urgent=True)
    randomFeaturedProducts = ([random.choice(featuredProducts)
                               for i in range(len(featuredProducts))])
    resultFeatuedProducts = []
    for item in randomFeaturedProducts:
        if not item in resultFeatuedProducts:
            resultFeatuedProducts.append(item)
    resultFeatuedProducts = resultFeatuedProducts[:len(
        resultFeatuedProducts)//4*4]
    randomNegotiableProducts = [random.choice(
        negotiableProducts) for i in range(len(negotiableProducts))]
    resultNegoitableProduct = []
    for item in randomNegotiableProducts:
        if not item in resultNegoitableProduct:
            resultNegoitableProduct.append(item)
    resultNegoitableProduct = resultNegoitableProduct[:10]
    try:
        testimonials = [random.choice(Testimony.objects.all())
                        for i in range(3)]
    except:
        testimonials = [1, 2, 3]

    context = {'products': products,
               'featuredProducts': resultFeatuedProducts,
               'negotiable': resultNegoitableProduct,
               'notifs': notifs,
               'updates': allproducts,
               'newNotif': newNotif,
               'subscribed': subscribed,
               'testimonials': testimonials,
               'lookfors': lookforpros}
    return render(request, 'home/index.html', context)
