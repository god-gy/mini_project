from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages

from .models import UserBlessing
from .services import pick_random_blessing, send_blessing_email


def _get_client_ip(request: HttpRequest) -> str | None:
    xff = request.META.get("HTTP_X_FORWARDED_FOR")
    if xff:
        return xff.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR")


@require_http_methods(["GET", "POST"])
def home(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        to_email = (request.POST.get("email") or "").strip()
        if not to_email:
            messages.error(request, "이메일을 입력해 주세요.")
            return redirect("blessings:home")

        blessing_text = pick_random_blessing()

        # base_url 구성: 배포 시엔 settings로 박는 게 안전
        base_url = getattr(settings, "SITE_BASE_URL", None)
        if not base_url:
            # 개발 편의용(리버스 프록시 환경에선 오작동 가능)
            scheme = "https" if request.is_secure() else "http"
            base_url = f"{scheme}://{request.get_host()}"

        send_blessing_email(to_email=to_email, blessing_text=blessing_text, base_url=base_url)
        return render(request, "blessings/email_received.html", {"email": to_email})

    return render(request, "blessings/home.html")


# blessings/views.py
@require_http_methods(["GET", "POST"])
def write(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        from_email = (request.POST.get("from_email") or "").strip()
        message_text = (request.POST.get("message") or "").strip()

        if not message_text:
            messages.error(request, "덕담 내용을 입력해 주세요.")
            return redirect("blessings:write")

        UserBlessing.objects.create(
            from_email=from_email or None,
            message=message_text,
            ip_address=_get_client_ip(request),
            user_agent=request.META.get("HTTP_USER_AGENT", "")[:300],
        )

        messages.success(request, "덕담을 저장했습니다.")
        return redirect("blessings:home")

    # GET
    from_email = (request.GET.get("from") or "").strip()
    return render(request, "blessings/write.html", {"from_email": from_email})



def owner_inbox(request: HttpRequest) -> HttpResponse:
    # MVP: 간단히 접근. 실제 배포는 로그인/비번 보호 필수
    items = UserBlessing.objects.order_by("-created_at")[:500]
    return render(request, "blessings/owner_inbox.html", {"items": items})
