test:
	pytest -v -p no:logging --reruns 3 --no-print-logs tests/

show_cases:
	python -m pytest --collect-only

run_test:
	echo "before tests"
	source $$HOME/miniconda/bin/activate; \
	conda activate skillbox_22; \
	pytest
	conda deactivate; \
	echo "after tests"
