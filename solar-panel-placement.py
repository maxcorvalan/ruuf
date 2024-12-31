def max_paneles(a, b, x, y):
    def puede_colocar_panel(grid, panel_ancho, panel_alto, pos_x, pos_y):
        if pos_x + panel_ancho > len(grid[0]) or pos_y + panel_alto > len(grid):
            return False

        for dy in range(panel_alto):
            for dx in range(panel_ancho):
                if grid[pos_y + dy][pos_x + dx] == 1:
                    return False

        return True

    def colocar_panel(grid, panel_ancho, panel_alto, pos_x, pos_y):
        for dy in range(panel_alto):
            for dx in range(panel_ancho):
                grid[pos_y + dy][pos_x + dx] = 1

    def quitar_panel(grid, panel_ancho, panel_alto, pos_x, pos_y):
        for dy in range(panel_alto):
            for dx in range(panel_ancho):
                grid[pos_y + dy][pos_x + dx] = 0

    def backtrack(grid):
        max_paneles = 0
        for pos_y in range(len(grid)):
            for pos_x in range(len(grid[0])):
                if a != b and puede_colocar_panel(grid, a, b, pos_x, pos_y):
                    colocar_panel(grid, a, b, pos_x, pos_y)
                    max_paneles = max(max_paneles, 1 + backtrack(grid))
                    quitar_panel(grid, a, b, pos_x, pos_y)

                if a != b and puede_colocar_panel(grid, b, a, pos_x, pos_y):
                    colocar_panel(grid, b, a, pos_x, pos_y)
                    max_paneles = max(max_paneles, 1 + backtrack(grid))
                    quitar_panel(grid, b, a, pos_x, pos_y)

                if a == b and puede_colocar_panel(grid, a, b, pos_x, pos_y):
                    colocar_panel(grid, a, b, pos_x, pos_y)
                    max_paneles = max(max_paneles, 1 + backtrack(grid))
                    quitar_panel(grid, a, b, pos_x, pos_y)

        return max_paneles

    if a <= 0 or b <= 0 or x <= 0 or y <= 0:
        return 0

    if (x % a == 0 and y % b == 0) or (x % b == 0 and y % a == 0):
        return (x // a) * (y // b) if (x % a == 0 and y % b == 0) else (x // b) * (y // a)

    grid = [[0 for _ in range(x)] for _ in range(y)]

    return backtrack(grid)

print(max_paneles(1, 2, 2, 4))  # Salida esperada: 4
print(max_paneles(1, 2, 3, 5))  # Salida esperada: 7
print(max_paneles(2, 2, 1, 10)) # Salida esperada: 0