from typing import Any
import pygame #memasukan pygame ke dalam python
from pygame.sprite import Group, Group #memasukan elemen group ke python dari pygame


#Setting Background

Layar = Lebar, Tinggi = 600, 800 #memasukan ukuran layar di windows

pygame.mixer.init()

class Background(): #membuat kelas untuk membuat mekanisme background yang dapat bergerak
    def __init__(self, win): #membuat pembangun untuk function dan menjadikan satu object ke dalam self
        self.win = win #memasukan atribut kelas background pada variable win atau windows menggunakan self

        self.image = pygame.image.load('D:/coding/Projek Air Strike/Background/bg2.png') #memasukan atau mengimport foto background dari file
        self.image = pygame.transform.scale(self.image, (Lebar, Tinggi)) #mengatur agar besar foto yang dari file sesuai dengan ukuran Layar game yang kita buat 
        self.rect = self.image.get_rect() #memberikan bingkai persegi panjang di pinggiran foto background yang sudah kita masukan agar backgroundnya dapat digerakan

        self.reset() #mereset gambar background ke posisi semula 
        self.move = True #membuat variable untuk menandakan bahwa gambar dapat bergerak
    
    def update(self, speed): #mengatur kecepatan bergerak gambar background 1 dan gambar background 2
        if self.move: #menggunakan function if agar jika gamenya belum dimulai backgroundnya tidak akan bergerak dan jika sudah dimulai maka funktion if akan menjalankan kodingan di bawah
            self.y1 += speed #menambahkan speed atau kecepatan pada variable y1 atau gambar pertama backgroundnya
            self.y2 += speed #menambahkan speed atau kecepatan pada variable y2 atau gambar background kedua yang berada diatas layar background pertama

            # Sistem Looping dari background yang dapat bergerak yaitu gambar pertama akan turun dan gambar kedua akan mengikuti gambar pertama, lalu layar kedua akan muncul kembali kelayar dan terus seperti itu.
            if self.y1 >= Tinggi: #jika variable y1 lebih banyak atau lebih tinggi dari Tinggi layar game maka dia harus berada di atas layar game atau minus Tinggi
                self.y1 = -Tinggi #jika variable y1 lebih banyak atau lebih tinggi dari Tinggi layar game maka dia harus berada di atas layar game atau minus Tinggi
            if self.y2 >= Tinggi: #jika variable y2 lebih banyak atau lebih tinggi dari Tinggi layar game maka dia harus berada di atas layar game atau minus Tinggi
                self.y2 = -Tinggi #jika variable y2 lebih banyak atau lebih tinggi dari Tinggi layar game maka dia harus berada di atas layar game atau minus Tinggi

        self.win.blit(self.image, (self.x, self.y1)) #function untuk menampilkan mekanisme layar bergerak ini dan mengatur posisi gambar backgroud 1 atau y1 secara bergilir
        self.win.blit(self.image, (self.x, self.y2)) #function untuk menampilkan mekanisme layar bergerak ini dan mengatur posisi gambar backgroud 2 atau y2 secara bergilir

    def reset(self): #membuat bungkus untuk membuat kodingan mereset baxkground
        self.x = 0 #memunculkan foto background di posisi x = 0 atau bisa dibilang di tengah layar
        self.y1 = 0 #memunculkan foto background di posisi y = 0 atau bisa dibilang di tengah layar
        self.y2 = -Tinggi #menaruh background kedua diatas posisi background pertama agar nantinya background kedua ini dapat bergerak kebawah dan foto backgroundnya seolah - olah dapat bergerak

#==============================================================================================

#Setting Player

