from django.views.generic import ListView
from .models import Parcel
from django.views.generic import View
from django.http import JsonResponse


class CrudView(ListView):
    model = Parcel
    template_name = 'pages/parcels.html'
    context_object_name = 'parcels'
    paginate_by = 2

    def get_queryset(self, *args, **kwargs):
        return Parcel.objects.filter(order=self.request.user).order_by('-id')


class CreateCrudParcel(View):

    def post(self, request):
        try:
            user_order = request.user
            recipient1 = request.POST.get('recipient', None)
            track1 = request.POST.get('treck', None)
            parcels_name1 = request.POST.get('parcels_name', None)
            price1 = request.POST.get('price', None)
            item_name1 = request.POST.get('item_name', None)
            country1 = request.POST.get('country', None)
            web_site1 = request.POST.get('web_site', None)
            comments1 = request.POST.get('comment', None)
            amount1 = request.POST.get('amount', None)
            weight1 = request.POST.get('weight', None)

            obj = Parcel.objects.create(
                order=user_order,
                treck=track1,
                recipient=recipient1,
                parcels_name=parcels_name1,
                price=price1,
                category=item_name1,
                country=country1,
                web_site=web_site1,
                comment=comments1,
                amount=amount1,
                weight=weight1,
            )

            user = {'id': obj.id, 'treck': obj.treck, 'recipient': obj.recipient,
                    'parcels_name': obj.parcels_name, 'price': obj.price,
                    'category': obj.category, 'country': obj.country, 'web_site': obj.web_site,
                    'comment': obj.comment, 'amount': obj.amount, 'weight': obj.weight }
            data = {
                'user': user
            }
            return JsonResponse(data)

        except:
            pass


class DeleteParcel(View):

    def post(self, request):
        id1 = request.POST.get('id', None)
        Parcel.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }

        return JsonResponse(data)


class UpdateParcel(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        track1 = request.POST.get('treck', None)
        parcels_name1 = request.POST.get('parcels_name', None)
        item_name1 = request.POST.get('item_name', None)
        country1 = request.POST.get('country', None)
        web_site1 = request.POST.get('web_site', None)
        comment1 = request.POST.get('comments', None)


        obj = Parcel.objects.get(id=id1)
        obj.treck = track1
        obj.parcels_name = parcels_name1
        obj.category = item_name1
        obj.country = country1
        obj.web_site = web_site1
        obj.comment = comment1
        obj.save()

        user = {'id': obj.id, 'treck': obj.treck, 'parcels_name': obj.parcels_name,
                'category': obj.category, 'country': obj.country, 'web_site': obj.web_site,
                'comment': obj.comment,}

        data = {
            'user': user
        }
        return JsonResponse(data)
