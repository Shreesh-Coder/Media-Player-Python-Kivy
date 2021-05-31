from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.videoplayer import VideoPlayer

class MainLayout(BoxLayout):
    video_player = ObjectProperty(None)
    files = ObjectProperty()
    ok = ObjectProperty()

    filechoose = FileChooserListView()

    filename = [""]
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)

    def open_file_chooser(self):
        self.add_widget(self.filechoose)
        self.files.disabled = True
        self.ok.disabled = False

    def on_selection(self):
        self.filename = self.filechoose.selection
        self.files.disabled = False
        self.ok.disabled = True
        print(self.filename)
        self.video_player.source = self.filename[0]
        self.video_player.volume = 1
        self.video_player.state = "play"
        self.remove_widget(self.filechoose)





class MediaApp(App):
    def build(self):
        return MainLayout()

MediaApp().run()