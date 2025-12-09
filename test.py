import firebase_admin
from firebase_admin import credentials, db

# Use your service account JSON file
cred = credentials.Certificate('soiled-a16a4-firebase-adminsdk-fbsvc-e98466361b.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://soiled-a16a4-default-rtdb.asia-southeast1.firebasedatabase.app'
})

# Push test data
sensor_ref = db.reference('sensor_data')
sensor_ref.set({
    'soil_percent': [65, 70, 68, 72],
    'soil_status': 'MOIST',
    'pump_status': 'OFF',
    'mode': 'AUTO',
    'temperature': 28.5,
    'humidity': 75.2,
    'battery_voltage': 12.4,
    'battery_percent': 85,
    'current_consumed': 0.5,
    'timestamp': '2025-05-28T10:30:00'
})

print("✅ Test data pushed to Firebase!")