class Player: #membuat kelas untuk mengatur mekanisme player
    def __init__(self, x, y): #membuat pembangun function untuk di jadikan kedalam satu object ke dalam self dan menempatkan posisi player

        self.image_list = [] #membuat list agar dapat memasukan 2 foto player 
        for i in range(2): #membuat list untuk memasukan gambar player 1 dan 2
            img = pygame.image.load(f'D:/coding/Projek Air Strike/Player/player{i+1}.png') #memasukan foto palyer1 dan player2 dari file
            img = pygame.transform.scale(img, (125, 100)) #mengatur perubahan ukuran fotonya di dalam game
            self.image_list.append(img) #menambahkan list gambar player ke 2 pada img

        self.x = x
        self.y = y
        self.reset(self.x, self.y)

    def reset(self, x, y):
        self.index = 0 #menampilkan gambar player 1
        self.image = self.image_list[self.index] #melooping gambar agar dapat muncul secara terus menerus di layar
        self.rect = self.image.get_rect(center=(x, y)) #memposisikan gambar player di tengah x dan y

        self.counter = 0 #pergerakan gambar playernya perframe
        self.speed = 5 #membuat kecepatan perubahan dari foto player 1 ke 2
        self.health = 100 #membuat variable darah atau nyawa player
        self.fuel = 100
        self.powerup = 0
        self.alive = True #variable player hidup
        self.lebar = self.image.get_width() #variable untuk memberikan info lebar dari layar game
        self.tinggi = self.image.get_height()

    def update(self, bergerak_kiri, bergerak_kanan, bergerak_atas, bergerak_bawah, explosion_group): #membuat bungkus untuk membuat kode agar player dapat animasi bergerak dan dapat bergerak ke kiri dan ke kanan tanpa melewati batas layar
        if self.alive:
            if bergerak_kiri and self.rect.x > 2: #jika player bergerak ke kiri dan posisi player kurang dari x = 2 maka akan menjalankan kodingan di bawah
                self.rect.x -= self.speed #player akan bergerak ke posisi -x atau ke kiri
        
            if bergerak_kanan and self.rect.x < Lebar - self.lebar: #jika player bergerak ke kanan dan posisi x player kurang dari lebar layar game maka akan menjalankan kodingan di bawah
                self.rect.x += self.speed #player akan bergerak ke posisi +x atau ke kanan

            if bergerak_atas and self.rect.y > 2: #jika player bergerak ke kiri dan posisi player kurang dari x = 2 maka akan menjalankan kodingan di bawah
                self.rect.y -= self.speed #player akan bergerak ke posisi -x atau ke kiri
        
            if bergerak_bawah and self.rect.y < Tinggi - self.tinggi: #jika player bergerak ke kanan dan posisi x player kurang dari lebar layar game maka akan menjalankan kodingan di bawah
                self.rect.y += self.speed #player akan bergerak ke posisi +x atau ke kanan
            
            if self.health <= 0:  #jika darah player mencapai 0
                x, y = self.rect.center
                explosion = Explosion(x, y, 2)
                explosion_group.add(explosion)
                
                self.alive = False  #player akan mati

        self.counter += 1 #player akan bergerak maju setiap 1 frame
        if self.counter >= 2: #jika gambar player sudah bergerak melebihi 1 frame maka akan menjalankan kodingan di bawah atau berganti menjadi gambar player ke 2 agar membuat animasi playernya
            self.index = (self.index + 1) % len(self.image_list) #saat player sudah bergerak melebihi 1 frame maka index nya akan kembali ke 0 secara otomatis dan terjadilah looping untuk animasi player
            self.image = self.image_list[self.index] #memasukan list gambar playernya ke funtion if ini
            self.counter = 0 #memasukan pergerakan awal gambar playernya

    def draw(self, win): #membuat bungkus atau function def untuk menampilkan gambar player ke layar game
        if self.alive:
            win.blit(self.image, self.rect) #menempatkan posisi player di dalam layar game

#==============================================================================================
        
#Setting Musuh

