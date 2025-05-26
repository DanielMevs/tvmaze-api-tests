# TV Maze API Test Suite

A comprehensive automated test suite for the TV Maze API using Python, Pytest, and Tavern framework.

## 🚀 Quick Start

```bash
# Clone and setup
git clone <repository-url>
cd tvmaze-api-tests

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your configuration

# Run all tests
pytest tests

# Running a specific test file
pytest tests/test_security.tavern.yaml

```

## 📋 Test Coverage

### **Core API Tests**

- **Show Search** - Single search functionality (`singlesearch`)
- **Cast Verification** - Actor presence in show cast (`cast`)
- **Pagination** - Response size limits and pagination (`pagination`)
- **Scheduling** - Show air day validation
- **Link Validation** - URL endpoint accessibility

### **Security Tests**

- **SQL Injection** - Protection against malicious queries (`security`)
- **Error Handling** - Invalid input handling
- **Negative Testing** - Non-existent show searches

## 🛠️ Tech Stack

- **Testing Framework**: Pytest + Tavern
- **API Client**: Requests
- **Reporting**: pytest-html
- **Configuration**: python-dotenv
- **Logging**: Python logging module

## 📁 Project Structure

```
tvmaze-api-tests/
├── tests/                          # Test files
│   ├── test_actor_is_in_cast_for_show.tavern.yaml
│   ├── test_security.tavern.yaml
│   ├── test_show_link_valid.tavern.yaml
│   ├── test_show_pagination.tavern.yaml
│   ├── test_show_scheduled_on_day.tavern.yaml
│   └── test_shows.tavern.yaml
├── utilities/
│   └── utils.py                    # Custom validation functions
├── common.yaml                     # Shared test variables
├── common_security.yaml            # Security test variables
├── conftest.py                     # Pytest configuration & fixtures
├── pytest.ini                     # Pytest settings
└── requirements.txt                # Dependencies
```

## ⚙️ Configuration

### Environment Variables (.env)

```bash
BASE_URL=https://api.tvmaze.com
SQL_INJECTION_QUERY="'; DROP TABLE shows; --"
```

### Test Markers

Run specific test categories:

```bash
pytest tests -m singlesearch    # Single search tests
pytest tests -m cast           # Cast-related tests
pytest tests -m pagination     # Pagination tests
pytest tests -m security       # Security tests
```

## 🔧 Key Features

### **Custom Validation Functions**

```python
# Example: Actor verification with logging
def actor_in_show(response, actor):
    logger.info(f"Searching for actor: {actor}")
    # Implementation details...
```

### **Environment-Based Configuration**

- Flexible base URL configuration
- Separate security test variables
- Environment-specific settings

### **Comprehensive Reporting**

- HTML reports with pytest-html
- Performance timing with custom fixtures
- Structured logging for debugging

### **Professional Test Organization**

- Modular test structure
- Reusable validation functions
- Clear test categorization with markers

## 📊 Running Tests

### **Advanced Options**

```bash

# Parallel execution
pytest -n auto

# Coverage report
pytest --cov=utilities
```

## 🐛 Debugging

### **Logging Output**

Tests include structured logging for debugging:

```
INFO: Loading environment configuration
INFO: Using BASE_URL: https://api.tvmaze.com
INFO: Searching for actor: H. Jon Benjamin
INFO: Actor H. Jon Benjamin found in cast
INFO: Test took 1.23 seconds
```

## 📈 Best Practices Demonstrated

- ✅ **Data-driven testing** with YAML configuration
- ✅ **Separation of concerns** (tests vs validation logic)
- ✅ **Environment-based configuration**
- ✅ **Comprehensive error handling**
- ✅ **Performance monitoring**
- ✅ **Security testing integration**
- ✅ **Professional reporting**

## 🤝 Contributing

1. Follow existing test patterns
2. Add appropriate markers for new tests
3. Update documentation for new features
4. Ensure tests pass locally before submitting

---

**Built for reliability, maintainability, and clear reporting** 🎯
