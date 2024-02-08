import { Link } from "react-router-dom";

export const Heros = () => {

    return (
        <div>
            <div className='d-none d-lg-block'>
                <div className='row g-0 mt-5'>
                    <div className='col-sm-6 col-md-6'>
                        <div className='col-image-left'></div>
                    </div>
                    <div className='col-4 col-md-4 container d-flex justify-content-center align-items-center'>
                        <div className='ml-2'>
                            <h1>Ignite Your Imagination with Our Bestsellers!</h1>
                            <p className='lead'>
                                We believe there's a book for every reader and a reader for every book.
                                Our shelves are brimming with tales that transport you to other worlds,
                                ideas that challenge your perceptions, and narratives that tug at your heartstrings
                            </p>
                                <Link type='button' className='btn btn-outline-success' to='/search'>
                                    Explore books</Link>
                        </div>
                    </div>
                </div>
                <div className='row g-0'>
                    <div className='col-4 col-md-4 container d-flex 
                        justify-content-center align-items-center'>
                        <div className='ml-2'>
                            <h1>Every Book Holds a Secret. Unlock Yours Today!</h1>
                            <p className='lead'>
                                At [Your Bookstore's Name], every visit is an adventure, every book a new friend waiting to be met.
                                We're more than just a bookstore; we're a community of dreamers, thinkers, and storytellers.
                            </p>
                        </div>
                    </div>
                    <div className='col-sm-6 col-md-6'>
                        <div className='col-image-right'></div>
                    </div>
                </div>
            </div>

            {/* Mobile Heros */}
            <div className='d-lg-none'>
                <div className='container'>
                    <div className='m-2'>
                        <div className='col-image-left'></div>
                        <div className='mt-2'>
                            <h1>What have you been reading?</h1>
                            <p className='lead'>
                                The library team would love to know what you have been reading.
                                Whether it is to learn a new skill or grow within one,
                                we will be able to provide the top content for you!
                            </p>
                                <Link type='button' className='btn main-color btn-lg text-white'
                                    to='search'>Explore top books</Link>
                        </div>
                    </div>
                    <div className='m-2'>
                        <div className='col-image-right'></div>
                        <div className='mt-2'>
                            <h1>Our collection is always changing!</h1>
                            <p className='lead'>
                                Try to check in daily as our collection is always changing! 
                                We work nonstop to provide the most accurate book selection possible 
                                for our Luv 2 Read students! We are diligent about our book selection 
                                and our books are always going to be our 
                                top priority.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}