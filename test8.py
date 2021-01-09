def decorator(func):
   def wrapper(*args):
      print("Function Wrapper executed")
      return func(*args)
   return wrapper


class A:
  def __init__(self,a,b):
      self.a=a
      self.b=b

  def __str__(self):
      return f"{self.a} and {self.b}"

  def __call__(self,func):
      def wrapper(*args):
          print("Class wrapper executed")
          print(self)
          return func(*args)
      return wrapper

@A(6,5)
@decorator
def func(*args):
    print(args)

if __name__=="__main__":
   func(5,6,7,8)

