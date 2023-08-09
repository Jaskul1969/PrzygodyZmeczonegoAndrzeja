def text(text, font,position, screen):
    temp = font.render(text, False,(255,89,200))
    screen.blit(temp, position)
