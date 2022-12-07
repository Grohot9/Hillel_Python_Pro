import sqlite3

from flask import Flask
from webargs import fields
from webargs.flaskparser import use_kwargs

from utils import format_records

app = Flask(__name__)


def execute_query(query, args=()):
    with sqlite3.connect("chinook.db") as connection:
        cursor = connection.cursor()
        cursor.execute(query, args)
        connection.commit()
        records = cursor.fetchall()
    return records


@app.route("/sales")
@use_kwargs(
    {
        "country": fields.Str(
            load_default="",
        ),
    },
    location="query"
)
def order_price(country):
    if country:
        query_add = f' WHERE BillingCountry = "{country}"'
        query = f"SELECT SUM(UnitPrice * Quantity) AS Sales, BillingCountry FROM invoice_items JOIN " \
                f"invoices ON invoice_items.InvoiceId = invoices.InvoiceId{query_add} " \
                f"GROUP BY BillingCountry;"
    else:
        query = "SELECT SUM(UnitPrice * Quantity) AS Sales, BillingCountry FROM invoice_items JOIN " \
                "invoices ON invoice_items.InvoiceId = invoices.InvoiceId " \
                "GROUP BY BillingCountry;"
    records = execute_query(query)
    return format_records(records)


@app.route("/track-info")
@use_kwargs(
    {
        "track_id": fields.Int(
            load_default=1,
        ),
    },
    location="query"
)
def get_all_info_about_track(track_id):
    if not str(track_id).isdigit():
        return "ERROR: track_id should be a number"
    query = f"SELECT tracks.TrackId, tracks.Name AS Track, tracks.Composer, albums.Title as Album," \
            f" artists.Name AS Artist, genres.Name AS Genre, playlists.Name AS Playlist," \
            f" floor((tracks.Milliseconds / (1000 * 60)) % 60) || 'm:' || floor((tracks.Milliseconds / 1000) % 60)" \
            f" || 's' AS Time, tracks.Bytes AS Size FROM tracks JOIN albums on tracks.AlbumId = albums.AlbumId JOIN" \
            f" artists on albums.ArtistId = artists.ArtistId JOIN genres on tracks.GenreId = genres.GenreId JOIN " \
            f"playlist_track on tracks.TrackId = playlist_track.TrackId JOIN " \
            f"playlists on playlist_track.PlaylistId = playlists.PlaylistId WHERE tracks.TrackId = {track_id}" \
            f" GROUP BY tracks.TrackId;"
    records = execute_query(query)
    return format_records(records)


app.run(port=5001, debug=True)