class Enemy(pygame.sprite.Sprite):  # membuat kelas musuh dan menambah fitur pygame untuk menampilkan sekumpulan musuh dan membuat destroy plane effect
    def __init__(self, x, y, type_): #membuat pembangun function untuk di jadikan kedalam satu object ke dalam self dan menempatkan posisi musuh dan functon type digunakan untuk memasukan angka ke dalam kodingan untuk meload atau memunculkan jenis - jenis musuhnya
        super(Enemy, self).__init__() #mengaktifkan fitur baru dalam python dari pygame

        self.type = type_ #membuat function type agar dapat meload atau menampilkan berbagai macam jenis musuh sesuai dengan input apa yang kita masukan
        self.image_list = [] #membuat list agar dapat memasukan berbagai foto musuhnya
        for i in range(2): #membuat list untuk memasukan gambar musuh 1 dan 2     
            if type_ == 1:                        #memunculkan enemy 1 saat di running bila dimasukan angka 1 
                img = pygame.image.load(f'D:/coding/Projek Air Strike/Enemy/enemy1-{i+1}.png') #memasukan foto semua foto enemy 1 dari file
            if type_ == 2:                        #memunculkan enemy 2 saat di running bila dimasukan angka 2
                img = pygame.image.load(f'D:/coding/Projek Air Strike/Enemy/enemy2-{i+1}.png') #memasukan foto semua foto enemy 2 dari file
            if type_ == 3:                        #memunculkan enemy 3 saat di running bila dimasukan angka 3
                img = pygame.image.load(f'D:/coding/Projek Air Strike/Enemy/enemy3-{i+1}.png') #memasukan foto semua foto enemy 3 dari file
            if type_ == 4:                        #memunculkan enemy 4 saat di running bila dimasukan angka 4 
                img = pygame.image.load(f'D:/coding/Projek Air Strike/Choppers/chopper1-{i+1}.png') #memasukan foto semua foto enemy 4 dari file
            if type_ == 5:                        #memunculkan enemy 5 saat di running bila dimasukan angka 5
                img = pygame.image.load(f'D:/coding/Projek Air Strike/Choppers/chopper2-{i+1}.png') #memasukan foto semua foto enemy 5 dari file
            
            w, h = img.get_width(), img.get_height() #membuat variable ukuran asli gambar musuhnya untuk di ubah ukurannya saat di dalam game tampa merusak animasi musuh
            height = (100 * h) // w #mengubah ukuran gambar asli musuhnya 
            img = pygame.transform.scale(img, (150, 100)) #mengatur perubahan ukuran gambar musuh di dalam game
            
            self.image_list.append(img) #menambahkan list gambar musuh ke 2 pada img
        
        self.index = 0 #menampilkan gambar muasuh 1
        self.image = self.image_list[self.index] #melooping gambar agar dapat muncul secara terus menerus di layar
        self.rect = self.image.get_rect() #memposisikan gambar musuh
        self.rect.x = x #membuat variable untuk #memposisikan gambar musuh di x
        self.rect.y = y #membuat variable untuk #memposisikan gambar musuh di y

        self.frame_dict = {1:3, 2:3, 3:3, 4:5, 5:4} #merubah musuh dengan mengubah value dari gambar musuhnya
        self.frame_fps = self.frame_dict[type_] #membuat variable untuk mengakses variable value type
        
        self.counter = 0 #pergerakan gambar musuhnya perframe
        self.speed = 1 #membuat kecepatan perubahan dari foto musuh 1 ke 2
        self.health = 100 #membuat variable darah atau nyawa musuh
        self.bullet_counter = 0 #pergerakan gambar pelurunya perframe

        if self.type in (1, 2, 3): #memasukan suara musuh
            self.fx = pygame.mixer.Sound('D:/coding/Projek Air Strike/Sound/plane5.mp3')
        elif self.type in (4, 5): #memasukan suara musuh
            self.fx = pygame.mixer.Sound('D:/coding/Projek Air Strike/Sound/chopper.mp3')

        self.fx.play(-1)

    def shoot(self, enemy_bullet_group): #membuat bungkus untuk mengatur posisi dan jumlah tembakan musuh
        if self.type in (1, 4, 5): #jika musuh yang dimasukan tipe 1 4 dan 5 maka akan menjalankan kode di bawah
            x, y = self.rect.center #memberi variable untuk menandakan posisi x dan y berada di tengah
            b = Bullet(x, y, self.type) #untuk mengatur poisi tembakan musuhnya berada di tengah
            enemy_bullet_group.add(b) #untuk memunculkan pelurunya
            
        if self.type in (2, 3): #jika musuh yang dimasukan tipe 2, 3 maka akan menjalankan kode di bawah
            x, y = self.rect.center #memberi variable untuk menandakan posisi x dan y berada di tengah
            b = Bullet(x-25, y+10, self.type) #untuk mengatur poisi tembakan musuhnya 
            enemy_bullet_group.add(b) #untuk memunculkan pelurunya
            b = Bullet(x+25, y+10, self.type) #untuk mengatur poisi tembakan musuhnya 
            enemy_bullet_group.add(b) #untuk memunculkan pelurunya
            
    def update(self, enemy_bullet_group, explosion_group): #membuat bungkus untuk membuat kode agar musuh dapat animasi bergerak dan dapat bergerak dari atas ke bawah
        self.rect.y += self.speed #menggerakan musuh dari atas ke bawah
        if self.rect.top >= Tinggi: #membuat jika musuh mencapai ketinggian tertentu akan meledak
           self.kill()  #untuk mengaktifkan kode meledak atau mematikan musuhnya
           
        if self.health <= 0:
            x, y = self.rect.center
            explosion = Explosion(x, y, 2)
            explosion_group.add(explosion)
            
            self.kill()
            self.fx.stop()
            
        self.bullet_counter += 1 #peluru akan bergerak maju setiap 1 frame
        if self.bullet_counter >= 60: #membuat tiap 60frame per detik akan muncul tembakan musuh
            self.shoot(enemy_bullet_group) #meyuruh agar musuhnya dapat menembak
            self.bullet_counter = 0 #pergerakan gambar pelurunya perframe
            
        self.counter += 1 #peluru akan bergerak maju setiap 1 frame
        if self.counter >= self.frame_fps: # mengakses variable value type
            self.index = (self.index + 1) % len(self.image_list)  #ngehandle animation frame enemy
            self.image = self.image_list[self.index] #memasukan list gambar pelurunya ke funtion if ini
            self.counter = 0 #pergerakan gambar pelurunya perframe

    def draw(self, win): #membuat bungkus atau function def untuk menampilkan gambar musuh ke layar game
        win.blit(self.image, self.rect) #menempatkan posisi musuh di dalam layar game

