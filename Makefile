project=xxx
all:
	python project_builder.py $(project)

clean:
	rm $(project) -rf

check:
	cd $(project) &&\
	autoreconf -if &&\
	./configure --enable-tests &&\
	make all check
