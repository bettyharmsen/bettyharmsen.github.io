TITLE="Weather - Betty's Favourite Links"

.PHONY: all

index.html: ../index.py index.csv
	python ../index.py index.csv index.html $(TITLE)

all:
	python ../index.py index.csv index.html $(TITLE)
	make -C aw all
	make -C ec all
	make -C twn all
