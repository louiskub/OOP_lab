from fastapi import FastAPI, HTTPException
from fastapi import Depends
from service import OrderDetail, Cabana, Ticket
from booking import Booking, Order

app = FastAPI()

# Temporary storage for orders (replace this with a proper database or storage mechanism)
temp_orders = {}


class TempOrder:
    def __init__(self, order):
        self.order = order


@app.post("/create-temp-order")
async def create_temp_order(visit_date: str, coupon: str):
    # Assuming you have the required parameters for creating an Order
    new_order = Order(visit_date=visit_date, coupon=coupon)
    temp_order_id = len(temp_orders) + 1
    temp_orders[temp_order_id] = TempOrder(order=new_order)
    return {"temp_order_id": temp_order_id}


@app.post("/add-item-to-temp-order/{temp_order_id}/{item_type}/{amount}")
async def add_item_to_temp_order(
    temp_order_id: int, item_type: str, amount: int
):
    if temp_order_id not in temp_orders:
        raise HTTPException(status_code=404, detail="Temp Order not found")

    temp_order = temp_orders[temp_order_id].order
    item = None

    # You need to implement your logic to create an instance of the item based on item_type
    if item_type == "ticket":
        item = Ticket(type="Example Ticket", amount_per_ticket=10, price=20)
    elif item_type == "cabana":
        item = Cabana(id=1, size="Large", zone="A")

    if not item:
        raise HTTPException(status_code=400, detail="Invalid item type")

    order_detail = OrderDetail(item=item, amount=amount)
    temp_order.add_order_detail(order_detail)

    return {"message": "Item added to temp order successfully"}


@app.post("/finalize-temp-order/{temp_order_id}")
async def finalize_temp_order(temp_order_id: int):
    if temp_order_id not in temp_orders:
        raise HTTPException(status_code=404, detail="Temp Order not found")

    temp_order = temp_orders[temp_order_id].order

    # Your logic to check availability, reserve, and perform other actions
    if temp_order.check_still_available():
        temp_order.reserve()

    # Your logic to update status, create a booking, etc.
    booking_id = len(temp_orders) + 1
    booking = Booking(
        customer="Example Customer",
        booking_id=booking_id,
        order=temp_order,
        order_datetime="2024-03-04T12:00:00",
    )

    # Remove the temporary order after finalizing
    del temp_orders[temp_order_id]

    return {"booking_id": booking_id, "message": "Temp Order finalized successfully"}