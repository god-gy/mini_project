import random
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.urls import reverse

from .models import PresetBlessing


def pick_random_blessing() -> str:
    qs = PresetBlessing.objects.filter(is_active=True).values_list("content", flat=True)
    contents = list(qs)
    if not contents:
        return "새해 복 많이 받으세요. 올해도 무탈하시길 바라요."
    return random.choice(contents)


def send_blessing_email(to_email: str, blessing_text: str, base_url: str):
    site_name = getattr(settings, "SITE_NAME", "새해 덕담")
    write_url = f"{base_url}{reverse('blessings:write')}?from={to_email}"

    subject = f"🎉 {site_name} : 새해 덕담이 도착했어요"

    # 텍스트 버전(메일 앱이 HTML을 못 읽는 경우 대비)
    text_body = (
        f"{site_name}\n\n"
        f"새해 덕담이 도착했습니다.\n\n"
        f"{blessing_text}\n\n"
        f"나도 덕담하기: {write_url}\n"
    )

    # HTML 버전(카드형)
    html_body = f"""
    <!doctype html>
    <html>
    <head>
      <meta charset="utf-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <title>{site_name}</title>
    </head>
    <body style="margin:0; background:#0b0f19; font-family: Arial, sans-serif; color:#e5e7eb;">
      <div style="max-width:720px; margin:0 auto; padding:26px 14px;">

        <div style="
          border:1px solid rgba(255,255,255,.10);
          background: linear-gradient(180deg, rgba(255,255,255,.05), rgba(255,255,255,.02));
          border-radius:18px;
          padding:18px 18px 14px;
          box-shadow: 0 18px 60px rgba(0,0,0,.35);
        ">
          <div style="display:flex; align-items:center; gap:10px; margin-bottom:12px;">
            <div style="
              width:34px; height:34px; border-radius:12px;
              background: radial-gradient(circle at 30% 30%, rgba(96,165,250,.9), rgba(34,197,94,.75) 55%, rgba(168,85,247,.35));
            "></div>
            <div>
              <div style="font-weight:700; letter-spacing:-.2px;">{site_name}</div>
              <div style="font-size:12px; color:#9ca3af;">새해 덕담 한 통, 가볍게 받아두기</div>
            </div>
          </div>

          <div style="font-size:20px; font-weight:800; letter-spacing:-.4px; margin:0 0 10px;">
            🎉 새해 덕담이 도착했어요
          </div>

          <div style="
            border:1px solid rgba(255,255,255,.10);
            background: rgba(15,23,42,.65);
            border-radius:16px;
            padding:14px;
            white-space:pre-wrap;
            line-height:1.65;
            font-size:15px;
          ">{blessing_text}</div>

          <div style="margin-top:14px;">
            <a href="{write_url}" style="
              display:inline-block;
              padding:12px 16px;
              border-radius:14px;
              text-decoration:none;
              font-weight:800;
              background: linear-gradient(180deg, rgba(34,197,94,.95), rgba(34,197,94,.75));
              color:#06110a;
              border: 1px solid rgba(34,197,94,.45);
            ">
              나도 덕담하기
            </a>
          </div>

          <div style="margin-top:10px; font-size:12px; color:#9ca3af;">
            버튼이 안 눌리면 아래 링크를 복사해서 열어주세요.<br/>
            <span style="word-break:break-all; color:#93c5fd;">{write_url}</span>
          </div>
        </div>

        <div style="margin-top:14px; text-align:center; color:#6b7280; font-size:12px;">
          © {site_name}
        </div>
      </div>
    </body>
    </html>
    """

    msg = EmailMultiAlternatives(
        subject=subject,
        body=text_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[to_email],
    )
    msg.attach_alternative(html_body, "text/html")
    msg.send()
