from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from moviepy.editor import VideoFileClip


class VideoProcessorApp(App):
    def build(self):
        self.selected_video = None

        layout = BoxLayout(orientation='vertical')

        # File chooser to select the video
        file_chooser = FileChooserListView()
        file_chooser.bind(on_selection=self.on_file_selected)
        layout.add_widget(file_chooser)

        # Button to start processing
        self.process_button = Button(text='Start Processing', disabled=True)
        self.process_button.bind(on_press=self.start_processing)
        layout.add_widget(self.process_button)

        return layout

    def on_file_selected(self, instance, selection):
        if selection:
            self.selected_video = selection[0]
            self.process_button.disabled = False
        else:
            self.selected_video = None
            self.process_button.disabled = True

    def start_processing(self, instance):
        if self.selected_video:
            video = VideoFileClip(self.selected_video)
            duration = video.duration
            video.close()
            popup = Popup(title='Video Information',
                          content=Label(text=f'Selected video duration: {duration} seconds'),
                          size_hint=(None, None), size=(400, 200))
            popup.open()
        else:
            popup = Popup(title='Error',
                          content=Label(text='Please select a video first!'),
                          size_hint=(None, None), size=(300, 200))
            popup.open()


if __name__ == '__main__':
    VideoProcessorApp().run()
