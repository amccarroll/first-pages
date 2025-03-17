# First Pages

A Django web application that showcases the first pages of classic books from Project Gutenberg. The app displays a random first page from a selection of classic books, allowing users to read the first few pages and then get the full book from Project Gutenberg.

## Features

- Random selection of classic books from Project Gutenberg
- Clean, modern UI with a focus on readability
- First page preview with "Read More" option
- Direct links to full books on Project Gutenberg
- Responsive design that works on all devices

## Setup

1. Clone the repository:
```bash
git clone https://github.com/amccarroll/first-pages.git
cd first-pages
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Fetch books from Project Gutenberg:
```bash
python manage.py fetch_gutenberg --num-books 5 --pages-per-book 5
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Visit http://127.0.0.1:8000/ in your browser

## Usage

1. Click "Get Started" to see a random first page from a classic book
2. Click "Read More" to see the next 4 pages
3. Click "Buy This Book" to get the full book from Project Gutenberg

## Available Books

The app includes a selection of classic books from Project Gutenberg:
- Pride and Prejudice
- The Adventures of Sherlock Holmes
- The Adventures of Tom Sawyer
- The Yellow Wallpaper
- A Modest Proposal
- Alice's Adventures in Wonderland
- Moby Dick
- A Tale of Two Cities
- Dracula
- Frankenstein

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 