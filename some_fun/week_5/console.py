import repositories.club_repository as club_repository
from models.club import Club


club_1 = Club("Tennis", 4)
club_2 = Club("Squash", 3)

club_repository.add_new_club(club_1)
club_repository.add_new_club(club_2)


