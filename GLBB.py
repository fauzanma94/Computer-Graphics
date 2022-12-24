import pygame
import math

# Tampilan windows
pygame.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Program Simulasi GLBB")
width = screen.get_width()
height = screen.get_height()

# Warna
hitam = (0,0,0)
putih = (255,255,255)
merah = (255,0,0)
oren = (255,165,0)
biru= (0,255,255)

# Inputan awal
time = 0
velocity = 1
g = 9.8/10000
vx = 0
vy = 0
dt = 0
radius = 0
radius2 = 0
v_input = "0"

# posisi awal bola
ball_x = width//2
ball_y = height//2
angle = 0
#Tambahan
active = False
fall = True
rotation = True
gravity = False
grab = False
click = False

# Waktu
clock = pygame.time.Clock()

def gerakan_bola(ball_vx, ball_vy):
    global ball_x, ball_y, vx, vy
    if ball_vx != 0:
        ball_x += ball_vx * dt
        vx -= vx/300
        if vx > -0.1 and vx < 0.1:
            vx = 0
        if side_L <= 0:
            ball_x = side_R
            vx = -vx / 1
        if side_R >= width:
            ball_x = width-60
            vx = -vx / 1
    if ball_vy != 0:
        if side_T >= 0 :
            ball_y += ball_vy * 2 * dt
        if side_B >= height :
            ball_y = latest_y-10
class Bola_Bergerak:
    def rotated_right(self):
        global vx
        vx = int(v_input) / 90
        get_angle()
    def rotated_left(self):
        global vx
        vx = -int(v_input) / 90
        get_angle()
    def button_key(key):
        global zoom, time, vx
        if key[pygame.K_d] and side_R<= width:
            vx = 0
            gerakan_bola(velocity,0)
        if key[pygame.K_a] and side_L >= 0:
            vx = 0
            gerakan_bola(-velocity,0)
        if key[pygame.K_w] and side_T >= 0:
            gerakan_bola(0,-velocity)
            time = 0
        get_angle()
bola_gerak = Bola_Bergerak()

def get_angle():
    global ball_x, latest_x, angle
    if rotation:
        if latest_x < ball_x:
            angle -= ((abs(ball_x-latest_x)*360)/(3.14))/200
        if latest_x > ball_x:
            angle += ((abs(ball_x-latest_x)*360)/(3.14))/200

def ukuran_bola():
    global radius
    ukuran_bola = (abs(height - 100 - ball_y)) / 200000
    radius = 50 - ukuran_bola

def get_grav():
    global time, ball_y, fall, vy, side_B, height
    if True:
        if fall and side_B <= height:
            ball_y += g * (time**2) * dt
            time += 1
        if side_B >= height:
            fall = False
            time = time/1.2
        if not fall:
            ball_y -= g * (time**2) * dt
            time -= 1
        if time < 1:
            fall = True
            time = 0


def garis_bola(x, y):
    cos = math.cos(math.radians(angle)*-1)
    sin = math.sin(math.radians(angle)*-1)
    x_ya = (x*cos)-(y*sin)
    y_ya = (x*sin)+(y*cos)
    return x_ya,y_ya

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def mouse_grab():
    global ball_x, ball_y
    if grab == True:
        ball_x = mouse_x
        ball_y = mouse_y
        if mouse_x - 40 <= 0:
            ball_x = 60
        if mouse_x + 40 >= width:
            ball_x = width - 60
        if mouse_y - 40 <= 0:
            ball_y = 40
        if mouse_y + 160 >= height:
            ball_y = height - 160
def button(teks, x, y, w, h, color, active_color ,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(screen, color,(x,y,w,h))
    smallText = pygame.font.Font("No Virus.ttf",20)
    textSurf, textRect = text_objects(teks, smallText, putih)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, active_color,(x,y,w,h))
        if click[0] == 1 != None:
            action()
        smallText = pygame.font.Font("No Virus.ttf",20)
        textSurf, textRect = text_objects(teks, smallText, putih)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        screen.blit(textSurf, textRect)

# Buat input box
input_rect = pygame.Rect(10, 530, 200, 35)
color_passive = pygame.Color(putih)
color = color_passive

while True:
    dt = clock.tick_busy_loop(120)
    mouse = pygame.mouse.get_pos()
    mouse_x = mouse[0]
    mouse_y = mouse[1]
    mousebox = pygame.draw.rect(screen, True, pygame.Rect(mouse_x, mouse_y, 1, 1))
    # Background warna window
    screen.fill(hitam)
    # Garis Lintasan
    pygame.draw.line(screen, putih, (0, 497), (1120, 497),20)
    # Membuat Lingkaran
    bola = pygame.draw.circle(screen, biru , (ball_x, ball_y), radius, 3)
    # Batas tiap tepi
    side_T = ball_y-40
    side_B = ball_y+150
    side_L = ball_x-50
    side_R = ball_x+50
    # Posisi Bola
    latest_x = ball_x
    latest_y = ball_y
    # Garis Anti aliasing
    x1,x2 = garis_bola(-radius,0),garis_bola(radius,0)
    x3,x4 = garis_bola(0,-radius),garis_bola(0,radius)
    x1 = ball_x+x1[0],x1[1]+ball_y
    x2 = ball_x+x2[0],x2[1]+ball_y
    x3 = ball_x+x3[0],x3[1]+ball_y
    x4 = ball_x+x4[0],x4[1]+ball_y
    line_rad = pygame.draw.line(screen, merah, x2, x1, 3)
    line_sam = pygame.draw.line(screen, oren, x4, x3, 3) 

    events = pygame.event.get()

    for event in events:
        # kondisi jika inputan kosong
        if v_input == "":
            v_input = "0"

        # untuk keluar program dengan x
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False

        if event.type == pygame.KEYDOWN:
            #input
            if event.key == pygame.K_BACKSPACE:
                v_input = v_input[:-1]
            else:
                diklik = event.unicode
                try:
                    cek = int(diklik)
                    if v_input == "0":
                        v_input = ""
                    v_input += diklik
                except:
                    pass
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not click and bola.colliderect(mousebox):
                vx = 1
                grab = True
                click = True
                rotation = False
            elif click and bola.colliderect(mousebox):
                time = 0
                grab = False
                click = False
                rotation = True
   

    # menampilkan input box
    base_font_input = pygame.font.Font(None,35)
    pygame.draw.rect(screen, color, input_rect, width=3)
    text_surface = base_font_input.render(v_input, True, putih)
    screen.blit(text_surface,(input_rect.x +10 , input_rect.y +6))
    input_rect.w = max(70, text_surface.get_width() + 10)
    gerakan_bola(vx, vy)
    Bola_Bergerak.button_key(pygame.key.get_pressed())
    get_grav()
    ukuran_bola()
    mouse_grab()
  
    button("(", 35, 570, 50, 30, hitam, putih, bola_gerak.rotated_right)
    button(")", 5, 570, 50, 30, hitam, putih, bola_gerak.rotated_left)
    pygame.display.update()