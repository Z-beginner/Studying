import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        #self.bg_color = (230, 230, 230) #R G B
        #上述已被self.settings.bg_color替代
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)) #创建游戏窗口
        pygame.display.set_caption("Alien Invasion") #设置窗口标题
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group() #创建一个对象用于装sprite

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()
            self.clock.tick(60)  # tick:跳动一次，限制不超过60帧，给循环限速

    def _check_events(self): #check前的_表示仅供类内部调用
        for event in pygame.event.get():  # 获取玩家产生的所有事件
            if event.type == pygame.QUIT:  # 玩家退出
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)  # 填充屏幕
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()  # 更新屏幕


if __name__ == "__main__": #打开python直接运行游戏
    ai = AlienInvasion()
    ai.run_game()