import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="bg-white p-4 text-black  shadow-md">
      <div className="container mx-auto flex justify-evenly items-center">
        <h1 className="text-2xl text-indigo-700 font-bold">Auth App</h1>
        <div>
          <Link to="/" className="mr-4 hover:text-gray-300">
            Login
          </Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
