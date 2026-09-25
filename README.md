# LIA Tracker

A small Python command-line script made to help keep track of LIA applications.

The idea is to make it easier to see:

- how many companies you have applied to
- which companies you are still waiting for
- which applications were rejected
- how many days you have been waiting
- which companies may need a follow-up

You can also add new applications directly from the terminal.

## Run the tracker

```bash
python3 tracker.py
```

## Add a new application

```bash
python3 tracker.py add
```

## applications.example.csv

The real `applications.csv` file is private and is ignored by Git.

To try the project, copy the example file:

```bash
cp applications.example.csv applications.csv
```

Then you can edit `applications.csv` manually or add new applications with:

```bash
python3 tracker.py add
```

## Coming soon

The next goal is to automate the tracker so it runs automatically when the computer starts or when the user logs in.

This way, the current LIA application status and follow-ups can be shown without manually starting the script every time.       
