import matplotlib.pyplot as plt
# import pprint ~ for printing coordinates

file = open('cat.results.txt')
results = file.read().split(' \n')
results.remove('')

new_cords = []
coordinates = []

results = [element.split(' ') for element in results]

for element in results:
    for number in element:
        new_cord = float(number)
        new_cords.append(new_cord)

    coordinates.append(new_cords)
    new_cords = []

# pprint.pprint(coordinates) ~ print coordinates

plt.gca().invert_yaxis()
plt.gca().set_facecolor('black')

for element in coordinates:
    x1, y1, x2, y2, w = element

    plt.plot((x1, x2), (y1, y2), 'w-', linewidth=1)

plt.savefig('cat_lsd_image')
plt.show()
