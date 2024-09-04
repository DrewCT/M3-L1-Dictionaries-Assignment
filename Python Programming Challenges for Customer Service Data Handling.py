#Task 1
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket(ticket_id, customer, issue):
    if ticket_id in service_tickets:
        print(f"Ticket ID {ticket_id} already exists.")
    else:
        service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}
        print(f"Ticket {ticket_id} opened successfully.")

def update_status(ticket_id, new_status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = new_status
        print(f"Ticket {ticket_id} status updated to {new_status}.")
    else:
        print(f"Ticket ID {ticket_id} not found.")

def display_tickets(status=None):
    for ticket_id, ticket_info in service_tickets.items():
        if status is None or ticket_info["Status"] == status:
            print(f"{ticket_id}: {ticket_info}")

open_ticket("Ticket003", "Charlie", "Account locked")

update_status("Ticket001", "closed")

print("\nAll tickets:")
display_tickets()

print("\nOpen tickets:")
display_tickets(status="open")

