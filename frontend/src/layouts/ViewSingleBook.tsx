import React, { useEffect, useState} from 'react';
import {Link, useParams, useNavigate} from 'react-router-dom';
import { responseData } from "../Api";

type BookData = {
    id: string;
    title: string;
    author: string;
    description: string;
    copies: number;
    copiesAvailable: number;
    category: string;
    img: string;
    price: number;
};

const ViewSingleBook: React.FC = () => {
    let { bookId } = useParams<{ bookId: string }>();

    const navigate = useNavigate();


    const [book, setBook] = useState<BookData | null>(null);
    const [isLoading, setIsLoading] = useState(true);
    const [httpError, setHttpError] = useState<string | null>(null);
    const [quantityAdjustment, setQuantityAdjustment] = useState(1);

    const formatPrice = (price: number) => {
        return `$${price.toFixed(2)}`;
    };

    const totalAmount = book ? book.price * quantityAdjustment : 0;

    const fetchBooksData = async (): Promise<BookData | null> => {
        return new Promise((resolve) => {
            setTimeout(() => {
                const bookData = Object.values(responseData).find(book => book.id === bookId);
                resolve(bookData ?? null); // Return null if no book is found
            }, 1000);
        });
    };

    const handleCheckout = () => {
        navigate(`/checkout/${book?.id}`, { state: { ...book, totalAmount } });
    };



    useEffect(() => {
        const fetchBook = async () => {
            setIsLoading(true);
            try {
                const fetchedBook = await fetchBooksData();
                setBook(fetchedBook);
            } catch (error) {
                console.log(error);
                setHttpError('An error occurred while fetching data');
            } finally {
                setIsLoading(false);
            }
        };

        fetchBook();
        window.scrollTo(0, 0);
    },[bookId]);

    if (isLoading) {
        return (
            <div className="d-flex justify-content-center align-items-center" style={{ height: '100vh' }}>
                <div className="spinner-border" role="status">
                    <span className="sr-only">Loading...</span>
                </div>
                <p className="ml-3">Loading book details...</p>
            </div>
        );
    }

    // Enhanced Error Handling
    if (httpError) {
        return (
            <div className="container mt-3 alert alert-danger">
                Something went wrong. Please try reloading the page or contact support.
            </div>
        );
    }

    if (!book) {
        return <div className="container mt-3 alert alert-warning">Book not found</div>;
    }

    const availabilityIndicator = book.copiesAvailable > 0 ? 'text-success' : 'text-danger';
    const availabilityText = book.copiesAvailable > 0 ? 'Available' : 'Out of Stock';

    const QuantityAdjustmentUI = () => (
        <div>
            <input
                type="number"
                value={quantityAdjustment}
                onChange={(e) => setQuantityAdjustment(Number(e.target.value))}
                className="form-control mb-2"
                min="1"
                max="10"
            />
        </div>
    );

    // Main Render
    return (
        <div className="container mt-5">
            {/* Breadcrumb Navigation */}
            <nav aria-label="breadcrumb">
                <ol className="breadcrumb">
                    <li className="breadcrumb-item"><Link to="/">Home</Link></li>
                    <li className="breadcrumb-item active" aria-current="page">Book Details</li>
                </ol>
            </nav>

            <div className="row">
                {/* Book Image */}
                <div className="col-md-6">
                    <img src={book?.img} alt={book?.title} className="img-fluid rounded"/>
                </div>


                {/* Book Details */}
                <div className="col-md-6">
                    <h2 className="mb-3">{book?.title}</h2>
                    <p className="lead"><strong>Price:</strong> {formatPrice(book?.price)}</p>
                    <p><strong>Author:</strong> {book?.author}</p>
                    <p><strong>Description:</strong> {book?.description}</p>
                    <p className={availabilityIndicator}><strong>Copies Available:</strong> {book?.copiesAvailable} ({availabilityText})</p>
                    <QuantityAdjustmentUI />
                    <p className="lead"><strong>Price:</strong> {book && formatPrice(book.price)}</p>
                    <p className="total-price mt-2">Total Price: {formatPrice(totalAmount)}</p>
                    <button onClick={handleCheckout} className="btn btn-outline-success btn-lg">
                        Checkout
                    </button>

                </div>
            </div>
        </div>
    );
};

export default ViewSingleBook;
