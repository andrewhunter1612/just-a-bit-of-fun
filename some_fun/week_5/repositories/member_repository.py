from models.member import Member
from models.club import Club
import repositories.club_repository as club_repository
from db.run_sql import run_sql


def add_new_member(member):
    sql = "INSERT INTO members (name, club_id) = (%s, %s) RETURNING *"
    values = [member.name, member.club.id]
    result = run_sql(sql, values)[0]
    member.id = result["id"]
    return member

def select_member(member):
    sql = "SELECT * FROM members WHERE id=%s"
    value = [member.id]
    result = run_sql(sql, value)[0]
    if result is not None:
        club = club_repository.select_club(result["club_id"])
        member = Member(result["name"], club, result["id"])
        return member

def select_all_members():
    results = run_sql("SELECT * FROM members")
    members = []
    for result in results:
        club = club_repository.select_club(result["club_id"])
        member = Member(result["name"], club, result["id"])
        members.append(member)
    return members