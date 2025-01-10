from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .forms import GitHubURLForm
from .utils import fetch_github_data

def generate_readme_from_github(request):
    if request.method == "POST":
        form = GitHubURLForm(request.POST)
        if form.is_valid():
            github_url = form.cleaned_data["github_url"]
            data = fetch_github_data(github_url)

            if data and isinstance(data, dict): 
                content = f"""# {data.get('repository_name', 'Project Name')}

## Description
{data.get('description', 'No description provided.')}

## Topics
{', '.join(data.get('topics') or ['No topics available.'])}

## License
{data.get('license', 'No license specified.')}
"""
                response = HttpResponse(content, content_type="text/markdown")
                response["Content-Disposition"] = 'attachment; filename="README.md"'
                return response

            return HttpResponse("Failed to fetch data from GitHub. Please check the URL or try again later.", status=400)
    else:
        form = GitHubURLForm()
    return render(request, "github_forms.html", {"form": form})
