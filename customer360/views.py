from django.shortcuts import render, get_object_or_404, redirect
from datetime import date, timedelta
from django.db.models import Count

# Explicit imports are clearer and avoid wildcard-import issues
from .models import Customer, Interaction

def index(request):
    customers = Customer.objects.all()
    context = {"customers":customers}
    return render(request,"index.html",context=context)

def create_customer(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        customer = Customer.objects.create(name=name,email=email,phone=phone,address=address)
        customer.save()
        msg = "Successfully Saved a Customer"
        return render(request,"add.html",context={"msg":msg})
    return render(request,"add.html")

def summary(request):
    thirty_days_ago = date.today() - timedelta(days=30)
    interactions_qs = Interaction.objects.filter(interaction_date__gte=thirty_days_ago)

    # total count
    count = interactions_qs.count()

    # group by channel and direction
    interactions = interactions_qs.values("channel", "direction").annotate(count=Count("channel"))
    context={
                "interactions":interactions,
                "count":count
             }

    return render(request,"summary.html",context=context)


def interact(request, cid):
    """Minimal interact view: shows choices on GET; creates Interaction on POST."""
    customer = get_object_or_404(Customer, id=cid)

    channels = Interaction.CHANNEL_CHOICES
    directions = Interaction.DIRECTION_CHOICES

    msg = ""
    if request.method == "POST":
        channel = request.POST.get("channel")
        direction = request.POST.get("direction")
        summary_text = request.POST.get("summary", "")

        if not channel or not direction:
            msg = "Please select both channel and direction."
        else:
            Interaction.objects.create(
                customer=customer,
                channel=channel,
                direction=direction,
                summary=summary_text,
            )
            # Post/Redirect/Get
            return redirect('interact', cid=cid)

    context = {
        "customer": customer,
        "channels": channels,
        "directions": directions,
        "msg": msg,
    }
    return render(request, "interact.html", context=context)

