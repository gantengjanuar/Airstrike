#Air Strike 

import random #memasukan elemen tambahan pada pygame ke dalam python
import pygame #memasukan pygame ke dalam python
from Objects import Background, Player, Enemy, Bullet, Explosion, Fuel, Powerup, Button, Message, BlinkingText #memasukan kelas dari file objects

pygame.init() #memulai codingan pygame
pygame.mixer.init()

#Setting Windows

Layar = Lebar, Tinggi = 600, 800 #memasukan ukuran layar dan lebar di windows
pygame.display.set_caption('Air Strike') #memasukan judul game

info = pygame.display.Info() #membuat variabel untuk memberikan info lebar dan tinggi layar windows
lebar = info.current_w #membuat variable untuk memberikan info lebar layar di windows 
tinggi = info.current_h #membuat variable untuk memberikan info panjang layar di windows

if lebar >= tinggi: #membuat variabel untuk mengatur posisi layar game di windows
    win = pygame.display.set_mode(Layar) #membuat layar permainan dapat ditampilkan di layar windows sasuai dengan ukuran variable Layar
else: #jika layar ini tidak berjalan di PC atau laptop akan menjalankan codingan else
    win = pygame.display.set_mode(Layar, pygame.SCALED | pygame.FULLSCREEN) #membuat layar permainan dapat ditampilkan di android dengan penuh atau fullscreen

clock = pygame.time.Clock() #membuat frame rate persecond atau gambar perdetik pada game
FPS = 60 #menentukan frame per second untu di tampilkan ke layar

#==============================================================================================

#Colors

WHITE = (255, 255, 255) #memasukan warna putih border
RED = (255, 0, 0)  #memasukan warna merah border
GREEN = (0, 255, 0)
BLUE = (30, 144, 255)
BLACK = (25, 25, 25)

#IMAGE

plane_img = pygame.image.load('D:/coding/Projek Air Strike/Player/plane2.png')
logo_img = pygame.image.load('D:/coding/Projek Air Strike/Logo/logo.png')
fighter_img = pygame.image.load('D:/coding/Projek Air Strike/Logo/fighter.png')
fighter_img = pygame.transform.scale(fighter_img, (885, 700))
awan_img = pygame.image.load('D:/coding/Projek Air Strike/Background/clouds.png')
awan_img = pygame.transform.scale(awan_img, (Lebar, 350))
icon_img = pygame.image.load('D:/coding/Projek Air Strike/Logo/lala.png') 
pygame.display.set_icon(icon_img)

home_img = pygame.image.load('D:/coding/Projek Air Strike/Button/Home.png')
replay_img = pygame.image.load('D:/coding/Projek Air Strike/Button/repeat.png')
soundOff_img = pygame.image.load('D:/coding/Projek Air Strike/Button/music-off.png')
soundOn_img = pygame.image.load('D:/coding/Projek Air Strike/Button/music-on.png')

#==========================================================================================================
#Tombol

