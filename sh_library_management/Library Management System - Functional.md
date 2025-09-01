# Library Management System - Functional Requirements

## 1: Author Management

### What the User Needs:
- Maintain a list of all authors
- See author's personal details (use existing contact model)
- Track which books each author has written
- Quick view of how many books each author has published

### Expected Functionality:
1. **Author Profile**: Click on any author to see their complete profile
2. **Book Counter**: Show total number of books written by each author
3. **Book List**: From author's profile, see all books they've written
4. **Search & Filter**: Find authors by name, nationality, or book genre

### Key Requirements:
- Connect authors with existing contact model
- One author can write multiple books
- Multiple authors can collaborate on one book
- Show relationships clearly in the interface

---

## 2: Book Catalog Management

### What the User Needs:
- Maintain complete book inventory
- Track book details (ISBN, category, publication info)
- Know which books are available vs. issued
- Manage book categories for easy organization

### Expected Functionality:
1. **Book Registry**: Master list of all books with search/filter options
2. **Availability Status**: Instantly see if book is available, issued, or lost
3. **Category Management**: Group books by Fiction, Non-fiction, Science, etc.
4. **Publisher Tracking**: Link books to publishing companies (use contact model)
5. **Multi-Author Support**: Handle books with multiple authors

### Business Rules:
- Each book must have unique ISBN
- Books can belong to multiple categories
- Track book condition (New, Good, Damaged)
- Some books might have multiple copies

---

## 3: Member Management

### What the User Needs:
- Register library members
- Track membership status and validity
- Monitor borrowing history and limits
- Handle member communications

### Expected Functionality:
1. **Member Registration**: Use existing contact model, add library-specific fields
2. **Membership Status**: Active, Expired, Suspended members
3. **Borrowing Limits**: Track how many books each member can borrow
4. **History Tracking**: See all books a member has ever borrowed

### Business Rules:
- Members can borrow maximum 3 books simultaneously
- Membership expires annually
- Suspended members cannot borrow books
- Track member contact preferences for notifications

---

## 4: Wizards for Common Operations

### Issue Books Wizard
**Purpose**: Streamline the book issuing process
- Select member from dropdown
- Choose multiple available books
- Set custom due date if needed
- Validate member eligibility

### Return Books Wizard
**Purpose**: Handle book returns efficiently
- Show all active loans for quick selection
- Calculate overdue fines automatically
- Process multiple returns simultaneously
- Update all related records

---

## Module 7: Business Constraints & Validations

### Data Integrity Rules:
1. **ISBN Validation**: Must be 13 digits, unique across all books
2. **Member Limit**: Cannot borrow more than 3 books at a time
3. **Date Logic**: Issue date cannot be in future, due date must be after issue date
4. **Membership Status**: Only active members can borrow books

---