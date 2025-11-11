try:
    import firebase_admin
    from firebase_admin import credentials, db

    cred = credentials.Certificate("firebase/serviceAccountKey.json")

    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred, {
            "databaseURL": "https://temp-477617-default-rtdb.firebaseio.com/"
        })

    realtime_db = db
except ModuleNotFoundError:
    
    import warnings

    warnings.warn(
        "firebase_admin not installed: realtime_db will be a stub returning empty data",
        ImportWarning,
    )

    class _StubRef:
        def __init__(self, path):
            self.path = path

        def get(self):
            # Return empty mapping to indicate no data in the stub environment.
            return {}

    class _StubDB:
        def reference(self, path):
            return _StubRef(path)

    realtime_db = _StubDB()
