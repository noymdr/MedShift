from supabase import create_client, Client

url = "https://jztbkzkirpwexldjhzps.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imp6dGJremtpcnB3ZXhsZGpoenBzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTQyMDYwNDksImV4cCI6MjA2OTc4MjA0OX0.S9KRPzyIP19ri1WJn_yOmUhSCqvairAIcZl6L2bcXhQ"
supabase: Client = create_client(url, key)

user = supabase.auth.sign_in_with_password({
    "email": "noy@medshift.com",
    "password": "admin1234!"
})
print(user.session.access_token)