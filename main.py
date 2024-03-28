# TODO сделать class и вызывать остюда объекты: стнция, перегон, МАП, тоннель, хар-ки реле и транс, быстрый поиск)

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
import subprocess


def exit_app(instance):
    App.get_running_app().stop()


class MainApp(App):
    def build(self):
        # Устанавливаем размеры окна приложения равными размерам экрана
        Window.size = (Window.width, Window.height)

        # Создаем менеджер экранов
        self.sm = ScreenManager()

        # Создаем экран "MainScreen"
        main_screen = Screen(name='main')

        # Создаем контейнер для главного окна с вертикальной ориентацией
        main_layout = BoxLayout(orientation='vertical')

        # Создаем фоновый слой
        background_layout = FloatLayout()

        # Создаем прямоугольный виджет с серым цветом
        background = Button(background_color=(0.9, 0.8, 0.6, 1))

        # Настройка размеров прямоугольного виджета, чтобы он занимал всё доступное пространство
        background.bind(size=background.setter('size'), pos=background.setter('pos'))

        # Добавляем фоновый прямоугольник на фоновый слой
        background_layout.add_widget(background)

        # Создаем главный контейнер с вертикальной ориентацией
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20, size_hint=(None, None), size=(400, 400))

        # Устанавливаем выравнивание по центру по обеим осям
        layout.bind(minimum_size=layout.setter('size'))
        layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        # Создаем кнопку "СТАНЦИЯ" и добавляем её в контейнер
        button_station = Button(text='СТАНЦИЯ', size_hint=(None, None), size=(200, 50), background_color=(1, 1, 0, 1))
        button_station.bind(on_press=self.on_station_press)
        layout.add_widget(button_station)

        # Создаем кнопку "ПЕРЕГОН" и добавляем её в контейнер
        button_peregon = Button(text='ПЕРЕГОН', size_hint=(None, None), size=(200, 50), background_color=(1, 1, 0, 1))
        button_peregon.bind(on_press=self.on_peregon_press)
        layout.add_widget(button_peregon)

        # Создаем кнопку "МАП" и добавляем её в контейнер
        button_MAP = Button(text='МАП', size_hint=(None, None), size=(200, 50), background_color=(1, 1, 0, 1))
        button_MAP.bind(on_press=self.on_MAP_press)
        layout.add_widget(button_MAP)

        # Создаем кнопку "тоннели" и добавляем её в контейнер
        button_tonnel = Button(text='ТОННЕЛИ', size_hint=(None, None), size=(200, 50), background_color=(1, 1, 0, 1))
        button_tonnel.bind(on_press=self.on_tonnel_press)
        layout.add_widget(button_tonnel)

        # Создаем остальные кнопки и добавляем их в контейнер
        buttons = ['АППАРАТУРА', 'БЫСТРЫЙ ПОИСК']
        for button_text in buttons:
            # Создаем кнопку с указанным размером и цветом
            button = Button(text=button_text, size_hint=(None, None), size=(200, 50), background_color=(1, 1, 0, 1))
            layout.add_widget(button)

        button_exit = Button(text='ВЫХОД', size_hint=(None, None), size=(200, 50), background_color=(1, 1, 0, 1))
        button_exit.bind(on_press=exit_app)
        layout.add_widget(button_exit)

        # Добавляем главный контейнер на фоновый слой
        background_layout.add_widget(layout)

        # Добавляем фоновый слой на экран "MainScreen"
        main_screen.add_widget(background_layout)

        # Добавляем экран "MainScreen" в менеджер экранов
        self.sm.add_widget(main_screen)

        return self.sm

    def on_station_press(self, instance):
        # Создаем новый экран "SecondScreen"
        second_screen = Screen(name='second')

        # Создаем контейнер для экрана с вертикальной ориентацией
        layout = BoxLayout(orientation='vertical')

        # Создаем кнопку "ТЫЯ" и добавляем её в контейнер
        button_tyia = Button(text='ТЫЯ', size_hint=(None, None), size=(200, 50),
                             pos_hint={'center_x': 0.5, 'center_y': 0.5}, background_color=(1, 1, 0, 1))
        button_tyia.bind(on_press=self.on_tyia_press)
        layout.add_widget(button_tyia)

        # Создаем кнопку "ГОУДЖЕКИТ" и добавляем её в контейнер
        button_goud = Button(text='ГОУДЖЕКИТ', size_hint=(None, None), size=(200, 50),
                             pos_hint={'center_x': 0.5, 'center_y': 0.5}, background_color=(1, 1, 0, 1))
        button_goud.bind(on_press=self.on_goud_press)
        layout.add_widget(button_goud)

        # Создаем кнопку "Дабан" и добавляем её в контейнер
        button_daban = Button(text='ДАБАН', size_hint=(None, None), size=(200, 50),
                              pos_hint={'center_x': 0.5, 'center_y': 0.5}, background_color=(1, 1, 0, 1))
        button_daban.bind(on_press=self.on_daban_press)
        layout.add_widget(button_daban)

        # Создаем кнопку "НАЗАД" и добавляем её в контейнер
        button_back = Button(text='НАЗАД', size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'y': 0},
                             background_color=(1, 1, 0, 1))
        button_back.bind(on_press=self.on_back_press)
        layout.add_widget(button_back)

        # Добавляем контейнер на экран "SecondScreen"
        second_screen.add_widget(layout)

        # Добавляем экран "SecondScreen" в менеджер экранов
        self.sm.add_widget(second_screen)

        # Переключаемся на экран "SecondScreen"
        self.sm.current = 'second'

        # включаем передачу от main до станций

    def on_tyia_press(self, instance):
        subprocess.run(["python", 'station/tyia.py'])

    def on_goud_press(self, instance):
        subprocess.run(["python", 'station/goud.py'])

    def on_daban_press(self, instance):
        subprocess.run(["python", 'station/daban.py'])

    def on_back_press(self, instance):
        # Переключаемся на экран "MainScreen"
        self.sm.current = 'main'

    def on_peregon_press(self, instance):
        # Создаем новый экран "ThirdScreen"
        third_screen = Screen(name='third')

        # Создаем контейнер для экрана с вертикальной ориентацией
        layout = BoxLayout(orientation='vertical')

        # Создаем кнопку "Дабан-Дельбичинда 1 путь" и добавляем её в контейнер
        button_daban_delb_1_put = Button(text='Дабан-Дельбичинда 1 путь', size_hint=(None, None), size=(200, 50),
                                         pos_hint={'center_x': 0.5, 'center_y': 0.5}, background_color=(1, 1, 0, 1))
        button_daban_delb_1_put.bind(on_press=self.on_daban_delb_1_put_press)
        layout.add_widget(button_daban_delb_1_put)

        # Создаем кнопку "Дабан-Дельбичинда 2 путь" и добавляем её в контейнер
        button_daban_delb_2_put = Button(text='Дабан-Дельбичинда 2 путь', size_hint=(None, None), size=(200, 50),
                                         pos_hint={'center_x': 0.5, 'center_y': 0.5}, background_color=(1, 1, 0, 1))
        button_daban_delb_2_put.bind(on_press=self.on_daban_delb_2_put_press)
        layout.add_widget(button_daban_delb_2_put)

        # Создаем кнопку "Дабан-Гоуджекит 1 путь" и добавляем её в контейнер
        button_daban_goud_1_put = Button(text='Дабан-Гоуджекит 1 путь', size_hint=(None, None), size=(200, 50),
                                         pos_hint={'center_x': 0.5, 'center_y': 0.5}, background_color=(1, 1, 0, 1))
        button_daban_goud_1_put.bind(on_press=self.on_daban_goud_1_put_press)
        layout.add_widget(button_daban_goud_1_put)

        # Создаем кнопку "Дабан-Гоуджекит 2 путь" и добавляем её в контейнер
        button_daban_goud_2_put = Button(text='Дабан-Гоуджекит 2 путь', size_hint=(None, None), size=(200, 50),
                                         pos_hint={'center_x': 0.5, 'center_y': 0.5}, background_color=(1, 1, 0, 1))
        button_daban_goud_2_put.bind(on_press=self.on_daban_goud_2_put_press)
        layout.add_widget(button_daban_goud_2_put)

        # Создаем кнопку "Гоуджекит-Тыя 1 путь" и добавляем её в контейнер
        button_goud_tyia_1_put = Button(text='Гоуджекит-Тыя 1 путь', size_hint=(None, None), size=(200, 50),
                                        pos_hint={'center_x': 0.5, 'center_y': 0.5}, background_color=(1, 1, 0, 1))
        button_goud_tyia_1_put.bind(on_press=self.on_goud_tyia_1_put_press)
        layout.add_widget(button_goud_tyia_1_put)

        # Создаем кнопку "Гоуджекит-Тыя 2 путь" и добавляем её в контейнер
        button_goud_tyia_2_put = Button(text='Гоуджекит-Тыя 2 путь', size_hint=(None, None), size=(200, 50),
                                        pos_hint={'center_x': 0.5, 'center_y': 0.5}, background_color=(1, 1, 0, 1))
        button_goud_tyia_2_put.bind(on_press=self.on_goud_tyia_2_put_press)
        layout.add_widget(button_goud_tyia_2_put)

        # Создаем кнопку "Тыя-пп1053 1 путь" и добавляем её в контейнер
        button_tyia_pp1053_1_put = Button(text='Тыя-пп 1053км 1 путь', size_hint=(None, None), size=(200, 50),
                                          pos_hint={'center_x': 0.5, 'center_y': 0.5}, background_color=(1, 1, 0, 1))
        button_tyia_pp1053_1_put.bind(on_press=self.on_tyia_pp1053_1_put_press)
        layout.add_widget(button_tyia_pp1053_1_put)

        # Создаем кнопку "Тыя-пп1053 2 путь" и добавляем её в контейнер
        button_tyia_pp1053_2_put = Button(text='Тыя-пп 1053км 2 путь', size_hint=(None, None), size=(200, 50),
                                          pos_hint={'center_x': 0.5, 'center_y': 0.5}, background_color=(1, 1, 0, 1))
        button_tyia_pp1053_2_put.bind(on_press=self.on_tyia_pp1053_2_put_press)
        layout.add_widget(button_tyia_pp1053_2_put)

        # Создаем кнопку "НАЗАД" и добавляем её в контейнер
        button_back = Button(text='НАЗАД', size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'y': 0},
                             background_color=(1, 1, 0, 1))
        button_back.bind(on_press=self.on_back_press)
        layout.add_widget(button_back)

        # Добавляем контейнер на экран "ThirdScreen"
        third_screen.add_widget(layout)

        # Добавляем экран "ThirdScreen" в менеджер экранов
        self.sm.add_widget(third_screen)

        # Переключаемся на экран "ThirdScreen"
        self.sm.current = 'third'

    # включаем передачу от main до перегонов
    def on_daban_delb_1_put_press(self, instance):
        subprocess.run(["python", 'peregony/daban_delb_1_put.py'])

    def on_daban_delb_2_put_press(self, instance):
        subprocess.run(["python", 'peregony/daban_delb_2_put.py'])

    def on_daban_goud_1_put_press(self, instance):
        subprocess.run(["python", 'peregony/daban_goud_1_put.py'])

    def on_daban_goud_2_put_press(self, instance):
        subprocess.run(["python", 'peregony/daban_goud_2_put.py'])

    def on_goud_tyia_1_put_press(self, instance):
        subprocess.run(["python", 'peregony/goud_tyia_1_put.py'])

    def on_goud_tyia_2_put_press(self, instance):
        subprocess.run(["python", 'peregony/goud_tyia_2_put.py'])

    def on_tyia_pp1053_1_put_press(self, instance):
        subprocess.run(["python", 'peregony/tyia_pp1053_1_put.py'])

    def on_tyia_pp1053_2_put_press(self, instance):
        subprocess.run(["python", 'peregony/tyia_pp1053_2_put.py'])

    def on_MAP_press(self, instance):
        # Создаем новый экран "FourthScreen"
        fourth_screen = Screen(name='fourth')

        # Создаем контейнер для экрана с вертикальной ориентацией
        layout = BoxLayout(orientation='vertical')

        # Создаем кнопку "1047км" и добавляем её в контейнер
        button_1047km = Button(text='переезд 1047 км', size_hint=(None, None), size=(200, 50),
                               pos_hint={'center_x': 0.5, 'center_y': 0.5}, background_color=(1, 1, 0, 1))
        button_1047km.bind(on_press=self.on_1047km_press)
        layout.add_widget(button_1047km)

        # Создаем кнопку "1026 км" и добавляем её в контейнер
        button_1026km = Button(text='переезд 1026 км', size_hint=(None, None), size=(200, 50),
                               pos_hint={'center_x': 0.5, 'center_y': 0.5}, background_color=(1, 1, 0, 1))
        button_1026km.bind(on_press=self.on_1026km_press)
        layout.add_widget(button_1026km)

        # Создаем кнопку "НАЗАД" и добавляем её в контейнер
        button_back = Button(text='НАЗАД', size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'y': 0},
                             background_color=(1, 1, 0, 1))
        button_back.bind(on_press=self.on_back_press)
        layout.add_widget(button_back)

        # Добавляем контейнер на экран "FourthScreen"
        fourth_screen.add_widget(layout)

        # Добавляем экран "FourthScreen" в менеджер экранов
        self.sm.add_widget(fourth_screen)

        # Переключаемся на экран "FourthScreen"
        self.sm.current = 'fourth'

        # включаем передачу от main до переездов

    def on_1026km_press(self, instance):
        subprocess.run(["python", 'MAP/1026km.py'])

    def on_1047km_press(self, instance):
        subprocess.run(["python", 'MAP/1047km.py'])



    def on_tonnel_press(self, instance):
        # Создаем новый экран "FifthScreen"
        fifth_screen = Screen(name='fifth')

        # Создаем контейнер для экрана с вертикальной ориентацией
        layout = BoxLayout(orientation='vertical')

        # Создаем кнопку "тоннель 1 путь" и добавляем её в контейнер
        button_1_put = Button(text='тоннель 1 путь', size_hint=(None, None), size=(200, 50),
                              pos_hint={'center_x': 0.5, 'center_y': 0.5}, background_color=(1, 1, 0, 1))
        button_1_put.bind(on_press=self.on_1_put_press)
        layout.add_widget(button_1_put)

        # Создаем кнопку "тоннель 2 путь" и добавляем её в контейнер
        button_2_put = Button(text='тоннель 2 путь', size_hint=(None, None), size=(200, 50),
                              pos_hint={'center_x': 0.5, 'center_y': 0.5}, background_color=(1, 1, 0, 1))
        button_2_put.bind(on_press=self.on_2_put_press)
        layout.add_widget(button_2_put)

        # Создаем кнопку "НАЗАД" и добавляем её в контейнер
        button_back = Button(text='НАЗАД', size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'y': 0},
                             background_color=(1, 1, 0, 1))
        button_back.bind(on_press=self.on_back_press)
        layout.add_widget(button_back)

        # Добавляем контейнер на экран "FifthScreen"
        fifth_screen.add_widget(layout)

        # Добавляем экран "FifthScreen" в менеджер экранов
        self.sm.add_widget(fifth_screen)

        # Переключаемся на экран "FifthScreen"
        self.sm.current = 'fifth'

        # включаем передачу от main до тоннелей

    def on_1_put_press(self, instance):
        subprocess.run(["python", 'tonnel/1_put.py'])



    def on_2_put_press(self, instance):
        subprocess.run(["python", 'tonnel/2_put.py'])


if __name__ == '__main__':
    MainApp().run()
