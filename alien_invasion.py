import pygame

from pygame.sprite import Group
from settings import Settings 
from ship import Ship
import game_functions as gf 



def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption('Alien Invasion')

	#创建一条飞船
	ship = Ship(ai_settings,screen)

	#创建一个用于存储子弹的编组
	bullets = Group()


	# 开始游戏主循环
	while True:

		#监控键盘鼠标
		gf.check_events(ai_settings,screen,ship,bullets) # 直接用模块调用函数
		ship.update()
		gf.update_bullets(bullets)
	
		gf.update_screen(ai_settings,screen,ship,bullets)
                

		#让最近绘制的屏幕可见
		pygame.display.flip()

run_game()