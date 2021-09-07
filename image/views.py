from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger


# Create your views here.

@login_required
def image_upload(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_image = form.save(commit=False)
            new_image.user = request.user
            new_image.save()
            return render(request, 'image/image_upload_done.html')
    else:
        form = ImageForm()
    return render(
        request, 'image/image_upload.html', {'form': form}
    )


@login_required
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images,10)
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger :
        images = paginator.page(1)
    except EmptyPage:
        images = paginator.page(paginator.num_pages)

    return render(request, 'image/image_list.html', {'images': images})


@login_required
def image_detail(request, id):
    try:
        image = Image.objects.get(pk=id)
    except ObjectDoesNotExist:
        return render(request, 'image/image_list.html')

    return render(request, 'image/image_detail.html', {'image': image})


@login_required
def image_like(request, id):
    try:
        islike = Image.objects.get(user_like=request.user, pk=id)
    except Image.DoesNotExist:
        islike = None

    if islike == None:
        image = Image.objects.get(pk=id)
        image.user_like.add(request.user)
        return JsonResponse({'status': 'success', 'image_status': 'count-like',
                             'number': str(Image.objects.get(pk=id).user_like.count())})
    else:
        image = Image.objects.get(pk=id)
        image.user_like.remove(request.user)
        return JsonResponse(
            {'status': 'success', 'image_status': 'count', 'number': str(Image.objects.get(pk=id).user_like.count())})


@login_required
def image_dislike(request, id):
    image = Image.objects.get(pk=id)
    image.user_like.remove(request.user)
    return redirect('image:image_detail', id=id)
