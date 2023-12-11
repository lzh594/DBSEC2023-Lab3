import { Book, User, RawToBook, BooksApiRaw } from './models';
import { requestData } from '../api';


export class BookService {
  total: number = 0; // database 中书总数
  private books: Book[] = [];
  private currentPage: number = 1;

  constructor() {
    this.AddBooks()
  }

  // 从 database 拿去新页
  async AddBooks(pageReq: number = 3) {
    for (let i = 0; i < pageReq; i++) {
      try {
        const res = await requestData({
          url: 'books/',
          method: 'get',
          query: {
            page: (this.currentPage + i).toString()
          }
        });
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
  private me!: User;
  constructor(username: string) {
    this.getUser(username);
  }

  async getUser(username: string){
    // 其实应该是静态方法。。
    try {
      const idResponse = await requestData({
        url: 'users/get_id/',
        method: 'get',
        query: { uname: username },
      })
      const id = idResponse?.data.uid;
      const userResponse = await requestData({
        url: `/users/${id}`,
        method: 'get',
        query: { uid: id, }
      })
      this.me = userResponse?.data;
    } catch (error) {
      throw new Error('get user failed')
    }
  }

  async addShoppingCart(bookID: number, amount: number = 1) {
    try {
      await requestData({
        url: 'shoppingcarts/',
        method: 'post',
        query: {
          uid: this.me.id,
          book_id: bookID,
          amount: amount,
        }
      });
    } catch (error) {
      throw new Error('update shopping cart failed')
    }
  }

  async addCollection(bookID: number) {
    try {
      await requestData({
        url: 'collection/',
        method: 'post',
        query: {
          uid: this.me.id,
          book_id: bookID,
        }
      });
    } catch (error) {
      throw new Error('update shopping cart failed')
    }
  }
}