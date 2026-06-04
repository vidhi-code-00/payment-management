@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    # Check email already exists or not
    check_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if check_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    # Hash password
    hashed_password = pwd.hash(user.password)

    # Create new user
    new_user = User(
        name=user.name,
        email=user.email,
        password=hashed_password,
        role=user.role
    )

    # Save in database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User Registered Successfully",
        "user": {
            "name": new_user.name,
            "email": new_user.email,
            "role": new_user.role
        }
    }