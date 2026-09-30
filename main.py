from js import document

def create_order():
    # Variables tracking order details (Types of Datatypes)
    total_price = 0.0          # Float datatype
    selected_items = []        # List datatype

    # Checking item 1
    if document.getElementById("item1").checked:
        price = float(document.getElementById("item1").value)
        total_price = total_price + price
        selected_items.append("Chocolate Chip (₱45)")

    # Checking item 2
    if document.getElementById("item2").checked:
        price = float(document.getElementById("item2").value)
        total_price = total_price + price
        selected_items.append("Double Chocolate Fudge (₱50)")

    # Checking item 3
    if document.getElementById("item3").checked:
        price = float(document.getElementById("item3").value)
        total_price = total_price + price
        selected_items.append("Red Velvet Cream Cheese (₱55)")

    # Checking item 4
    if document.getElementById("item4").checked:
        price = float(document.getElementById("item4").value)
        total_price = total_price + price
        selected_items.append("Oatmeal Raisin (₱45)")

    # Checking item 5
    if document.getElementById("item5").checked:
        price = float(document.getElementById("item5").value)
        total_price = total_price + price
        selected_items.append("Matcha Green Tea (₱50)")

    # Format output summary using join() method
    if len(selected_items) > 0:
        items_string = ", ".join(selected_items)
        summary = "Items Ordered: " + items_string + " | Total Amount: ₱" + str(total_price)
    else:
        summary = "No items selected."

    # Display total in HTML
    document.getElementById("receipt-output").innerText = summary