PYTHON ?= python3

.PHONY: run test clean

run:
	$(PYTHON) -m src.main config.txt

test:
	$(PYTHON) -m unittest discover -s tests -v

clean:
	rm -f output/maze.txt
