def get_planes_from_db():
    return []


def save_danger_dict_in_db(danger_for_plane_dict):
    pass


def compute_danger_for_plane_from_missile(plane, missile):
    return 0.0


planes = get_planes_from_db()
missiles = []

danger_for_plane_dict = {}

# for each plane compute the expected danger to this plane
for plane in planes:
    danger_for_plane = 0.0

    for missile in missiles:
        danger_for_plane_from_missile = compute_danger_for_plane_from_missile(plane, missile)
        print("computed danger for plane %s from missile %s is %d ", plane, missile, danger_for_plane_from_missile)
        danger_for_plane += danger_for_plane_from_missile

    danger_for_plane_dict[plane] = danger_for_plane

save_danger_dict_in_db(danger_for_plane_dict)

print("the danger map is built and stored in db")
