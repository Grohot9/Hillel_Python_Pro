from flask import Flask
from webargs import fields
from webargs.flaskparser import use_kwargs

from utils import format_records, execute_query

app = Flask(__name__)


# First Task
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Circle(Point):
    def __init__(self, x=0, y=0, radius=1):
        super().__init__(x=x, y=y)
        self.radius = radius

    def contains(self, point: Point) -> bool:
        print(self.x, self.y, self.radius, point.x, point.y)
        if ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 2 <= self.radius:
            return True
        return False


@app.route("/stats_by_city")
@use_kwargs(
    {
        "genre": fields.Str(
            required=True,
        ),
    },
    location="query"
)
def stats_by_city(genre):
    query = f"SELECT genres.Name, invoices.BillingCity, COUNT(invoices.BillingCity) FROM genres JOIN tracks ON" \
            f" genres.GenreId = tracks.GenreId JOIN invoice_items ON tracks.TrackId = invoice_items.TrackId JOIN" \
            f" invoices ON invoice_items.InvoiceId = invoices.InvoiceId WHERE genres.Name = \"{genre}\";"
    result = execute_query(query)
    if result == [(None, None, 0)]:
        return "ERROR: genre not found"
    return format_records(result)


app.run(port=5001, debug=True)
