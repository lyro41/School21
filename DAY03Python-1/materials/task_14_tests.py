from task14 import Calculator


def test_init():
	c = Calculator()
	assert bool(c.history(1)) == False, "history не пуста"
	assert bool(c.last) == False, "last не пустое"

def test_sum():
	c = Calculator()
	assert c.sum(1, 2) == 3, "сумма считается неверно"
	assert c.last == "sum(1, 2) == 3", "при сложении не записался last"
	assert c.history(1) == "sum(1, 2) == 3", "неправильная запись в history"

def test_sub():
	c = Calculator()
	assert c.sub(1, 2) == -1, "разность считается неверно"
	assert c.last == "sub(1, 2) == -1", "при вычитании не записался last"
	assert c.history(1) == "sub(1, 2) == -1", "неправильная запись в history"

def test_mul():
	c = Calculator()
	assert c.mul(3, 2) == 6, "произведение считается неверно"
	assert c.last == "mul(3, 2) == 6", "при произведении не записался last"
	assert c.history(1) == "mul(3, 2) == 6", "неправильная запись в history"

def test_div():
	c = Calculator()
	assert c.div(3, 2) == 1.5, "деление считается неверно"
	assert c.last == "div(3, 2) == 1.5", "при делении не записался last"
	assert c.history(1) == "div(3, 2) == 1.5", "неправильная запись в history"

def test_mod():
	c = Calculator()
	assert c.div(3, 2, True) == 1, "деление с остатком считается неверно"
	assert c.last == "div(3, 2) == 1", "при делении с остатком не записался last"
	assert c.history(1) == "div(3, 2) == 1", "неправильная запись в history"

def test_history():
	c = Calculator()
	c1 = Calculator()
	c.sum(1, 2)
	assert c.last == "sum(1, 2) == 3", "при сложении не записался last"
	c1.sum(5, 5)
	assert c.history(1) == "sum(1, 2) == 3", f"неправильная запись в history: {c.history(1)}"
	c.sum(3, 4)
	assert c.last == "sum(3, 4) == 7", "при сложении не записался last"
	c1.sub(6, 3)
	assert c.history(2) == "sum(1, 2) == 3", f"неправильная запись в history(2): {c.history(2)}"
	assert c.history(1) == "sum(3, 4) == 7", f"неправильная запись в history(1): {c.history(1)}"
	c.sub(5, 5)
	assert c.last == "sub(5, 5) == 0", "не записался last"
	c1.mul(543, 55)
	assert c.history(3) == "sum(1, 2) == 3", f"неправильная запись в history(3): {c.history(3)}"
	assert c.history(2) == "sum(3, 4) == 7", f"неправильная запись в history(2): {c.history(2)}"
	assert c.history(1) == "sub(5, 5) == 0", f"неправильная запись в history(1): {c.history(1)}"
	c.mul(-1, 6)
	assert c.last == "mul(-1, 6) == -6", "не записался last"
	c1.div(54, 3)
	assert c.history(4) == "sum(1, 2) == 3", f"неправильная запись в history(4): {c.history(4)}"
	assert c.history(3) == "sum(3, 4) == 7", f"неправильная запись в history(3): {c.history(3)}"
	assert c.history(2) == "sub(5, 5) == 0", f"неправильная запись в history(2): {c.history(2)}"
	assert c.history(1) == "mul(-1, 6) == -6", f"неправильная запись в history(1): {c.history(1)}"

def test_last():
	c1 = Calculator()
	c2 = Calculator()
	c1.sum(1, 2)
	assert c1.last == "sum(1, 2) == 3", "при сложении не записался last"
	assert c2.last == "sum(1, 2) == 3", "при сложении не записался last"
	assert c1.last is c2.last, "last не ссылается на один и тот же объект"
	c2.mul(35, 100)
	assert c1.last == "mul(35, 100) == 3500", "при вычитании не записался last"
	assert c2.last == "mul(35, 100) == 3500", "при вычитании не записался last"
	assert c1.last is c2.last, "last не ссылается на один и тот же объект"
	assert c1.history(1) != c2.history(1), "history разных калькуляторов совпадают"
	c1.clear()
	assert c1.last is None, "clear не задает значение None в last"
	assert c2.last is None, "clear не задает значение None в last"
	assert c1.last is c2.last, "last не ссылается на один и тот же объект"


test_init()
test_sum()
test_sub()
test_mul()
test_div()
test_mod()
test_history()
test_last()
