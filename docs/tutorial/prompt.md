When you need to ask the user for info interactively you should normally use <a href="https://typer.tiangolo.com/tutorial/options/prompt/" target="_blank">*CLI Option*s with Prompt</a>, because they allow using the CLI program in a non-interactive way (for example, a Bash script could use it).

But if you absolutely need to ask for interactive information without using a *CLI option*, you can use `typer.prompt()`:

```Python hl_lines="5"
{!./src/prompt/tutorial001.py!}
```

Check it:

<div class="termy">

```console
$ python main.py

# What's your name?:$ Camila

Hello Camila
```

</div>

## Confirm

There's also an alternative to ask for confirmation. Again, if possible, you should use a <a href="https://typer.tiangolo.com/tutorial/options/prompt/" target="_blank">*CLI Option* with a confirmation prompt</a>:

```Python hl_lines="5"
{!./src/prompt/tutorial002.py!}
```

Check it:

<div class="termy">

```console
$ python main.py

# Are you sure you want to delete it? [y/N]:$ y

Deleting it!

// This time cancel it
$ python main.py

# Are you sure you want to delete it? [y/N]:$ n

Not deleting
Aborted!
```

</div>

## Confirm or abort

As it's very common to abort if the user doesn't confirm, there's an integrated parameter `abort` that does it automatically:

```Python hl_lines="5"
{!./src/prompt/tutorial003.py!}
```

<div class="termy">

```console
$ python main.py

# Are you sure you want to delete it? [y/N]:$ y

Deleting it!

// This time cancel it
$ python main.py

# Are you sure you want to delete it? [y/N]:$ n

Aborted!
```

</div>
