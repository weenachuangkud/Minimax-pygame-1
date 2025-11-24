from utility import find_best_move, find_win_possibly
from object import Button
from config import *
from random import choice
import pygame
import tictactoe

#wtf is going on lmao
#please dont take these code serouisly lmao, im tryna farming github repo

def main():
    pygame.init()
    tictactoe.init()

    screen = pygame.display.set_mode((SIZE, SIZE))
    pygame.display.set_caption("TicTacToe Minimax py")
    running : bool = True
    gameOver : bool = False
    winner = None
    clock = pygame.time.Clock()

    cell_size = SIZE // 3
    buttons : list[list[Button]] = []
    
    Turn : str = choice([tictactoe.PLAYER, tictactoe.AI])
    TurnEnded = False

    #TODO : fuck i'm out
    def PlayTurn(event):
        nonlocal Turn, TurnEnded, buttons, running
        
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
            TurnEnded = True
            return

        if Turn == tictactoe.PLAYER:    
            if event is None:
                return
            if event.type != pygame.MOUSEBUTTONDOWN or event.button != 1:
                return

            pressed = False
            for i in range(ROWS):
                if pressed:
                    break
                for j in range(COLS):
                    btn = buttons[i][j]
                    if btn.text == "" and btn.handle_event(event, tictactoe.PLAYER):
                        btn.text = tictactoe.PLAYER
                        btn.action = None
                        pressed = True
                        TurnEnded = True
                        break

        elif Turn == tictactoe.AI:
            block_move = find_win_possibly(buttons, tictactoe.PLAYER)
            if block_move:
                r, c = block_move
                buttons[r][c].text = tictactoe.AI
                buttons[r][c].action = None
                TurnEnded = True
            else:
                best_move = find_best_move(buttons)
                if best_move:
                    r, c = best_move
                    if 0 <= r < ROWS and 0 <= c < COLS and buttons[r][c].text == "":
                        buttons[r][c].text = tictactoe.AI
                        buttons[r][c].action = None
                        TurnEnded = True
                   
                   
    #TODO : Contiune
    def IsGameOver():
        nonlocal winner, gameOver
        gameOver = tictactoe.check_tie(buttons)
        winner = tictactoe.check_winner(buttons)
        return True if gameOver or winner else False

    def OnClick(self : Button, symbol : str):
        self.text = symbol

    for r in range(ROWS):
        row = []
        for c in range(COLS):
            x = c * cell_size + CELL_PADDING
            y = r * cell_size + CELL_PADDING
            w = cell_size - CELL_PADDING * 2
            h = cell_size - CELL_PADDING * 2
            btn = Button(x,y,w,h,"", OnClick)
            row.append(btn)
        buttons.append(row)
    
    #TODO : Contiune
    while running:
        if IsGameOver():
            running = False
            print("TIE" if not winner else f"Winner : {winner}")
            break
        
        for event in pygame.event.get():
            if Turn == tictactoe.AI and not TurnEnded:
                PlayTurn(event)
                break
            
            if Turn == tictactoe.PLAYER:
                PlayTurn(event)
                break
                
        if TurnEnded:
            Turn = tictactoe.AI if Turn == tictactoe.PLAYER else tictactoe.PLAYER
            TurnEnded = False
        
        screen.fill(BG_COLOR)
        
        # vert
        for i in range(1, 3):
            x = i * cell_size
            pygame.draw.line(screen, LINE_COLOR, (x, 0), (x, SIZE), LINE_THICKNESS)
        # horz
        for i in range(1, 3):
            y = i * cell_size
            pygame.draw.line(screen, LINE_COLOR, (0, y), (SIZE, y), LINE_THICKNESS)

        for r in range(ROWS):
            for c in range(COLS):
                buttons[r][c].draw(screen)
                
        pygame.display.flip()
        clock.tick(60)
            
    pygame.quit()
    
if __name__ == "__main__":
    main()
