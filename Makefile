TITLE="Betty's Favourite Links"

.PHONY: all

index.html: index.py index.csv
	python index.py index.csv index.html $(TITLE)

all:
	python index.py index.csv index.html $(TITLE)
	make -C art all
	make -C banking all
	make -C birds all
	make -C cooking all
	make -C entertainment all
	make -C family all
	make -C games all
	make -C gardening all
	make -C genealogy all
	make -C holland all
	make -C local all
	make -C news all
	make -C pictures all
	make -C psychic all
	make -C search all
	make -C shopping all
	make -C weather all
