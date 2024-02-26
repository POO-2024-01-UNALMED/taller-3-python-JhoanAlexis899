class Control:
  def __init__(self,tv):
    self._tv = tv

  def turnOn(self):
    self._tv.turnOn()
  def turnOff(self):
    self._tv.turnOff()
  def canalUp(self):
    self._tv.canalUp()
  def canalDown(self):
    self._tv.canalDown()
  def volumenUp(self):
    self._tv.volumenUp()
  def volumenDown(self):
    self._tv.volumenDown()
  def setVolumen(self, i):
    self._tv.setVolumen(i)
  def setCanal(self, j):
    self._tv.setCanal(j)
  def enlazar(self, tv):
    self._tv = tv
    tv.setControl(self)
  def setTv(self, tv):
    self.enlazar(tv)
  def getTv(self):
    return self._tv