def cough_dec(func):

  def func_wrapper(*args, **kwargs):
    #code before function
    print('cough')

    #function
    func(*args, **kwargs)

    #code after function
    print('cough')

  return func_wrapper

@cough_dec
def question():
  print('can you give me a discount on that?')

@cough_dec
def answer(reply):
  print(reply)

question()
answer('not really, I am sorry!')
