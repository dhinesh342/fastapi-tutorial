from fastapi import APIRouter,Depends,status,Response,HTTPException
from typing import List
from sqlalchemy.orm import Session
from .. import schemas,database,models
from ..services import blog

router=APIRouter(
    prefix="/blog",
    tags=["blogs"]
)
get_db=database.get_db

@router.get("/",response_model=List[schemas.showBlog])
def get_all_blog(db:Session=Depends(get_db)):
    # blogs=db.query(models.Blog).all()
    # blogs=db.query(models.Blog).where(id==1)
    return blog.get_all(db) 

@router.post("/",status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog,db: Session=Depends(get_db)):
    # new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
    # db.add(new_blog)
    # db.commit()
    # db.refresh(new_blog)
    return blog.create(request,db)

@router.get("/{id}",status_code=200,response_model=schemas.showBlog)
def get_blog(id:int,db:Session=Depends(get_db)):
    # blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    # if not blog:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with ID:{id} is not available")
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {"detail":f"Blog with ID:{id} is not available"}
    return blog.getby_id(id,db)


@router.delete("/{id}",status_code=status.HTTP_200_OK)
def delete_blog(id,db:Session=Depends(get_db)):
    # blog=db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
    # if not blog:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id:{id} not found")
    # db.commit()
    return blog.delete(id,db)

@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED)
def update_blog(id:int,request:schemas.Blog,db:Session=Depends(get_db)):
    # return request
    # blog=db.query(models.Blog).filter(models.Blog.id==id)
    # if not blog.first():
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with ID:{id} not found")
    # blog.update(request.dict())
    # db.commit()
    return blog.update(id,request,db)