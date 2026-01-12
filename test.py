# body 클래스 생성
class Body:
  def __init__(self, content):
    self.content = content
    
# body 생성
a = Body("공미남")
# 출력
print(a.content)

print(dir(a))