#==============================================================================================
    
#Membuat Mekanisme Peluru
              
class Bullet(pygame.sprite.Sprite): # membuat kelas musuh dan menambah fitur pygame untuk menampilkan sekumpulan peluru
    def __init__(self, x, y, type_, dx=None): #membuat pembangun function untuk di jadikan kedalam satu object ke dalam self dan menempatkan posisi peluru dan functon type digunakan untuk memasukan angka ke dalam kodingan untuk meload atau memunculkan jenis - jenis pelurunya
        super(Bullet, self).__init__() #mengaktifkan fitur baru dalam python dari pygame
        
        self.dx = dx
        powerup_bullet = False
        if self.dx in range(-3, 4):
            powerup_bullet = True
        
        if type_ == 1: #memunculkan peluru 1 saat di running bila dimasukan angka 1 
            self.image = pygame.image.load('D:/coding/Projek Air Strike/Bullets/1.png') #memasukan foto semua foto peluru 1 dari file
            self.image = pygame.transform.scale(self.image, (20, 40)) #mengatur perubahan ukuran fotonya di dalam game
        if type_ == 2: #memunculkan peluru 2 saat di running bila dimasukan angka 2
            self.image = pygame.image.load('D:/coding/Projek Air Strike/Bullets/2.png') #memasukan foto semua foto peluru 2 dari file
            self.image = pygame.transform.scale(self.image, (15, 30)) #mengatur perubahan ukuran fotonya di dalam game
        if type_ == 3: #memunculkan peluru 3 saat di running bila dimasukan angka 3
            self.image = pygame.image.load('D:/coding/Projek Air Strike/Bullets/3.png') #memasukan foto semua foto peluru 3 dari file
            self.image = pygame.transform.scale(self.image, (20, 40)) #mengatur perubahan ukuran fotonya di dalam game
        if type_ in (4, 5): #memunculkan peluru 4 saat di running bila dimasukan angka 4
            self.image = pygame.image.load('D:/coding/Projek Air Strike/Bullets/4.png') #memasukan foto semua foto peluru 4 dari file
            self.image = pygame.transform.scale(self.image, (20, 20)) #mengatur perubahan ukuran fotonya di dalam game
        if type_ == 6: #memunculkan peluru 5 saat di running bila dimasukan angka 5
            self.image = pygame.image.load('D:/coding/Projek Air Strike/Bullets/5.png') #memasukan foto semua foto peluru 5 dari file
            self.image = pygame.transform.scale(self.image, (20, 40)) #mengatur perubahan ukuran fotonya di dalam game
            
        self.rect = self.image.get_rect(center=(x, y)) #memposisikan gambar peluru
        if type_ == 6 or powerup_bullet: #jika memasukan angka 6 maka akan menjalankan kodingan di bawah
            self.speed = -3 #membuat peluru bergerak keatas
        else: #jika memasukan angka selain 6 maka akan menjalankan kodingan di bawah
            self.speed = 3 #membuat peluru bergerak kebawah
            
        if self.dx == None:
            self.dx = 0
            
        self.damage_dict = {1:5, 2:10, 3:15, 4:20, 4:25, 5:26, 6:15} #memasukan damage peluru berdasarkan tipe musuh & Player
        self.damage = self.damage_dict[type_] #membuat variable damage peluru
        if powerup_bullet:
            self.damage = 25 #increase damage player when get powerup
                
    def update(self): #mengatur pergerakan peluru
        self.rect.x += self.dx
        self.rect.y += self.speed #mengatur peluru agar dapat bergerak ke atas
        if self.rect.bottom <= 0: #bila peluru sudah kebawah dan keluar layar maka akan menjalankan kode di bawah
            self.kill() #jika sudah sampai bawah maka peluru akan hancur
        if self.rect.top >= Tinggi: #bila peluru sudah keatas dan keluar layar maka akan menjalankan kode di bawah
            self.kill #jika sudah sampai atas maka peluru akan hancur
    
    def draw(win): #membuat bungkus atau function def untuk menampilkan gambar peluru ke layar game
        win.blit(self.image, self.rect) #menempatkan posisi peluru di dalam layar game
        
