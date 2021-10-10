
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
docker run -itd -v /tmp:/tmp tictactoe --training --learning 0.0001 --min_probaility 0.5 --iteration 1000000
```

Run interactive
```
docker run -it --rm -v /tmp:/tmp tictactoe
```