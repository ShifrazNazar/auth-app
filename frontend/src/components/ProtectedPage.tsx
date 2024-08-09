import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Navbar from "./Navbar";

function ProtectedPage() {
  const navigate = useNavigate();

  useEffect(() => {
    const verifyToken = async () => {
      const token = localStorage.getItem("authToken");

      if (!token) {
        navigate("/");
        return;
      }

      try {
        const response = await fetch(
          `http://localhost:8000/validate_token?token=${token}`
        );

        if (!response.ok) {
          throw new Error("Token verification failed");
        }
      } catch (error) {
        localStorage.removeItem("authToken");
        navigate("/");
      }
    };

    verifyToken();
  }, [navigate]);

  return (
    <div className="min-h-screen bg-gray-100">
      <Navbar />
      <main className="flex flex-col items-center justify-center min-h-screen p-4">
        <div className="bg-white shadow-md rounded-lg p-8 max-w-lg w-full">
          <h2 className="text-4xl font-bold text-gray-800 mb-4">
            Welcome to the Auth App
          </h2>
          <p className="text-lg text-gray-600 mb-4">
            This is a simple authentication application built with React and
            FastAPI.
          </p>
          <p className="text-sm text-gray-500">
            Use the navigation bar to explore the Login and Register pages.
          </p>
        </div>
      </main>
    </div>
  );
}

export default ProtectedPage;
