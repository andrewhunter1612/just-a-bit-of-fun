from models.time import Time
from models.club import Club
import repositories.club_repository as club_repository
from db.run_sql import run_sql

def add_new_session_time(time):
    sql = "INSERT INTO times_available (start_time, duration, club_id, day) = (%s, %s, %s, %s) RETURNING *"
    values = [time.start_time, time.duration, time.club.id, time.day]
    result = run_sql(sql, values)[0]
    time.id = result["id"]
    return time

def select_time(id):
    sql = "SELECT FROM times_available WHERE id=%s"
    value = [id]
    result = run_sql(sql, value)[0]
    if result is not None:
        club = club_repository.select_club(result["club_id"])
        time = Time(result["start_time"], result["duration"], club, result["day"], result["id"])
        return time

def select_all_times():
    results = run_sql("SELECT * FROM times_available")
    times = []
    for result in results:
        club = club_repository.select_club(result["club_id"])
        time = Time(result["start_time"], result["duration"], club, result["day"], result["id"])
        times.append(time)
    return times

def get_all_available_club_times(club):
    sql = "SELECT * FROM times_available WHERE club_id=%s"
    value = [club.id]
    results = run_sql(sql, value)
    times = []
    for result in results:
        club = club_repository.select_club[result["club_id"]]
        time = Time(result["start_time"], result["duration"], club, result["day"], result["id"])
        times.append(time)
    return times
