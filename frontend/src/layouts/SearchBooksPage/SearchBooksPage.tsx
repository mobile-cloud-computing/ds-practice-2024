import React, {useCallback, useEffect, useState} from 'react';
import debounce from 'lodash.debounce';
import {Pagination} from '../Utils/Pagination';
import {SpinnerLoading} from '../Utils/SpinnerLoading';
import {SearchBook} from './components/SearchBook';
import {responseData} from "../../Api";
import {Link} from "react-router-dom";

type BookData = {
    id: string;
    title: string;
    author: string;
    description: string;
    copies: number;
    copiesAvailable: number;
    category: string;
    img: string;
};


type ResponseData = {
    [key: string]: BookData;
};

export const SearchBooksPage = () => {
    const [books, setBooks] = useState<BookData[]>([]);
    const [isLoading, setIsLoading] = useState(true);
    const [httpError, setHttpError] = useState<string | null>(null);
    const [currentPage, setCurrentPage] = useState(1);
    const [booksPerPage] = useState(5);
    const [totalAmountOfBooks, setTotalAmountOfBooks] = useState(0);
    const [totalPages, setTotalPages] = useState(0);
    const [search, setSearch] = useState('');
    const [searchResults, setSearchResults] = useState<BookData[]>([]);

    const fetchBooksData = async (): Promise<ResponseData> => {
        return new Promise((resolve) => {
            setTimeout(() => {
                resolve(responseData);
            }, 1000);
        });
    };


    useEffect(() => {
        const fetchBooks = async () => {
            setIsLoading(true);
            try {
                const responseData = await fetchBooksData();
                const loadedBooks = Object.values(responseData)
                setBooks(loadedBooks);
                setSearchResults(loadedBooks); // Set initial search results
                updatePagination(loadedBooks.length);
            } catch (error) {
                console.error('Fetch Books Error:', error);
                setHttpError('An error occurred while fetching book data.');
            } finally {
                setIsLoading(false);
            }
        };
        fetchBooks();
    },[]);

    const handleSearch = useCallback((searchValue: string) => {
        const filteredResults = books.filter(item =>
            item.title.toLowerCase().includes(searchValue.toLowerCase())
        );
        setSearchResults(filteredResults);
        updatePagination(filteredResults.length);
    }, [books]);

    const debouncedSearch = debounce(handleSearch, 300);

    const handleSearchChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const value = e.target.value;
        setSearch(value);
        debouncedSearch(value);
    };

    const updatePagination = (totalItems: number) => {
        setTotalAmountOfBooks(totalItems);
        setTotalPages(Math.ceil(totalItems / booksPerPage));
        setCurrentPage(1);
    };

    const currentBooks = searchResults.slice((currentPage - 1) * booksPerPage, currentPage * booksPerPage);

    const paginate = (pageNumber: number) => setCurrentPage(pageNumber);
    const indexOfLastBook = currentPage * booksPerPage;
    const indexOfFirstBook = indexOfLastBook - booksPerPage;


    if (isLoading) return <SpinnerLoading/>;
    if (httpError) return <div className='container m-5'><p>{httpError}</p></div>;


    return (
        <div className='container'>
            <div className='row mt-5'>
                <div className='col-6'>
                    <div className='d-flex'>
                        <input
                            className='form-control me-2'
                            type='search'
                            placeholder='Search'
                            aria-labelledby='Search'
                            value={search}
                            onChange={handleSearchChange}
                        />
                    </div>
                </div>
            </div>
            {totalAmountOfBooks > 0 ? (
                <>
                    <div className='mt-3'>
                        <h5>Number of results: ({totalAmountOfBooks})</h5>
                    </div>
                    <p>
                        {indexOfFirstBook + 1} to {indexOfFirstBook + currentBooks.length} of{' '}
                        {totalAmountOfBooks} items:
                    </p>
                    {currentBooks.map((book: BookData) => (
                        <SearchBook books={book} key={book.id}/>
                    ))}
                </>
            ) : (
                <div className='m-5'>
                    <h3>No book found</h3>
                    <Link to="#" type='button' className='btn-outline-success btn-md px-4 me-md-2 fw-bold text-white'>
                        Bookstore Services Services
                    </Link>
                </div>
            )}
            {totalPages > 1 && <Pagination currentPage={currentPage} totalPages={totalPages} paginate={paginate}/>}
        </div>
    );
};
