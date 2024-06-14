import React, { useEffect, useState } from "react";
import { getUsers } from "../api";

interface User {
  id: number;
  name: string;
  email: string;
  role: {
    id: number;
    name: string;
  };
}

const UserList: React.FC = () => {
  const [users, setUsers] = useState<User[]>([]);

  useEffect(() => {
    const fetchUsers = async () => {
      const usersData = await getUsers();
      setUsers(usersData);
    };

    fetchUsers();
  }, []);

  return (
    <div>
      <h2>User List</h2>
      <ul>
        {users.map((user) => (
          <li key={user.id}>
            {user.name} ({user.email}) - {user.role.name}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default UserList;
