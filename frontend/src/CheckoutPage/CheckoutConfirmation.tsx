import React from 'react';
import { useLocation } from 'react-router-dom';

const ConfirmationPage: React.FC = () => {
    const location = useLocation();
    const { orderStatusResponse } = location.state as any;

    return (
        <div className="container mt-5">
            <h1>Order Confirmation</h1>
            <h2>Order ID: {orderStatusResponse.orderId}</h2>
            <p>Status: {orderStatusResponse.status}</p>
            {orderStatusResponse.suggestedBooks && orderStatusResponse.suggestedBooks.length > 0 &&
                <div>
                    <h3>Suggested Books</h3>
                    <ul>
                        {orderStatusResponse.suggestedBooks.map((book: any, index: number) => (
                            <li key={index}>
                                <h4>{book.title}</h4>
                                <p>Book ID: {book.bookId}<br />
                                Author: {book.author}</p>
                            </li>
                        ))}
                    </ul>
                </div>
            }
        </div>
    );
};

export default ConfirmationPage;
