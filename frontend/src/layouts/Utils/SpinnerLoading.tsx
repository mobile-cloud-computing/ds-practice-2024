import React from "react";

export const SpinnerLoading = () => {
    return (
        <div className="d-flex justify-content-center align-items-center" style={{ height: '100vh' }}>
            <div className="spinner-border" role="status">
                <span className="sr-only">Loading...</span>
            </div>
            <p className="ml-3">Loading book details...</p>
        </div>
    );
}