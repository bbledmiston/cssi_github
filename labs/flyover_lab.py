def newYork():
  return "We're leaving New York!"

best_states = ["Pennsylvania", "Ohio", "Illinois"].upper()

def pennsylvania():
  return "We're flying over " + best_states[0] + "!"

def ohio():
  return "We're flying over Pennsylvania!"
print newYork()
print pennsylvania()

def flyOver(state_name_string):
    print "We are flying over " + state_name_string

for state in states:
    flyOver(state.upper())
