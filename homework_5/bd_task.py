from flask import Flask
from webargs import fields
from webargs.flaskparser import use_kwargs

from utils import format_records, execute_query

app = Flask(__name__)


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
    query = f"SELECT BillingCity FROM (SELECT genres.Name, invoices.BillingCity, COUNT(invoices.BillingCity)" \
            f" FROM genres JOIN tracks ON genres.GenreId = tracks.GenreId JOIN invoice_items ON" \
            f" tracks.TrackId = invoice_items.TrackId JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId" \
            f" WHERE genres.Name = \"{genre}\");"
    result = execute_query(query)
    if result == [(None, None, 0)]:
        return "ERROR: genre not found"
    return format_records(*result)


app.run(port=5001, debug=True)
