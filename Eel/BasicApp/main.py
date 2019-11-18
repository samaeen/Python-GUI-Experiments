import eel
eel.init('web')
eel.start('main.html', mode='chrome', cmdline_args=['--start-fullscreen', '--browser-startup-dialog'])