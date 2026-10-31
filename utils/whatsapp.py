from urllib.parse import quote

# International format with no "+", as wa.me requires.
WHATSAPP_NUMBER = "2349118298317"


def whatsapp_order_url(lines: list[dict]) -> str:
    """wa.me link that opens a chat with the farm, pre-filled with the cart.
    Prices are left out because they're confirmed in the chat."""
    items_text = "\n".join(
        f"- {line['product_name']} ({line['size_label']}) x{line['qty']}"
        for line in lines
    )
    message = f"Hello RedBased Agric Farm, I'd like to order:\n{items_text}"
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(message)}"
