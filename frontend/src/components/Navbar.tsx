import React, { useState, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";

const Navbar = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("authToken");
    setIsLoggedIn(!!token);
  }, []);

  const handleLogout = () => {
    localStorage.removeItem("authToken");
    setIsLoggedIn(false);
    navigate("/");
  };

  return (
    <nav className="bg-white p-4 text-black shadow-md">
      <div className="container mx-auto flex justify-between items-center">
        <h1 className="text-2xl text-indigo-700 font-bold">Auth App</h1>
        <div>
          {isLoggedIn ? (
            <button
              onClick={handleLogout}
              className="mr-4 text-red-500 hover:text-red-700"
            >
              Logout
            </button>
          ) : (
            <Link to="/" className="mr-4 hover:text-gray-300">
              Login
            </Link>
          )}
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
