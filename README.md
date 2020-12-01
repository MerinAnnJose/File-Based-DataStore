# File-Based-DataStore
A file-based key-value datastore with basic (CRUD - CREATE, READ, UPDATE, DELETE) operations.


FEATURES:
1. It can be initialized using an optional file path. If one is not provided, it will reliably
create itself in a reasonable location on the laptop.

2. A new key-value pair can be added to the data store using the Create operation. The key
is always a string - capped at 32chars. The value is always a JSON object - capped at
16KB.(NOTE: Here the user can specify the number of attributes they want to add along with their 
corresponding values, which will then be converted into a JSON object.)

3. If Create is invoked for an existing key, an appropriate error must be returned.

4. A Read operation on a key can be performed by providing the key, and receiving the
value in response, as a JSON object.

5. A Delete operation can be performed by providing the key.

6. Every key supports setting a Time-To-Live property when it is created. This property is
optional. If provided, it will be evaluated as an integer defining the number of seconds
the key must be retained in the data store. Once the Time-To-Live for a key has expired,
the key will no longer be available for Read or Delete operations.

7. It'll also be ensured that the size of the file storing data never exceeds 1GB.

LANGUAGE USED:
Python





