import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import CreateUser from "./components/User-Management/create_user";
import DeleteUser from "./components/User-Management/delete_user";
import GetUser from "./components/User-Management/get_user";
import GetUsers from "./components/User-Management/get_users";
import UpdateUser from "./components/User-Management/update_user";

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/create-user" element={<CreateUser />} />
                <Route path="/delete-user" element={<DeleteUser />} />
                <Route path="/get-user" element={<GetUser />} />
                <Route path="/get-users" element={<GetUsers />} />
                <Route path="/update-user" element={<UpdateUser />} />
            </Routes>
        </Router>
    );
}

export default App;
