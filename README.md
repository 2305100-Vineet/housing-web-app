# SAP SD — Order-to-Cash (O2C) Capstone Project

---

## Student Details

| Field | Details |
|-------|---------|
| **Name** | Vineet Kumar Jha |
| **Roll Number** | 2305100 |
| **Program** | B.Tech — Computer Science Engineering |
| **Course** | SAP Data / Analytics Engineer |
| **University** | Kalinga Institute of Industrial Technology (KIIT) |

---

## Project Title

**Order-to-Cash (O2C) Process Flow in SAP SD**

An end-to-end implementation of the complete O2C sales cycle using SAP Sales & Distribution (SD), integrated with SAP Materials Management (MM), Financial Accounting (FI), and Warehouse Management (WM).

---

## 📁 Repository Structure

```
2305100_project/
│
├── 2305100_Vineet_O2C_Capstone_Project_Report.pdf
├── README.md
├── References.md
├── O2C_Process_Flow_Diagram.png
│
└── Screenshots/
    ├── XD01_Customer_Master.png
    ├── MM01_Material_Master.png
    ├── VA01_Sales_Order.png
    ├── CO09_ATP_Check.png
    ├── VL01N_Delivery.png
    └── VF01_Billing.png
```

---

## Company Blueprint

**Fictitious Company:** VKJ Trading Co. Pvt. Ltd.

| Organizational Element | Configured Value |
|------------------------|-----------------|
| Company Code | VKJ1 — VKJ Trading Co. Pvt. Ltd. |
| Sales Organization | 1000 — VKJ Sales India |
| Distribution Channel | 10 — Direct Sales |
| Division | 00 — Cross-Division |
| Plant | 1000 — VKJ Main Plant, Bhubaneswar |
| Shipping Point | SHP1 — Central Dispatch Hub |
| Storage Location | 0001 — Main Warehouse |

---

## O2C Process Flow

```
  XD01 / MM01          VA11 / VA21             VA01                CO09
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Customer &  │────▶│  Inquiry &   │────▶│ Sales Order  │────▶│ ATP / Avail. │
│   Material   │     │  Quotation   │     │  Creation    │     │    Check     │
│    Master    │     │              │     │              │     │              │
└──────────────┘     └──────────────┘     └──────────────┘     └──────┬───────┘
                                                                        │
                                                                        ▼
                                                  VF01 / F-28     VL01N / VL02N
                                              ┌──────────────┐  ┌──────────────┐
                                              │  Billing &   │◀─│  Outbound    │
                                              │   Payment    │  │  Delivery +  │
                                              │              │  │     PGI      │
                                              └──────────────┘  └──────────────┘
```

---

## Step-by-Step Implementation

### Step 1 — Customer Master `XD01`

Stores customer address, payment terms, reconciliation account (FI), and sales area data. Mandatory before any sales document can be created. Ensures every customer transaction is linked to the correct FI reconciliation account for automatic AR postings.

### Step 2 — Material Master `MM01`

Captures product data across SD, MM, and MRP views. The Sales Org. view defines the delivering plant and item category group. The MRP view governs replenishment logic and planned delivery time.

### Step 3 — Inquiry & Quotation `VA11` / `VA21`

A customer Inquiry captures product interest without commitment. The system generates a formal Quotation with agreed pricing and validity period, which is directly referenced when creating the Sales Order — maintaining full document traceability.

### Step 4 — Sales Order Creation `VA01`

The central O2C document (document type: OR). Captures sold-to/ship-to party, line items, pricing conditions, payment terms, and incoterms. All downstream documents (delivery, invoice) are created with reference to the Sales Order, forming a complete auditable document chain.

### Step 5 — Availability Check / ATP `CO09`

SAP automatically runs Available-to-Promise (ATP) logic at order save — checking stock against confirmed demands (purchase orders, reservations, deliveries) to commit a reliable delivery date. Prevents overselling and sets accurate customer expectations.

### Step 6 — Outbound Delivery `VL01N` / `VL02N`

Delivery document triggers warehouse picking and packing. Post Goods Issue (PGI) simultaneously reduces inventory in MM and auto-posts Cost of Goods Sold (COGS) in FI — no manual entry needed. Also unlocks the billing due list for invoice creation.

