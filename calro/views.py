from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

from .AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
from .utils import get_amaranthgroups


username = 'geogirl'
apikey = 'a9a96e78d32fd2d7449d6ec8249f70876b101f576cc488dafab971b968da65ab'

def groups_view(request):
    if 'q' in request.GET:
        q = request.GET['q']
        amaranth = get_amaranthgroups(query=q)
    else:
        amaranth = get_amaranthgroups()

    if request.method == 'POST':
        recipient = request.POST.get('recipient', '')
        message = request.POST.get('message', '')

        to = recipient
        message = message

        gateway = AfricasTalkingGateway(username, apikey)

        try:
        # Thats it, hit send and we'll take care of the rest.

            results = gateway.sendMessage(to, message)
            context = {
                'response': results
            }
            # recipient['number'], recipient['status'], recipient['messageId'], recipient['cost'])
        except (AfricasTalkingGatewayException, e):
            pass

    data = []
    for a in amaranth['data']:
        data.append(a)

    context = {
        'hivGroups': data
    }
    return render(request, 'hiv-groups.html', context)


def home(request):
    return render(request,'index.html')
