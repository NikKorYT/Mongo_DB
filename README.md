# MongoDB + RabbitMQ Quote Management System

A distributed quote management system that demonstrates MongoDB integration with RabbitMQ message queuing for asynchronous email processing.

## 🚀 Features

- **MongoDB Integration**: Uses MongoEngine ODM for document modeling and database operations
- **Message Queue System**: RabbitMQ implementation for asynchronous user notification processing
- **Data Seeding**: Automated population of quotes and authors from JSON files
- **Interactive Search**: Command-line interface for searching quotes by author, tag, or multiple tags
- **Producer/Consumer Pattern**: Distributed architecture for scalable email processing

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────┐    ┌─────────────────┐
│    MongoDB      │    │   RabbitMQ   │    │   Email Service │
│   (Documents)   │◄──►│   (Queue)    │◄──►│   (Consumer)    │
└─────────────────┘    └──────────────┘    └─────────────────┘
         ▲                       ▲                     ▲
         │                       │                     │
┌─────────────────┐    ┌──────────────┐    ┌─────────────────┐
│    Seeder       │    │   Producer   │    │   Consumer      │
│  (Data Import)  │    │ (User Queue) │    │ (Email Sender)  │
└─────────────────┘    └──────────────┘    └─────────────────┘
```

## 📊 Data Models

### Authors
```python
class authors(Document):
    full_name = StringField(required=True)
    born_date = DateTimeField(required=True)
    born_location = StringField(required=True)
    description = StringField(required=True)
```

### Quotes
```python
class qoutes(Document):
    tags = ListField(StringField())
    author = ReferenceField(authors)  # MongoDB relationship
    quote = StringField(required=True)
```

### Users
```python
class users(Document):
    name = StringField(required=True)
    email = EmailField(required=True)
    message_sent_status = BooleanField(required=True, default=False)
```

## 🛠️ Technologies Used

- **Database**: MongoDB with MongoEngine ODM
- **Message Broker**: RabbitMQ with Pika library
- **Data Generation**: Faker for test data
- **Configuration**: ConfigParser for secure credential management
- **Languages**: Python 3.x

## 📋 Prerequisites

- Python 3.7+
- MongoDB Atlas account (or local MongoDB instance)
- RabbitMQ server
- Required Python packages (see requirements below)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Mongo_DB
   ```

2. **Install dependencies**
   ```bash
   pip install mongoengine pika faker configparser
   ```

3. **Configure database connection**
   
   Copy the example config and add your credentials:
   ```bash
   cp configs/config.ini.example configs/config.ini
   ```
   
   Then edit `configs/config.ini` with your actual MongoDB credentials:
   ```ini
   [DB]
   USER=your_mongodb_username
   PASS=your_mongodb_password
   DOMAIN=your_mongodb_cluster.mongodb.net
   ```

4. **Start RabbitMQ server**
   ```bash
   # Using Docker
   docker run -d --hostname rabbitmq --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
   
   # Or install locally
   # Follow RabbitMQ installation guide for your OS
   ```

## 🚀 Usage

### 1. Seed Database with Sample Data
```bash
python seeds.py
```
This will:
- Clear existing data
- Import authors from `contents/authors.json`
- Import quotes from `contents/qoutes.json`

### 2. Interactive Quote Search
```bash
python request.py
```

**Available commands:**
- `name:Albert Einstein` - Find quotes by author name
- `tag:life` - Find quotes by single tag
- `tags:life,wisdom,success` - Find quotes by multiple tags
- `exit` - Exit the application

### 3. Run Producer (Generate Users & Queue Messages)
```bash
python producer.py
```
This will:
- Generate 20 fake users
- Send user IDs to RabbitMQ queue for processing

### 4. Run Consumer (Process Email Queue)
```bash
python consumer.py
```
This will:
- Listen for user IDs from the queue
- Simulate sending emails to users
- Update user status in MongoDB

## 📁 Project Structure

```
Mongo_DB/
├── configs/
│   ├── config.ini.example  # Template for database configuration
│   └── config.ini          # Your actual config (not in git)
├── contents/
│   ├── authors.json        # Sample authors data
│   └── qoutes.json         # Sample quotes data
├── models.py               # MongoDB document models
├── seeds.py                # Database seeding script
├── request.py              # Interactive search interface
├── producer.py             # Message queue producer
├── consumer.py             # Message queue consumer
├── .gitignore              # Git ignore file
└── README.md               # This file
```

## 🔍 Key Features Demonstrated

### MongoDB Operations
- **Document Modeling**: Complex relationships using ReferenceField
- **CRUD Operations**: Create, read, update operations
- **Query Patterns**: Field matching, array queries, reference lookups
- **Connection Management**: Secure connection with authentication

### RabbitMQ Integration
- **Producer Pattern**: Publishing messages to queues
- **Consumer Pattern**: Processing messages asynchronously
- **Message Durability**: Persistent message delivery
- **Connection Management**: Proper connection handling

### Distributed System Design
- **Separation of Concerns**: Different scripts for different responsibilities
- **Asynchronous Processing**: Non-blocking email notifications
- **Scalability**: Can run multiple consumers for load distribution
- **Fault Tolerance**: Message acknowledgment and error handling

## 🔄 Workflow Example

1. **Data Setup**: Run `seeds.py` to populate quotes and authors
2. **User Generation**: Run `producer.py` to create users and queue notifications
3. **Background Processing**: Run `consumer.py` to process email queue
4. **Interactive Search**: Use `request.py` to search through quotes

## 🧪 Sample Data

The system includes sample data with:
- **Authors**: Famous personalities with biographical information
- **Quotes**: Inspirational quotes tagged by themes
- **Users**: Generated fake users for testing the notification system

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📝 License

This project is part of a learning module demonstrating MongoDB and RabbitMQ integration patterns.

## 📞 Contact

For questions about this implementation, please refer to the repository owner.

---

*This project demonstrates practical implementation of NoSQL databases with message queuing systems, showcasing distributed system architecture and asynchronous processing patterns.*