### Step 7 — Billing & Payment `VF01` / `F-28`

VF01 generates the customer invoice, posting Accounts Receivable (Dr) and Revenue (Cr) simultaneously in FI. The output determination framework auto-generates the invoice PDF. Payment received via F-28 clears the open AR item, completing the O2C cycle.

> Complete document chain: **Inquiry → Quotation → Sales Order → Delivery → PGI → Invoice → Payment** — permanently linked and auditable in SAP.

---

## Tech Stack

| Module | Full Name | Role in O2C |
|--------|-----------|-------------|
| SAP SD | Sales & Distribution | Core module — Inquiry, Quotation, Sales Order, Delivery, Billing |
| SAP MM | Materials Management | Material Master, inventory management, ATP stock data, Goods Issue |
| SAP FI | Financial Accounting | Customer reconciliation, A/R posting, revenue recognition, payment clearing |
| SAP WM | Warehouse Management | Transfer orders, picking confirmation, storage bin management |

---

## Key Transaction Codes

| T-Code | Description | Module |
|--------|-------------|--------|
| XD01 | Create Customer Master | SD / FI |
| MM01 | Create Material Master | MM |
| VA11 | Create Inquiry | SD |
| VA21 | Create Quotation | SD |
| VA01 | Create Sales Order | SD |
| CO09 | Availability Overview (ATP) | SD / MM |
| VL01N | Create Outbound Delivery | SD / WM |
| VL02N | Post Goods Issue | SD / MM / FI |
| VF01 | Create Billing Document | SD / FI |
| F-28 | Incoming Payment | FI |

---

## Unique Points / Key Features

**Business Value**
- Real-time stock visibility via ATP prevents overselling and stockouts
- Automated credit limit check reduces bad debt exposure significantly
- Single source of truth eliminates data mismatches across departments
- Faster billing cycle shortens Days Sales Outstanding (DSO) and improves cash flow
- Full document trail ensures audit readiness and regulatory compliance

**Technical Differentiation**
- ATP logic integrates SD + MM in real time for reliable delivery commitment
- PGI triggers automatic COGS recognition — no manual FI entry needed
- Output determination framework auto-generates and emails invoice PDFs
- Pricing condition technique supports complex discounts and surcharge rules
- BAPI/IDOC interfaces enable seamless integration with external e-commerce platforms

---

## Future Improvements

| Enhancement | Description |
|-------------|-------------|
| SAP S/4HANA Migration | Leverage Fiori UI and in-memory HANA for real-time order analytics and sub-second processing |
| EDI / IDOC Integration | Automated order and invoice exchange with customer systems using EDIFACT/X12 |
| SAP Analytics Cloud | Live O2C dashboards tracking order backlog, delivery performance, and DSO KPIs |
| ML-Based ATP Forecasting | Predictive availability using SAP IBP demand forecasting integrated with ATP engine |
| Collections Automation | Dunning letters and collection workflows via SAP Collections Management |

---

## Financial Accounting Flow

```
POST GOODS ISSUE (VL02N)
    Debit  →  Cost of Goods Sold (COGS)      (Expense recognized)
    Credit →  Inventory Account              (Stock reduced)

BILLING DOCUMENT (VF01)
    Debit  →  Accounts Receivable (AR)       (Customer owes money)
    Credit →  Revenue Account               (Revenue recognized)

INCOMING PAYMENT (F-28)
    Debit  →  Bank / Cash Account            (Payment received)
    Credit →  Accounts Receivable (AR)       (Open item cleared)
```

---

## Conclusion

This project demonstrates a complete SAP SD Order-to-Cash cycle — from organizational structure setup and master data (XD01, MM01) through inquiry and quotation (VA11/VA21), sales order (VA01), ATP check (CO09), outbound delivery with PGI (VL01N), billing (VF01), to final payment clearing (F-28).

The interaction between SAP SD, MM, FI, and WM modules highlights SAP's capability to transform traditionally fragmented manual processes into a unified, real-time, and audit-ready framework — a core competency developed through the SAP Data/Analytics Engineer program at KIIT.

---

*Capstone Project — KIIT University | 2025–26 | SAP Data / Analytics Engineer Program*
