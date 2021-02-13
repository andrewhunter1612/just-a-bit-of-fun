from models.club import Club
from db.run_sql import run_sql

def add_new_club(club):
    sql = "INSERT INTO clubs (name, number_of_courts) VALUES (%s, %s) RETURNING *"
    values = [club.name, club.number_of_courts]
    result = run_sql(sql, values)
    club.id = result[0]["id"]
    return club

def select_club(id):
    sql = "SELECT * FROM clubs WHERE id =%s"
    value = [id][0]
    result = run_sql(sql, value)[0]
    if result is not None:
        club = Club(result["name"], result["number_of_courts"], result["id"])
        return club

def select_all_clubs():
    results = run_sql("SELECT * FROM clubs")
    clubs = []
    for result in results:
        club = Club(result["name"], result["number_of_courts"], result["id"])
        clubs.append(club)
    return clubs
