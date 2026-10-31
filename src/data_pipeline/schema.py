from datetime import date
from decimal import Decimal
from pydantic import BaseModel, Field, ConfigDict

class LineItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    
    product_id: int | None = Field(None, description="ID of the product")
    product_name: str | None = Field(None, description="Name of the product")
    quantity: int | None = Field(None, description="Quantity of the product")
    unit_price: Decimal | None = Field(None, description="Per unit price, no currency symbol")
    line_total: Decimal | None = Field(None, description="Total for this line")
    
class Invoice(BaseModel):
    model_config = ConfigDict(extra="forbid")
    
    order_id: int | None = Field(None, description="ID of the order")
    order_date: date | None = Field(None, description="Date of the invoice")
    customer: str | None = Field(None, description="Customer name")
    line_items: list[LineItem] = Field(default_factory=list)
    total: Decimal | None = Field(None, description="Invoice total")