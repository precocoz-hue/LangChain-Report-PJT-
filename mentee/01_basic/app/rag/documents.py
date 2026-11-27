"""B-06: 실제 VIEW 원문을 LangChain Document와 Metadata로 보존."""
from langchain_core.documents import Document
from app.services.errors import ServiceError

def to_document(row):
    # TODO B-06: Document의 page_content에는 row[content]를, metadata에는 source_id=RPT-번호, report_id/title/category_code/revision/overview/distance를 넣으세요.
    return Document(page_content=row['content'],
                    metadata={'source_id':f"RPT-{row['report_id']}",
                              'report_id':row['report_id'],
                              'title':row['title'],
                              'category_code':row['category_code'],
                              'revision':row['revision'],
                              'overview':row['overview'],
                              'distance':float(row['distance'])})
    # END TODO B-06

def source_of(doc):
    return {k:doc.metadata[k] for k in ('source_id','report_id','title','category_code','revision')}


"""B-06: 실제 VIEW 원문을 LangChain Document와 Metadata로 보존."""
from langchain_core.documents import Document

def to_document(row):
    # BEGIN B-06
    return Document(page_content=row['content'],metadata={
        'source_id':f"RPT-{row['report_id']}",'report_id':row['report_id'],
        'title':row['title'],'category_code':row['category_code'],'revision':row['revision'],
        'overview':row['overview'],'distance':float(row['distance'])})
    # END B-06

def source_of(doc):
    return {k:doc.metadata[k] for k in ('source_id','report_id','title','category_code','revision')}
