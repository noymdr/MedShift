import os
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from supabase import create_client, Client
from functools import lru_cache

# Supabase configuration
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://jztbkzkirpwexldjhzps.supabase.co")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")

print(f"=== DEBUG: Supabase Config ===")
print(f"SUPABASE_URL: {SUPABASE_URL}")
print(f"SUPABASE_ANON_KEY: {SUPABASE_ANON_KEY[:20]}..." if SUPABASE_ANON_KEY else "None")

bearer_scheme = HTTPBearer()

@lru_cache()
def get_supabase_client() -> Client:
    print(f"=== DEBUG: Creating Supabase client ===")
    client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)
    print(f"Supabase client created successfully")
    return client

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    print(f"=== DEBUG: get_current_user called ===")
    token = credentials.credentials
    print(f"Token: {token[:50]}...")
    
    try:
        print(f"Getting Supabase client...")
        supabase = get_supabase_client()
        
        print(f"Calling supabase.auth.get_user...")
        print(f"Token: {token}")
        user_response = supabase.auth.get_user(token)
        print(f"User response: {user_response}")
        
        if hasattr(user_response, 'user'):
            user = user_response.user
            print(f"User object: {user}")
            return user
        else:
            print(f"Unexpected response structure: {user_response}")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid user response")
            
    except Exception as e:
        print(f"Error in get_current_user: {e}")
        print(f"Error type: {type(e)}")
        import traceback
        print(f"Traceback: {traceback.format_exc()}")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid token: {str(e)}")

def require_role(role: str):
    def dependency(user=Depends(get_current_user)):
        print(f"=== DEBUG: Role Check ===")
        print(f"User: {user}")
        print(f"Required role: {role}")
        
        if hasattr(user, 'app_metadata'):
            user_role = user.app_metadata.get("role")
        else:
            print(f"User object doesn't have app_metadata attribute")
            user_role = None
            
        print(f"User role: {user_role}")
        
        if user_role != role:
            print(f"❌ Role mismatch: {user_role} != {role}")
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient permissions")
        else:
            print(f"✅ Role match: {user_role} == {role}")
        return user
    return dependency