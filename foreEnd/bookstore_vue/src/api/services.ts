import { Book, User, RawToBook, BooksApiRaw } from './models';
import { reactive } from 'vue';
import { requestData } from '../api';


export class BookService {
  total: number = 0; // database 中书总数
  private books: Book[] = [];
  private currentPage: number = 1;
  private request = reactive({
    url: '',
    method: '',
    query: {}
  })

  constructor() {
    this.request.url = 'books/';
    this.request.method = 'get';
  }

  // 从 database 拿去新页
  async AddBooks(pageReq: number = 3) {
    for (let i = 0; i < pageReq; i++) {
      this.request.query = { page: (this.currentPage + i).toString() };
      try {
        const res = await requestData(this.request);
        const data = RawToBook(res?.data);
        this.books.push(...data.books);
        this.total = data.totalBooks;
        this.currentPage += 1;
      } catch (error) {
        console.error("add books failed", error)
        break;
      }
    }
    this.currentPage += pageReq;
  }

  getBooks(): Book[] {
    return this.books;
  }

  filterBooks(): BookFilter {
    return new BookFilter(this.books);
  }

  sortBooks(): BookSorter {
    return new BookSorter(this.books);
  }
}


class BookFilter {
  private books: Book[];

  constructor(books: Book[]) {
    this.books = books;
  }

  byYear(startYear: number, endYear: number): BookFilter {
    this.books = this.books.filter(book =>
      book.year >= startYear && book.year <= endYear);
    return this;
  }

  byTitle(title: string): BookFilter {
    this.books = this.books.filter(book =>
      book.title.toLowerCase().includes(title.toLowerCase())
    );
    return this;
  }

  byCategory(category: string): BookFilter {
    this.books = this.books.filter(book =>
      book.category.toLowerCase().includes(category.toLowerCase())
    );
    return this;
  }

  byPrice(minPrice: number, maxPrice: number): BookFilter {
    this.books = this.books.filter(book => {
      return book.price >= minPrice && book.price <= maxPrice;
    });
    return this;
  }

  getBooks(): Book[] {
    return this.books;
  }
}


class BookSorter {
  private books: Book[];

  constructor(books: Book[]) {
    this.books = books;
  }

  byPrice(ascending: boolean = true) {
    this.books.sort((a, b) =>
      ascending ? a.price - b.price : b.price - a.price
    );
    return this;
  }

  bySales(ascending: boolean = true) {
    this.books.sort((a, b) =>
      ascending ? a.sales - b.sales : b.sales - a.sales);
    return this;
  }

  byYear(ascending: boolean = true) {
    this.books.sort((a, b) =>
      ascending ? a.year - b.year : b.year - a.year);
    return this;
  }

  getBooks(): Book[] {
    return this.books;
  }
}


export class UserService {
  private user: User;
  private request = reactive({
    url: '',
    method: '',
    query: {}
  })

  constructor(me: User) {
    this.user = me;
  }

  async addShoppingCart(bookID: number, amount: number = 1) {
    this.request.url = 'shoppingcarts/'
    this.request.method = 'post';
    const data = {
      uid: this.user.id,
      book_id: bookID,
      amount: amount,
    }
    this.request.query = data;
    try {
      await requestData(this.request);
    } catch (error) {
      throw new Error('update shopping cart failed')
    }
  }

  async addCollection(bookID: number) {
    this.request.url = 'shoppingcarts/'
    this.request.method = 'post';
    const data = {
      uid: this.user.id,
      book_id: bookID,
    }
    this.request.query = data;
    try {
      await requestData(this.request);
    } catch (error) {
      throw new Error('update shopping cart failed')
    }
  }
}