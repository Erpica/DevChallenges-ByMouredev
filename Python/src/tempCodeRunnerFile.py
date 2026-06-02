class Session_Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Session_Singleton, cls).__new__(cls)
        return cls._instance

session_singleton11 = Session_Singleton
session_singleton11 = Session_Singleton()
print("\n",session_singleton11)