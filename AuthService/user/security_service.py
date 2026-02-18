import bcrypt


class PasswordEncoder:
    @staticmethod
    def hash(password):
        salt = bcrypt.gensalt()
        hash_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hash_password.decode('utf-8')

    @staticmethod
    def equals(password, hash_password):
        try:
            return bcrypt.checkpw(password.encode('utf-8'),
                                  hash_password.encode('utf-8'))
        except Exception:
            return False