#==========================================================================================================
        
class Explosion(pygame.sprite.Sprite): # membuat kelas musuh dan menambah fitur pygame untuk menampilkan sekumpulan peluru
    def __init__(self, x, y, type_): #membuat pembangun function untuk di jadikan kedalam satu object ke dalam self dan menempatkan posisi peluru dan functon type digunakan untuk memasukan angka ke dalam kodingan untuk meload atau memunculkan jenis - jenis pelurunya
        super(Explosion, self).__init__()
        
       
        self.img_list = []
        if type_ == 1:
            self.lenghth = 3  #3 foto 3 length
        elif type_ == 2:
            self.lenghth = 8  #8 foto 8 length
            
        for i in range(self.lenghth):
            img = pygame.image.load(f'D:/coding/Projek Air Strike/Explosion{type_}/{i+1}.png')
            w, h = img.get_size()  #mengetahui ukuran gambar
            width = int(w * 0.40)
            height = int(w * 0.40)
            img = pygame.transform.scale(img, (width, height)) #resize gambar
            self.img_list.append(img)
            
        self.index = 0
        self.image = self.img_list[self.index]
        self.rect = self.image.get_rect(center=(x, y)) 
            
        self.counter = 0

           
    def update(self):
        self.counter += 1 
        if self.counter >= 7: # mengakses variable value type
            self.index += 1
            if self.index >= self.lenghth: 
                self.kill()
            else:
                self.image = self.img_list[self.index] #memasukan list gambar pelurunya ke funtion if ini
                self.counter = 0 #pergerakan gambar pelurunya perframe
  
    def draw(win): #membuat bungkus atau function def untuk menampilkan gambar peluru ke layar game
        win.blit(self.image, self.rect) #menempatkan posisi peluru di dalam layar game
        
