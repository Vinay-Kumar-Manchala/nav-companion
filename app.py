import uvicorn
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from src.scripts.handler import LogicHandler

app = FastAPI(root_path="/mutual-funds/")


@app.get("/heart", response_class=HTMLResponse)
def read_items():
    return "Lub Dub...Lub Dub...Lub Dub..."


@app.get("/mutual-funds", response_class=HTMLResponse)
def listing_funds():
    temp = LogicHandler().get_list_of_mutual_funds()
    return temp


@app.post("/handle_form")
def fund_subscription(email: str = Form(...),
    mutual_fund: str = Form(...),
    action: str = Form(...)):
    print(email, mutual_fund, action)
    return {"status": "success"}


@app.post("/verify-mail")
def mail_verification():
    ...


@app.get("/validate-mail")
def mail_validation():
    ...


@app.get("/unsubscribe")
def unsubscribe_service():
    ...


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=int("9999"))
