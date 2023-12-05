class Text:
    def __init__(self, text, font, color, position, center=False):
        self.text = text
        self.font = font
        self.color = color
        self.position = position
        self.center = center
        self.rendered_text = self.render()

        self.rendered_text = self.font.render(self.text, True, self.color)
        self.rect = self.rendered_text.get_rect()

        if self.center:
            self.rect.center = self.position
        else:
            self.rect.topleft = self.position


    def render(self):
        return self.font.render(self.text, True, self.color)

    def update(self, new_text):
        self.text = new_text
        self.rendered_text = self.render()

    def draw(self, surface):
        lines = self.text.split('\n')  # Split the text into lines using '\n'
        for i, line in enumerate(lines):
            text_surface = self.font.render(line, True, self.color)
            rect = text_surface.get_rect()

            if self.center:
                rect.center = self.position[0], self.position[1] + i * rect.height
            else:
                rect.topleft = self.position[0], self.position[1] + i * rect.height

            surface.bl