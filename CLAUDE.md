# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Korean-language console quiz game (movie trivia, 4-choice questions) built as a class assignment. Requirements live in `mission_2.md`; the step-by-step implementation plan (class design, commit plan) is in `PLAN.md`.

## Running

```bash
python main.py
```

Python 3.10+, standard library only — do not add external dependencies. There are no tests or linters. The game is interactive (menu-driven `input()` loop); to exercise it non-interactively, pipe menu selections to stdin (e.g. `printf '3\n5\n' | python main.py`).

`state.json` is written via a relative path (`STATE_FILE` in `quiz_game.py`), so always run from the repo root.

## Architecture

Three small modules with a strict layering:

- `quiz.py` — `Quiz` class: one question with 4 choices and a 1-based `answer` index, plus `to_dict()`/`from_dict()` for JSON serialization and `default_quizzes()` (the fallback data set).
- `quiz_game.py` — `QuizGame` class: the menu loop (`run()`), all five menu features, and persistence (`load_state()`/`save_state()` against `state.json`).
- `main.py` — entry point; catches `KeyboardInterrupt`/`EOFError` and calls `save_state()` so Ctrl+C/EOF never loses data.

Conventions the code relies on:

- **All user input goes through `read_int()`/`read_text()`** in `QuizGame` (strip whitespace, reject empty/non-numeric/out-of-range, re-prompt). Never call raw `input()` for new features.
- **Persistence is defensive**: missing `state.json` → start with `default_quizzes()`; corrupted file → reset to defaults and re-save. `save_state()` is called after every mutation and on exit, always with `encoding="utf-8"` and `ensure_ascii=False`. Schema is documented in README.md.
- Answer numbers are **1-based** (1–4) everywhere: in `Quiz.answer`, user input, and `state.json`.
- All user-facing text, comments, and docstrings are in Korean.

## Commits

Messages follow `Type: 설명` in Korean, with types `Feat`, `Fix`, `Refactor`, `Docs`, `Init`, `Merge` — one feature-sized change per commit (see `git log` for examples).
