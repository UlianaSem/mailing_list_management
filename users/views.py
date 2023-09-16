from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import CreateView

from users.forms import UserRegisterForm, UserVerificationForm
from users.models import User
from users.services import _create_verification_code, send_code


class RegisterCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    def get_success_url(self):
        return reverse('users:verification', args=[self.object.pk])

    def form_valid(self, form):
        new_user = form.save()
        new_user.code = _create_verification_code()
        new_user.save()

        send_code(new_user.pk)

        return super().form_valid(form)


def pass_verification(request, pk):
    user = User.objects.get(pk=pk)

    if request.method == 'POST':
        form = UserVerificationForm(request.POST)
        user_code = request.POST.get('code')

        if user.code == user_code:
            user.is_active = True
            user.save()

            return redirect(reverse('users:login'))

        else:
            return render(request, 'users/verification_form.html', {'form': form, 'pk': pk})

    else:
        form = UserVerificationForm()

    return render(request, 'users/verification_form.html', {'form': form, 'pk': pk})
