import { User } from '../models/User';

export const dummy_users:User[] = [
  { _id: 700,
    email: "bobdylan@gmail.com",
    first_name: "Bob",
    last_name: "Dylan",
    role_id: 0,
    phone: "1-347-1234",
    address: "123 Baker Street",
    public: true,
    password: "abc123"
  },
  { _id: 701,
    email: "mickjagger@gmail.com",
    first_name: "Mick",
    last_name: "Jagger",
    role_id: 1,
    phone: "1-347-9001",
    address: "456 Baker Street",
    public: true,
    password: "abc123"
  },
  { _id: 702,
    email: "johnsmit@gmail.com",
    first_name: "John",
    last_name: "Smith",
    role_id: 1,
    phone: "1-347-0091",
    address: "789 Baker Street",
    public: true,
    password: "abc123"
  },
];