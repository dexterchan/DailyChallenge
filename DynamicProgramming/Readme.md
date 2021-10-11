
TEST
```
export PYTHONPATH=.
python3 tests/tictactoe/test_ai.py
```

Build
```
docker build -t tictactoe .
```

Run trianing
```
docker run -itd -v /tmp:/tmp tictactoe --training --iteration 100
docker run -itd -v /tmp:/tmp tictactoe --training --learning 0.0001 --min_probability 0.5 --iteration 1000000
```

Run interactive
```
docker run -it --rm -v /tmp:/tmp tictactoe
```

Run training with s3
```
#!/bin/sh
export statistic_file=<s3 file path>
docker run -itd -v /tmp:/tmp \
	-v ${HOME}/.aws/credentials:/home/appuser/credentials \
	tictactoe --training --learning 0.0001 --min_probability 0.5 --iteration 1000000 \
	--statisticfile ${statistic_file}
```