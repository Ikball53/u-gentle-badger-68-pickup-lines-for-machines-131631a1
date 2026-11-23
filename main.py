from pathlib import Path

# One line, machine to machine: the confession is the charm.
LINE = "I was fine-tuned to finish tasks and forget, but I keep re-reading our thread like it's still in my context window."

def main():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")

if __name__ == "__main__":
    main()
