# # Create a class that encapsulates logic for converting temperatures between Celsius and Fahrenheit, Kelvin . 
# # Use properties with getters and setters to ensure valid temperature values and provide a user-friendly interface.

# class TemperatureConverter:
#     def __init__(self):
#         self._celsius = 0.0

#     @property
#     def celsius(self):
#         return self._celsius

#     @celsius.setter
#     def celsius(self, value):
#         if value < -273.15:
#             raise ValueError("Temperature cannot be below absolute zero in Celsius")
#         self._celsius = value

#     @property
#     def fahrenheit(self):
#         return self._celsius * 9/5 + 32

#     @fahrenheit.setter
#     def fahrenheit(self, value):
#         self.celsius = (value - 32) * 5/9

#     @property
#     def kelvin(self):
#         return self._celsius + 273.15

#     @kelvin.setter
#     def kelvin(self, value):
#         self.celsius = value - 273.15

# # Example usage
# temp_converter = TemperatureConverter()
# temp_converter.celsius = 25
# print(f"Celsius: {temp_converter.celsius}")
# print(f"Fahrenheit: {temp_converter.fahrenheit}")
# print(f"Kelvin: {temp_converter.kelvin}")

# temp_converter.fahrenheit = 77
# print(f"Celsius: {temp_converter.celsius}")
# print(f"Fahrenheit: {temp_converter.fahrenheit}")
# print(f"Kelvin: {temp_converter.kelvin}")

# temp_converter.kelvin = 298.15
# print(f"Celsius: {temp_converter.celsius}")
# print(f"Fahrenheit: {temp_converter.fahrenheit}")
# print(f"Kelvin: {temp_converter.kelvin}")

# ################################################ Alberto ###########################

# class ConvertTemperature:
#     LOWEST_CELSIUS_TEMP = -273.15
#     KELVIN_VALUE = 273.15
#     FAHRENHEIT_VALUE = 32

#     def __init__(self, temp_in_celsius=0.0) -> None:
#         self._temp_in_celsius = temp_in_celsius

#     @property
#     def temp_in_celsius(self) -> float:
#         print("Temperature in Celsius: ")
#         return self._temp_in_celsius

#     @property
#     def celsius_to_fahrenheit(self) -> float:
#         return round(((1.8 * self._temp_in_celsius) + self.FAHRENHEIT_VALUE), 2)

#     @property
#     def celsius_to_kelvin(self) -> float:
#         return round((self._temp_in_celsius + self.KELVIN_VALUE), 2)

#     @temp_in_celsius.setter
#     def temp_in_celsius(self, value):
#         if value > self.LOWEST_CELSIUS_TEMP:
#             print("Setting temperature in Celsius...")
#             self._temp_in_celsius = value
#         else:
#             self._temp_in_celsius = self.LOWEST_CELSIUS_TEMP
#             print(
#                 "Value you've entered is below lowest temperature.\nTemperature has been set to it's lowest."
#             )


# converter = ConvertTemperature()

# print(converter.celsius_to_fahrenheit, converter.celsius_to_kelvin)

# converter.temp_in_celsius = 15.0

# print(converter.celsius_to_fahrenheit, converter.celsius_to_kelvin)

#####################################################################################################
# Create a class that securely stores and manages passwords. 
# Use properties with getters and setters to ensure password security and prevent unauthorized access.

# Requirements:
#  - Define a property named password that sets the password. The setter should:
#  - Enforce a minimum password length (e.g., 8 characters).
#  - Check for common password patterns or dictionary words (optional for an extra challenge).
#  - Hash the password using a secure hashing algorithm (e.g., SHA-256) before storing it.
#  - Create a getter for password that always returns randomly places 8 to 12 elements from hash function  
# (symbols must not be duplicated) to prevent direct access to the actual password.
#  - Create a setter, that would take current password and new one, if current password is correct , would set new one, otherwise raise error.

# import hashlib
# import random

# class PasswordManager:
#     def __init__(self):
#         self._password_hash = None

#     @property
#     def password(self):
#         if self._password_hash:
#             return self._generate_random_password()
#         else:
#             return None

#     def _generate_random_password(self):
#         symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*'
#         password_length = random.randint(8, 12)
#         password_chars = random.sample(symbols, password_length)
#         return ''.join(password_chars)

#     def set_password(self, new_password):
#         if len(new_password) < 8:
#             raise ValueError("Password must be at least 8 characters long.")
        
#         # Additional checks for common patterns or dictionary words can be added here
        
#         self._password_hash = self._hash_password(new_password)

#     def _hash_password(self, password):
#         return hashlib.sha256(password.encode()).hexdigest()

#     def change_password(self, current_password, new_password):
#         if self._password_hash is None:
#             raise ValueError("No password set.")
        
#         if self._password_hash == self._hash_password(current_password):
#             self.set_password(new_password)
#         else:
#             raise ValueError("Incorrect current password.")

# # Example usage
# password_manager = PasswordManager()

# password_manager.set_password("StrongPassword123")

# print(f"Randomly generated password: {password_manager.password}")

# try:
#     password_manager.change_password("StrongPassword123", "NewPassword456")
#     print("Password changed successfully.")
# except ValueError as e:
#     print(f"Error: {e}")

#################################### Alberto ################################

# import hashlib, random
# from dataclasses import dataclass


# @dataclass
# class NewPassword:
#     old_password: str
#     new_password: str


# class WrongPasswordError(Exception):
#     pass


# class Password:
#     MIN_PASSWORD_LENGTH = 6
#     WEAK_PASSWORDS = [
#         "123456",
#         "12345678",
#         "123456789",
#         "12345",
#         "1234567",
#         "password",
#         "abcdef",
#         "abc123",
#         "qwerty",
#         "111111",
#         "1234",
#         "iloveyou",
#     ]

#     def __init__(self, password: str) -> None:
#         self._password = self._validate_password(password)

#     def _validate_password(self, password) -> str:
#         if (
#             len(password) >= self.MIN_PASSWORD_LENGTH
#             and password not in self.WEAK_PASSWORDS
#         ):
#             print("Password meets the requirements.")
#             hashed_password = self._hash_password(password=password)
#             return hashed_password
#         else:
#             return "Weak password"

#     @staticmethod
#     def _hash_password(password) -> str:
#         password_bytes = password.encode("utf-8")
#         hash_object = hashlib.sha256(password_bytes)
#         return hash_object.hexdigest()

#     def get_scrambled_hash(self) -> str:
#         hash_list = []
#         while len(hash_list) < random.randint(8, 12):
#             x = self._password[random.randrange(64)]
#             if x not in hash_list:
#                 hash_list.append(x)
#         scrambled_hash = "".join(hash_list)
#         return scrambled_hash

#     @property
#     def password(self) -> str:
#         return self.get_scrambled_hash()

#     @password.setter
#     def password(self, new_password: "NewPassword") -> None:
#         compare_hash = self._hash_password(password=new_password.old_password)
#         if compare_hash == self._password:
#             self._password = self._validate_password(new_password.new_password)
#             print("New password has been set")
#         else:
#             raise WrongPasswordError("Wrong password")


# passw = Password("passwordas")

# print(passw.password)

# new_password = NewPassword(old_password="passwordas", new_password="blablablabal")

# try:
#     passw.password = new_password
# except WrongPasswordError as err:
#     print(err)

# print(passw.password)



