from Learning.state import LessonState

state = LessonState()

state.total_steps = 10
state.current_step = 4

print("Progress:", state.progress)