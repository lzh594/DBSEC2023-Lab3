export interface Book {
  id: number;
  title: string;
  author: string;
  publisher: string;
  category: string;
  year: number;
  isbn: string;
  price: number;
  sales: number;
  url: string;
  rate: number;
}

export interface BooksApiRaw {
  count: number;
  next: string | null;
  preivous: string | null;
  results: any[];
}

export interface User{
  id: number;
  name: string;
  pwdhash: string;
  email: string;
  tel: string;
}

export function RawToBook(res: BooksApiRaw): { books: Book[], totalBooks: number, next: string | null } {
    const books = res.results.map(item => 
      ({
        id: item.book_id,
        author: item.author.aname,
        category: item.category.category_name,
        publisher: item.publisher.pname,
        title: item.bname,
        year: item.pub_year,
        url: item.url,
        isbn: item.isbn,
        sales: item.sales,
        price: parseFloat(item.price),
        rate: parseFloat(item.rate)
      } as Book));

    return {
      books,
      totalBooks: res.count,
      next: res.next
    };
  }