#============================================
#Fuel Class
class Fuel(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Fuel, self).__init__()
        
        self.image = pygame.image.load('D:/coding/Projek Air Strike/Player/fuel.png')
        self.rect = self.image.get_rect(center=(x, y))
        
    def update(self):
        self.rect.y += 1
        if self.rect.top >= Tinggi:
            self.kill()
     
    def draw(self, win):
        win.blit(self.image, self.rect)      
            
#============================================
        
#Powerup Class
class Powerup(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Powerup, self).__init__()
        
        self.image = pygame.image.load('D:/coding/Projek Air Strike/Player/powerup.png')
        self.rect = self.image.get_rect(center=(x, y))
        
    def update(self):
        self.rect.y += 1
        if self.rect.top >= Tinggi:
            self.kill()
     
    def draw(self, win):
        win.blit(self.image, self.rect) 

#==========================================================================================================

class Button(pygame.sprite.Sprite):
	def __init__(self, img, scale, x, y):
		super(Button, self).__init__()
		
		self.scale = scale
		self.image = pygame.transform.scale(img, self.scale)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.clicked = False

	def update_image(self, img):
		self.image = pygame.transform.scale(img, self.scale)

	def draw(self, win):
		action = False
		pos = pygame.mouse.get_pos()
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] and not self.clicked:
				action = True
				self.clicked = True

			if not pygame.mouse.get_pressed()[0]:
				self.clicked = False

		win.blit(self.image, self.rect)
		return action
    
#==========================================================================================================
    
class Message():
    def __init__(self, x, y, size, text, font, color, win):
        self.win = win
        self.color = color
        self.x, self.y = x, y

        if not font:
            self.font = pygame.font.SysFont('Verdana', size)
            anti_alias = True
        else:
            self.font = pygame.font.Font(font, size)
            anti_alias = False

        self.image = self.font.render(text, anti_alias, color)
        self.rect = self.image.get_rect(center=(x, y))
        self.shadow = self.font.render(text, anti_alias, (54, 69, 79))
        self.shadow_rect = self.image.get_rect(center=(x + 2, y + 2))

    def update(self, text = None, Shadow = True):
        if text:
            self.image = self.font.render(f'{text}', False, self.color)
            self.rect = self.image.get_rect(center=(self.x, self.y))
            self.shadow = self.font.render(f'{text}', False, (54, 69, 79))
            self.shadow_rect = self.image.get_rect(center=(self.x + 2, self.y + 2))

        if Shadow:
            self.win.blit(self.shadow, self.shadow_rect)
        self.win.blit(self.image, self.rect)

class BlinkingText(Message):
    def __init__(self, x, y, size, text, font, color, win):
        super(BlinkingText, self).__init__(x, y, size, text, font, color, win)
        self.index = 0
        self.show = True

    def update(self):
        self.index += 1
        if self.index % 40 == 0:
            self.show = not self.show

        if self.show:
            self.win.blit(self.image, self.rect)
        