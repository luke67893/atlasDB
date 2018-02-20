from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from taskDB.atlasUpload.models import Task
from taskDB.atlasUpload.forms import DocumentForm

# Create your views here.

def upload(request):
	# Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('atlasUpload.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'atlasUpload/index.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

    # return render(request, 'atlasUpload/index.html')
