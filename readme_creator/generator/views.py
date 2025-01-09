from django.http import HttpResponse
from django.shortcuts import render
from .forms import GitHubURLForm
from .utils import fetch_github_data

def generate_readme_from_github(request):
    if request.method == "POST":
        form = GitHubURLForm(request.POST)
        if form.is_valid():
            github_url = form.cleaned_data["github_url"]
            data = fetch_github_data(github_url)

            if data:
                content = f"""# {data.get('name', 'Project Name')}

## Description
{data.get('description', 'No description provided.')}

## Topics
{', '.join(data.get('topics', [])) if data.get('topics') else 'No topics available.'}

## License
{data.get('license', {}).get('name', 'No license specified.')}
                """
                response = HttpResponse(content, content_type="text/markdown")
                response["Content-Disposition"] = 'attachment; filename="README.md"'
                return response
            else:
                return HttpResponse("Failed to fetch data from GitHub. Please check the URL.", status=400)
    else:
        form = GitHubURLForm()

    return render(request, "generator/github_form.html", {"form": form})
