run:
	which python
	python src/entrypoint.py

voice_pipeline:
	python src/voice_pipeline_only.py

test_strategist:
	python src/strategist_test.py