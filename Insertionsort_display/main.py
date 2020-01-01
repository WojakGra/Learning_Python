import sys, pygame, random, time


pygame.init()

list = []
for _ in range(400):
    list.append(random.random())

size = width, height = 800, 600
red = 255, 0, 0
black = 0, 0, 0

screen = pygame.display.set_mode(size)
game = 1

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if game == 1:
        screen.fill(black)
        left_side = 1.0
        for j in range(len(list)):
            pygame.draw.line(screen, red, (left_side, (list[j]*600.0)), (left_side, 600.0), 1)
            left_side += 2.0
        pygame.display.flip()
        print(list)
        time.sleep(2)

        # We set swapped to True so the loop looks runs at least once
        for i in range(1, len(list)):
            item_to_insert = list[i]
            # And keep a reference of the index of the previous element
            j = i - 1
            # Move all items of the sorted segment forward if they are larger than
            # the item to insert
            while j >= 0 and list[j] > item_to_insert:
                list[j + 1] = list[j]
                j -= 1
            # Insert the item
            list[j + 1] = item_to_insert
            left_side = 1.0
            screen.fill(black)
            for o in range(len(list)):
                pygame.draw.line(screen, red, (left_side, (list[o]*600.0)), (left_side, 600.0), 1)
                left_side += 2.0
            pygame.display.flip()
            time.sleep(0.01)
        print(list)
    game = 2
    pygame.display.flip()