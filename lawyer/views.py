
from django.shortcuts import render, redirect
from .forms import LawyerRegistrationForm

def register_view(request):
    if request.method == 'POST':
        form = LawyerRegistrationForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                # Redirect to a success page or the desired URL
                return redirect('success_page')  # Replace 'success_page' with your actual URL pattern name
        except Exception as e:
            print(f"Error during form submission: {e}")
            # Optionally, you can log the error or handle it in another way

    else:
        form = LawyerRegistrationForm()

    return render(request, 'register.html', {'form': form})

    

