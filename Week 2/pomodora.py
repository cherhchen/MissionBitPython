import rumps

# TODO: Implement all the TODOs.
# The functions `start_button_clicked`, `stop_button_clicked`, and `continue_button_clicked` are
# called when their respective buttons are clicked in the application menu. Meanwhile, the function
# `every_second` is called once every second continuously.
# Tip: Use `rumps.notification(<title>, <subtitle>, <message>)` to send a notification.

is_timer_running = False
seconds_remaining = 0
title = '🍅'

def start_button_clicked():
  '''This method is called when the "Start New Timer" button is clicked.'''
  global is_timer_running, seconds_remaining
  # TODO: Uncomment the lines below and fill them in.
  is_timer_running = True
  seconds_remaining = 5
  rumps.notification('Pomodoro Timer', '', 'The timer has started.')
  print('start_button_clicked')

def stop_button_clicked():
  '''This method is called when the "Stop Timer" button is clicked.'''
  global is_timer_running, seconds_remaining
  # TODO: Uncomment the lines below and fill them in.
  is_timer_running = False
  rumps.notification('Pomodoro Timer', '', 'The timer has stopped.')
  print('stop_button_clicked')

def continue_button_clicked():
  '''This method is called when the "Continue Timer" button is clicked.'''
  global is_timer_running, seconds_remaining
  # TODO: Uncomment the lines below and fill them in.
  is_timer_running = True
  rumps.notification('Pomodoro Timer', '', 'The timer has resumed.')
  print('continue_button_clicked')

def every_second():
  '''This method is called once every second.'''
  global is_timer_running, seconds_remaining, title

  # TODO: Fill this in. Depending on `is_timer_running`, decrement `seconds_remaining` accordingly.
  # Use `title = <new title>` to display the number of seconds remaining. If `seconds_remaining` has
  # reached zero, reset `is_timer_running` and notify the user that they should take a break :)
  # BONUS: Display the time remaining in the format "Xm Ys", such as "24m 30s". 
  # NOTE: For this BONUS part, we need to learn about integer division, but the application will still run without it! It is written with two slashes ("//") and divides only in whole numbers and throws out the remainder. Sort of like the opposite of modulo.

  if is_timer_running == True:
    seconds_remaining -= 1
    minutes = seconds_remaining // 60
    seconds = seconds_remaining % 60
    title = str(minutes) + 'm ' + str(seconds) + 's'
    print(title)
    if seconds_remaining == 0:
      is_timer_running = False
      rumps.notification('Pomodoro Time', '', 'You should take a break :)')
  

################################ DO NOT MODIFY CODE BELOW THIS LINE ################################

class PomodoroTimer(rumps.App):
  def __init__(self): super(PomodoroTimer, self).__init__(title)

  @rumps.clicked('Start New Timer')
  def start_timer(self, _): start_button_clicked()

  @rumps.clicked('Continue Timer')
  def continue_timer(self, _): continue_button_clicked()

  @rumps.clicked('Stop Timer')
  def stop_timer(self, _): stop_button_clicked()

  @rumps.timer(1)
  def tick(self, _):
    global title
    every_second()
    self.title = title

if __name__ == "__main__":
  PomodoroTimer().run()