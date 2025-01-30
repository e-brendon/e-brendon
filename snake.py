# snake.py
import argparse

def generate_snake(output_file):
    snake_svg = """
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400">
        <text x="10" y="20" font-size="16" fill="black">GitHub Snake Animation</text>
        <rect x="10" y="30" width="780" height="360" fill="lightgreen" stroke="green" />
        <circle cx="50" cy="50" r="10" fill="blue" />
        <circle cx="70" cy="50" r="10" fill="red" />
        <circle cx="90" cy="50" r="10" fill="yellow" />
    </svg>
    """
    with open(output_file, "w") as file:
        file.write(snake_svg)
    print(f"Snake animation generated at {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate GitHub Snake animation")
    parser.add_argument("--output", default="github-contribution-grid-snake.svg", help="Output SVG file")
    args = parser.parse_args()
    generate_snake(args.output)
