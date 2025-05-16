from django.db import models

from Backend import settings


# Create your models here.

# -- Borrowed (history) table
# CREATE TABLE Borrowed (
#     borrowed_id INT IDENTITY(1,1) PRIMARY KEY,
#     book_id INT NOT NULL,
#     user_id INT NOT NULL,
#     borrow_date DATE NOT NULL,
#     CONSTRAINT FK_Borrowed_Books FOREIGN KEY (book_id) REFERENCES Books(book_id) ON DELETE CASCADE,
#     CONSTRAINT FK_Borrowed_Users FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
# );
#
# -- Borrow counter table
# CREATE TABLE BorrowCounter (
#     book_id INT PRIMARY KEY,
#     borrow_count INT NOT NULL DEFAULT 0,
#     CONSTRAINT FK_BorrowCounter_Books FOREIGN KEY (book_id) REFERENCES Books(book_id) ON DELETE CASCADE
# );
#
# GO
# CREATE TRIGGER trg_UpdateBorrowCounter
# ON Borrowed
# AFTER INSERT
# AS
# BEGIN
#     -- Update existing counter
#     UPDATE bc
#     SET bc.borrow_count = bc.borrow_count + 1
#     FROM BorrowCounter bc
#     JOIN inserted i ON bc.book_id = i.book_id;
#
#     -- Insert new counter rows
#     INSERT INTO BorrowCounter (book_id, borrow_count)
#     SELECT i.book_id, 1
#     FROM inserted i
#     WHERE NOT EXISTS (
#         SELECT 1
#         FROM BorrowCounter bc
#         WHERE bc.book_id = i.book_id
#     );
# END;
# GO

