#Setting up variables
BulletPerson = pygame.mixer.Sound('Bullet(hit).mp3')
BulletOther = pygame.mixer.Sound('Bullet(miss).mp3')
Shooting = pygame.mixer.Sound('Gunshot.wav')
Walking = pygame.mixer.Sound('Walking.wav')

#Playing any sound/music we want to play throughout the whole game
pygame.mixer.music.load('NAME OF FILE.mp3')
pygame.mixer.music.play(-1)


#When Player Shoots
if keys[pygame.K_SPACE]:
    Shooting.play()

#When Player Walks
if player1.move:
    Walking.play()

#When Bullet hits Player
if pygame.sprite.spritecollideany(bullet, player):
    BulletPerson.play()
    
#When Bullet hits Enemy
if pygame.sprite.spritecollideany(bullet, enemy):
    BulletPerson.play()

#When Bullet hits Platform/ Wall/ Ground
if pygame.sprite.spritecollideany(bullet, platform):
    BulletOther.play()


#Continuous sound/music stops when he dies
if Dead == True:
    pygame.mixer.music.stop()
