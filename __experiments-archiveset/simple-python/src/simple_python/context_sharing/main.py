import a_pack.aaa1
import a_pack.aaa2
import b_pack.bbb1
import b_pack.bbb2
from context.box import lazy
print("main.py")
print(lazy.check())
lazy.parse()
print(lazy.check())
lazy.inject()
print(lazy.check())
print(lazy.size())


