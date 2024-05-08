from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render,redirect
from.models import UploadedMedia


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
    


@login_required(login_url="/login/")
def upload_material(request):
    if request.method == 'POST':
        # Get the form data from POST request
        product_name = request.POST.get('product_name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        vendor = request.POST.get('vendor')
        tagline = request.POST.get('tagline')
        length = request.POST.get('length')
        height = request.POST.get('height')
        breadth = request.POST.get('breadth')
        media_file = request.FILES.get('media_file')

        # Process the form data here
        if product_name and description and media_file:
            # Save the file to the desired location
            with open('media/' + media_file.name, 'wb+') as destination:
                for chunk in media_file.chunks():
                    destination.write(chunk)

            media = UploadedMedia(
                user=request.user,
                product_name=product_name,
                description=description,
                price=price,
                vendor=vendor,
                tagline=tagline,
                length=length,
                height=height,
                breadth=breadth,
                media_file=media_file
            )
            media.save()
            # Redirect the user back to the media_upload.html page
            return redirect('media_upload.html')
        else:
            return HttpResponse("Form data incomplete. Please fill in all fields.")

    return HttpResponse("GET request received.")


@login_required(login_url="/login/")
def fetch_uploaded(request):
    media_list = UploadedMedia.objects.filter(user=request.user).order_by('-uploaded_at')
    return render(request, 'home/fetch_uploaded.html', {'media_list': media_list})