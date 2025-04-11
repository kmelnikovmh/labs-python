from .models import Receipt, Item, Participant
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def my_receipts(request):
    receipts = Receipt.objects.filter(owner=request.user).order_by("-created_at")
    context = {
        "receipts": receipts,
        "total_receipts": receipts.count(),
    }
    return render(request, "checks/my_receipts.html", context)

@login_required
def create_receipt(request):
    if request.method == "POST":
        receipt = Receipt.objects.create(
            owner=request.user,
            title=request.POST.get("title"),
            image=request.FILES.get("image")
        )

        for item_index in range(100):
            item_name_key = f"item_name_{item_index}"
            item_price_key = f"item_price_{item_index}"
            if item_name_key in request.POST:
                item_name = request.POST.get(item_name_key, '') 
                item_price = request.POST.get(item_price_key, '0') 
                if item_name:
                    try:
                        Item.objects.create(
                            name=item_name,
                            price=item_price, 
                            receipt=receipt,
                        )
                    except Exception as e:
                        print(f"Ошибка при создании Item: {e}")

            else:
                break 

        for participant_index in range(100): 
            participant_name_key = f"participant_name_{participant_index}"
            if participant_name_key in request.POST:
                participant_name = request.POST.get(participant_name_key, '')
                if participant_name:
                    Participant.objects.create(
                        name=participant_name,
                        receipt=receipt,
                    )
            else:
                break 

        return redirect("checks:receipt_detail", receipt_id=receipt.id)
    return render(request, "checks/create_receipt.html")


@login_required
def receipt_detail(request, receipt_id):
    receipt = get_object_or_404(Receipt, id=receipt_id, owner=request.user)
    items = receipt.items.all()
    participants = receipt.participants.all()

    total = sum(item.price for item in items)

    context = {
        "receipt": receipt,
        "items": items,
        "participants": participants,
        "total_amount": total,
    }
    return render(request, "checks/receipt_detail.html", context)


@login_required
def delete_receipt(request, receipt_id):
    receipt = get_object_or_404(Receipt, id=receipt_id, owner=request.user)
    if request.method == "POST":
        receipt.delete()
        return redirect("checks:my_receipts")
    return render(request, "checks/receipt_confirm_delete.html", {"receipt": receipt})