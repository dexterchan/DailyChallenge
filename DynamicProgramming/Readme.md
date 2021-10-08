

Build
```
docker build -t tictactoe .
```

Run trianing
```
docker run -itd -v /tmp:/tmp tictactoe --training --iteration 100
```

Run interactive
```
docker run -it --rm -v /tmp:/tmp tictactoe
```