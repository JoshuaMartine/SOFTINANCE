import tkinter as tk

class AnimatedBoxes:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=300, height=200, bg='gray')
        self.canvas.pack()

        # Crear cuadros
        self.boxes = [
            self.canvas.create_rectangle(50, 75, 100, 125, fill="white"),
            self.canvas.create_rectangle(110, 75, 160, 125, fill="white"),
            self.canvas.create_rectangle(170, 75, 220, 125, fill="white"),
            self.canvas.create_rectangle(230, 75, 280, 125, fill="white")
        ]
        
        self.current_box = 0
        self.move_up = True
        self.animate()

    def animate(self):
        # Ciclo que mueve un cuadro a la vez
        move_distance = -20 if self.move_up else 20
        self.canvas.move(self.boxes[self.current_box], 0, move_distance)

        # Actualizar cuadro actual y dirección
        self.current_box = (self.current_box + 1) % 4
        if self.current_box == 0:
            self.move_up = not self.move_up

        # Llama a sí mismo después de un tiempo
        self.root.after(500, self.animate)

def main():
    root = tk.Tk()
    root.title("Animación Secuencial de Cuadros")
    app = AnimatedBoxes(root)
    root.mainloop()

if __name__ == "__main__":
    main()