home_btn = Button(home_img, (24, 24), Lebar // 4 - 18, Tinggi // 2 + 120) #Mengatur letak dan ukuran tombol
replay_btn = Button(replay_img, (36, 36), Lebar // 2 - 18, Tinggi // 2 + 115)
sound_btn = Button(soundOn_img, (24, 24), Lebar - Lebar // 4 - 18, Tinggi // 2 + 120)

#==============================================================================================
#FONTS

game_over_font = 'D:/coding/Projek Air Strike/Font/zig.ttf' #masukin font
score_font = 'D:/coding/Projek Air Strike/Font/gomarice_no_continue.ttf'
final_score_font = 'D:/coding/Projek Air Strike/Font/gomarice_no_continue.ttf'
tap_to_play_font = 'D:/coding/Projek Air Strike/Font/DisposableDroidBB_bld.ttf'

game_over_msg = Message(Lebar // 2, 150, 45, 'Game Over', game_over_font, WHITE, win) #variable utuk nampilin font dan mengatur letak, warna, dan tulisan nya)
score_msg = Message(Lebar - 50, 28, 35, '0', score_font, RED, win)
final_score_msg = Message(Lebar // 2, 340, 50, '0', final_score_font, RED, win)
tap_to_play_msg = BlinkingText(Lebar // 2, Tinggi - 100, 35, 'Press Enter To Play', tap_to_play_font, RED, win)

#==============================================================================================
#SOUNDS

player_bullet_sound = pygame.mixer.Sound('D:/coding/Projek Air Strike/Sound/gunshot.wav') #memasukan sound ke pygame saat player menembak
click_sound = pygame.mixer.Sound('D:/coding/Projek Air Strike/Sound/click.mp3') #memasukan sound ke pygame saat player menglick mouse
collision_sound = pygame.mixer.Sound('D:/coding/Projek Air Strike/Sound/mini_exp.mp3') #memasukan sound ke pygame saat musuh menabrak player
blast_sound = pygame.mixer.Sound('D:/coding/Projek Air Strike/Sound/blast.wav') #memasukan sound ke pygame saat musuh meledak
fuel_sound = pygame.mixer.Sound('D:/coding/Projek Air Strike/Sound/fuel.wav') #memasukan sound ke pygame saat player mendapatkan bensin dan power up
ultimate_sound = pygame.mixer.Sound('D:/coding/Projek Air Strike/Sound/ulti.mp3')

pygame.mixer.music.load('D:/coding/Projek Air Strike/Sound/Doof.mp3') #tambahin backsound
pygame.mixer.music.play(loops= -1) #ngatur looping
pygame.mixer.music.set_volume(0.5) #ngatur volume

#==============================================================================================
#OBJECTS

score = 0
BG = Background(win) #membuat variable untuk memasukan kelas background bergerak dari file Objects
P = Player(300, Tinggi - 150) #membuat variable untuk memasukan kelas player dan mengatur posisi player pada layar dari file Objects

enemy_group = pygame.sprite.Group() #memunculkan musuh secara bersamaan
player_bullet_group = pygame.sprite.Group() #mengupdate atau menambahkan kumpulan peluru player dari file object ke dalam file running
enemy_bullet_group = pygame.sprite.Group() #mengupdate atau menambahkan kumpulan peluru musuh dari file object ke dalam file running
explosion_group = pygame.sprite.Group()
fuel_group = pygame.sprite.Group()
powerup_group = pygame.sprite.Group()

def shoot_bullet():
     x, y = P.rect.center[0], P.rect.y #untuk mengetahui posisi player
     
     if P.powerup > 0:
         for dx in range(-3, 4):
             b = Bullet(x, y, 4, dx)   #memunculkan peluru di posisi x+30 / memunculkan peluru 4.png
             player_bullet_group.add(b)
             ultimate_sound.play()
         P.powerup -= 1
     else:
        b = Bullet(x-30, y, 6)   #memunculkan peluru di posisi x+30
        player_bullet_group.add(b) #variable untuk menambahkan peluru
        b = Bullet(x+30, y, 6)  #memunculkan peluru di posisi x+30
        player_bullet_group.add(b) #variable untuk menambahkan peluru
        player_bullet_sound.play() #masukin suara tembakan player
     
def reset():
    enemy_group.empty()
    player_bullet_group.empty()
    enemy_bullet_group.empty()
    explosion_group.empty() 
    fuel_group.empty()
    powerup_group.empty()

    P.reset(P.x, P.y)

level = 1 #untuk mengatur level permainan
plane_destroy_count = 0
plane_frequency = 4500  #untuk mengatur kapan musuh muncul /milisecond
start_time = pygame.time.get_ticks() #untuk mengetahui berapa lama bermain game
E = Enemy(144, 80, 2)  #membuat variable untuk memasukan codingan enemy dan mengatur ukuran dan pilihan musuh pada layar dari file objects

#==============================================================================================

#Setting Kontrol dan In Game

bergerak_atas = False
bergerak_bawah = False
bergerak_kiri = False #membuat variable untuk memberikan info player tidak bergerak kiri 
bergerak_kanan = False #membuat variable untuk memberikan info player tidak bergerak kanan

home_page = True
game_page = False
score_page = False

sound_on = True

running = True #variable untuk menjalankan program game secara terus menerus
while running: #membuat looping agar permainan dapat berjalan secara terus menerus

    for event in pygame.event.get(): #event apa saja yang terjadi di dalam game atau input apa saja yang dimasukan user agar program berjalan seperti menggerakan pesawat
        if event.type == pygame.QUIT: #membuat kunci agar bisa menginput untuk keluar dari game saat menekan tombol silang di layar windows
            running = False #mematikan atau memanggil program quit agar dapat keluar dari game

        if event.type == pygame.KEYDOWN: #memasukan kunci apa yang harus dipencet jika ingin keluar dari game
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q: #menekan tombol esc atau q untuk keluar dari permainan
                running = False #mematikan atau memanggil program quit agar dapat keluar dari game

            if event.key == pygame.K_RETURN:
                if home_page:
                    home_page = False
                    game_page = True

        if event.type == pygame.KEYDOWN and game_page: #membuat kunci agar player bisa bergerak ke kiri dan ke kanan saat menekan kunci
            if event.key == pygame.K_LEFT: #memasukan kunci kiri agar player bergerak ke kiri
                bergerak_kiri = True #menyalakan update dari player agar dapat bergerak ke kiri

            if event.key == pygame.K_RIGHT: #memasukan kunci kanan agar player bergerak ke kanan
                bergerak_kanan = True  #menyalakan update dari player agar dapat bergerak ke kanan

            if event.key == pygame.K_UP: #memasukan kunci kiri agar player bergerak ke kiri
                bergerak_atas = True #menyalakan update dari player agar dapat bergerak ke kiri

            if event.key == pygame.K_DOWN: #memasukan kunci kanan agar player bergerak ke kanan
                bergerak_bawah = True  #menyalakan update dari player agar dapat bergerak ke kanan
                
            if event.key == pygame.K_SPACE: #memasukan kunci spasi untuk menembakan peluru
                shoot_bullet()
        
            if event.key == pygame.K_a: #memasukan kunci a agar player bergerak ke kiri
                bergerak_kiri = True  #menyalakan update dari player agar dapat bergerak ke kiri

            if event.key == pygame.K_d: #memasukan kunci d agar player bergerak ke kanan
                bergerak_kanan = True   #menyalakan update dari player agar dapat bergerak ke kanan

            if event.key == pygame.K_w: #memasukan kunci kiri agar player bergerak ke kiri
                bergerak_atas = True #menyalakan update dari player agar dapat bergerak ke kiri

            if event.key == pygame.K_s: #memasukan kunci kanan agar player bergerak ke kanan
                bergerak_bawah = True  #menyalakan update dari player agar dapat bergerak ke kanan

        if event.type == pygame.MOUSEBUTTONDOWN:
            if home_page:
                home_page = False
                game_page = True
            
        if event.type == pygame.KEYUP: #membuat codingan agar player diam saat tidak ada input yang masuk dari keyboard
            bergerak_kiri = False      #variabel untuk player diam saat tidak ada input
            bergerak_kanan = False     #variabel untuk player diam saat tidak ada input
            bergerak_atas = False
            bergerak_bawah = False
            
#========================================================================================================== 
    if home_page: #mengatur home page 
        win.fill(BLACK)
        win.blit(logo_img, (3, 2)) #mengatur letak logo
        win.blit(fighter_img, (Lebar // 800 - 150, Tinggi // 30)) #mengatur letak logo
        #pygame.draw.circle(win, WHITE, (Lebar // 2, Tinggi // 2 + 50), 51, 3) #membuat border lingkaran sekitar logo
        
        tap_to_play_msg.update()

    if score_page: #mengatur skor page
        win.fill(BLACK)
        win.blit(logo_img, (3, 2))
        game_over_msg.update()
        final_score_msg.update(score)

        if home_btn.draw(win): #mengatur tombol
            home_page = True
            game_page = False
            score_page = False
            reset()
            click_sound.play()

            plane_destroy_count = 0
            level = 1
            score = 0
            score_msg.update(score)

        if replay_btn.draw(win):
            game_page = True
            score_page = False
            reset()
            click_sound.play()

            plane_destroy_count = 0
            level = 1
            score = 0
            score_msg.update(score)

        if sound_btn.draw(win):
            sound_on = not sound_on

            if sound_on:
                sound_btn.update_image(soundOn_img)
                pygame.mixer.music.play(loops=-1) 
            else:
                sound_btn.update_image(soundOff_img)
                pygame.mixer.music.stop()
    
#membuat musuh muncul tiap 3 detik
    if game_page:       
        current_time = pygame.time.get_ticks() #untuk selalu mengupdate tick game
        delta_time = current_time - start_time #mengatur waktunya agar jika sudah melewati frekuensi musuhnya akan muncul
        if delta_time >= plane_frequency: #jika waktunya sudah melewati frekuensi yang ditentukan maka akan menjalankan kode di bawah
            if level == 1:
                type = 1
            if level == 2:
                type = 2
            if level == 3:
                type = 3
            if level == 4:
                type = random.randint(4, 5)
            if level == 5:
                type = random.randint(1, 5)

            x = random.randint(10, Lebar - 100) #variable untuk memunculkan musuh secara acak
            e = Enemy(x, -150, type) #variable untuk memunculkan musuhnya
            enemy_group.add(e) #memasukan kumpulan musuhnya
            start_time = current_time #membuat variable untuk memulai waktunya

        if plane_destroy_count:
            if plane_destroy_count & 5 == 0 and level < 5:
                level += 1
                plane_destroy_count = 0

        P.fuel -= 0.05 #decreasing fuel
        BG.update(1) #mengatur kecepatan pergerakan background 
        #win.blit(awan_img, (0, 70))

        P.update(bergerak_kiri, bergerak_kanan, bergerak_atas, bergerak_bawah, explosion_group) #memasukan update agar player dapat menampilkan animasi bergerak, dan meledal
        P.draw(win) #menampilkan variable P atau menampilkan player ke layar
        
        player_bullet_group.update() #memasukan update agar muncul peluru player
        player_bullet_group.draw(win) #menampilkan peluru player
        enemy_bullet_group.update() #memasukan update agar muncul peluru musuh
        enemy_bullet_group.draw(win) #menampilkan agar peluru musuh
        explosion_group.update()
        explosion_group.draw(win)
        fuel_group.update() 
        fuel_group.draw(win)
        powerup_group.update() 
        powerup_group.draw(win)
        enemy_group.update(enemy_bullet_group, explosion_group) #memasukan update agar muncul musuh
        enemy_group.draw(win) #menampilkan variable enemy menampilkan musuh ke layar
        
        if P.alive:
            player_hit = pygame.sprite.spritecollide(P, enemy_bullet_group, False) #membuat peluru musuh tidak menembus player
            for bullet in player_hit: #jika peluru terkena player maka akan menjalankan kode di bawah
                P.health -= bullet.damage #darah player berkurang sesuai dengan damage dari peluru
                print(P.health)
                
                x, y = bullet.rect.center
                explosion = Explosion(x, y, 1)
                explosion_group.add(explosion)
                bullet.kill() #peluru hancur atau hilang saat terkena player
                collision_sound.play() #memasukan suara
                
            for bullet in player_bullet_group: #mengatur peluru
                planes_hit = pygame.sprite.spritecollide(bullet, enemy_group, False) #variable saat peluru terkena player maka akan hilang
                for plane in planes_hit: #jika player terkena hit maka akan jalan kodingan di bawah
                    plane.health -= bullet.damage #darah player dikurang damage dari peluru musuh
                    if plane.health <= 0:
                        x, y = plane.rect.center
                        rand = random.random()
                        if rand >= 0.9:    #generate powerup secara random
                            power = Powerup(x, y)
                            powerup_group.add(power)
                        elif rand >= 0.3:  #generate fuel secara random
                            fuel = Fuel(x, y)
                            fuel_group.add(fuel)

                        plane_destroy_count += 1
                        score += 1
                        blast_sound.play() #memasukan suara
                        
                    x, y = bullet.rect.center
                    explosion = Explosion(x, y, 1)
                    explosion_group.add(explosion)
                
                    bullet.kill() #peluru hancur atau hilang
                    collision_sound.play() #menampilkan suara
                    
            player_collide = pygame.sprite.spritecollide(P, enemy_group, True)
            if player_collide:           
                x, y = bullet.rect.center
                explosion = Explosion(x, y, 2)
                explosion_group.add(explosion)
                
                x, y = player_collide[0].rect.center
                explosion = Explosion(x, y, 2)
                explosion_group.add(explosion)

                P.health = 0 #membuat player mati jika terkena musuh
                P.alive = False
                blast_sound.play()
                
            if pygame.sprite.spritecollide(P, fuel_group, True):
                P.fuel += 25
                if P.fuel >= 100:
                    P.fuel = 100
                fuel_sound.play() #menampilkan suara

            if pygame.sprite.spritecollide(P, powerup_group, True):  
                P.powerup += 3
                fuel_sound.play()

        if not P.alive or P.fuel <= -10:
            if len(explosion_group) == 0:
                game_page = False
                score_page = True

                reset()

        score_msg.update(score)

        fuel_color = RED if P.fuel <= 40 else GREEN   #jika fuel dibawah 40 fuel color akan berubah jadi merah             
        pygame.draw.rect(win, fuel_color, (30, 20, P.fuel, 10), border_radius=4) #membuat fuel bar berwarna yang akan berkurang sesuai health player
        pygame.draw.rect(win, WHITE, (30, 20, 100, 10), 2, border_radius=4 )
        pygame.draw.rect(win, RED, (30, 32, P.health, 10), border_radius=4) #membuat health bar berwarna yang akan berkurang sesuai health player
        pygame.draw.rect(win, WHITE, (30, 32, 100, 10), 2, border_radius=4 ) #membuat borrder putih di health bar
        win.blit(plane_img, (10, 15))
    
    
    pygame.draw.rect(win, WHITE, (0, 0, Lebar, Tinggi), 5, border_radius=2) #mengatur ukuran dan posisi border atau bingkai layar permainan
    clock.tick(FPS) #memasukan variable FPS agar bisa ditampilkan di windows
    pygame.display.update() #memperbarui perubahan apa saja yang ditambahkan di dalam game seperti mengganti background, menambah player, dll



pygame.quit() #mengakhiri permainan atau keluar dari looping 
