#Deals with User-Role Management.

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import UserRoleMap # Table 'UserRoleMap' from app.models
from app.database import get_db
import uuid
from pydantic import BaseModel
from fastapi import HTTPException

router = APIRouter()

#used when creating a new user-role.(json object)
#used for incoming data.
class UserRoleCreate(BaseModel):
    user: str
    role: str

#json object
#used for outgoing data.
class UserRoleResponse(BaseModel):
    id: str
    user: str
    role: str

#ADDs a new user-role
@router.post("/user-role", response_model=UserRoleResponse, status_code=201)
def create_user_role(user_role: UserRoleCreate, db: Session = Depends(get_db)):
    """
    TODO: Implement POST /user-role
    - Create new user-role mapping
    - Generate UUID for id
    - Save to user_role_map table
    - Return created mapping
    """
    try:
        # TODO: Create new UserRoleMap instance
        new_user_role = UserRoleMap(user=user_role.user, role=user_role.role)

        # TODO: Add to database and commit
        db.add(new_user_role)
        db.commit()
        db.refresh(new_user_role)

        return UserRoleResponse( #returns json object
            id=str(new_user_role.id),
            user=user_role.user,
            role=user_role.role,
        )
    except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

#Gets all user-role.
#response will be a list of JSON objects.
@router.get("/user-role", response_model=list[UserRoleResponse])
def get_all_user_roles(db: Session = Depends(get_db)):
    """
    TODO: Implement GET /user-role
    - Query all user-role mappings from database
    - Return list of all mappings
    """
    try:
        # TODO: Query all UserRoleMap records
        user_roles = db.query(UserRoleMap).all()
        # TODO: Convert to response format
        #returns json response
        return [UserRoleResponse(
             id=str(ur.id), 
             user=ur.user, 
             role=ur.role) 
             for ur in user_roles]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


