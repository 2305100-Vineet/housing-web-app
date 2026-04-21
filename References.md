# References & Resources

**Project:** SAP SD — Order-to-Cash (O2C) Capstone Project
**Student:** Vineet Kumar Jha | Roll No: 2305100 | KIIT University | 2025–26

---

## YouTube References

| # | Description | Link |
|---|-------------|------|
| 1 | SAP SD Order-to-Cash (O2C) Full Process Walkthrough | https://youtu.be/r3bqbqIR5FI |
| 2 | SAP SD End-to-End Sales Cycle Tutorial | https://youtu.be/ZRmtgo_84aQ |
| 3 | SAP SD Complete Tutorial Playlist | https://youtube.com/playlist?list=PLLvAEtvfPC9i4zylwZNMIIClhIiERbIVc |

---

## Official SAP Documentation

| Resource | Link |
|----------|------|
| SAP Help Portal (Main) | https://help.sap.com |
| SAP SD — Sales and Distribution | https://help.sap.com/docs/SUPPORT_CONTENT/sd/3362915062.html |
| SAP SD — Introduction & Overview | https://help.sap.com/docs/SUPPORT_CONTENT/abap/3353523547.html |
| SAP S/4HANA — List of SD Documents | https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/0e1db853dcfcb44ce10000000a174cb4.html |
| SAP Community Network | https://community.sap.com |
| SAP Learning Hub | https://learning.sap.com |
| openSAP — Free Courses | https://open.sap.com |

---

## Academic & Course References

| Reference | Details |
|-----------|---------|
| KIIT SAP Project Work Guidance | Internal course document — SAP Data/Analytics Engineer Program, KIIT University, 2025–26 |
| Capstone Project Submission Guidelines V2 | Internal guidelines document — KIIT University, April 2026 |
| SAP Project Helper Document | Trainer-shared reference document — SAP SD O2C module, KIIT, 2026 |

---

## Online Knowledge Bases

| Resource | URL |
|----------|-----|
| GURU99 — SAP SD Free Course | https://www.guru99.com/free-sap-sd-training-course.html |
| GURU99 — What is SAP SD | https://www.guru99.com/sap-sd-introduction.html |
| Tutorialspoint — SAP SD Home | https://www.tutorialspoint.com/sap_sd/index.htm |
| Tutorialspoint — SAP SD Sales Order Processing | https://www.tutorialspoint.com/sap_sd/sap_sd_sales_order_processing.htm |
| Tutorialspoint — SAP SD Creation of Sales Order | https://www.tutorialspoint.com/sap_sd/sap_sd_creation_sales_order.htm |
| Tutorialspoint — SAP SD Sales Order Types | https://www.tutorialspoint.com/sap_sd/sap_sd_sales_order_types.htm |

---

## Key Concepts Referenced

| Concept | Description | Used In |
|---------|-------------|---------|
| Document Flow | Linked chain — Inquiry → Quotation → Sales Order → Delivery → Invoice → Payment | All Steps |
| ATP (Available-to-Promise) | Real-time stock check against confirmed demands to commit a delivery date | CO09 — Step 5 |
| Post Goods Issue (PGI) | Inventory reduction + automatic COGS posting in FI triggered by delivery | VL02N — Step 6 |
| Pricing Condition Technique | Framework for applying discounts, surcharges, and taxes using condition records | VA01 — Step 4 |
| Output Determination | Framework for auto-generating and sending invoice PDFs to customers | VF01 — Step 7 |
| Credit Management | Automated credit limit check at sales order to block high-risk customers | VA01 — Step 4 |
| Incoterms | International trade terms defining delivery responsibility (CIF, FOB, EXW) | VA01 — Step 4 |
| Days Sales Outstanding (DSO) | KPI measuring average days taken to collect payment after invoice | VF01 + F-28 |
| BAPI / IDOC | SAP interfaces for integrating external systems with SAP SD | Integration layer |

---

## Full T-Code Reference

| T-Code | Full Name | Module |
|--------|-----------|--------|
| XD01 | Create Customer Master | SD / FI |
| XD02 | Change Customer Master | SD / FI |
| XD03 | Display Customer Master | SD / FI |
| MM01 | Create Material Master | MM |
| VA11 | Create Inquiry | SD |
| VA21 | Create Quotation | SD |
| VA01 | Create Sales Order | SD |
| VA02 | Change Sales Order | SD |
| VA03 | Display Sales Order | SD |
| CO09 | Availability Overview (ATP) | SD / MM |
| VL01N | Create Outbound Delivery | SD / WM |
| VL02N | Change Delivery / Post Goods Issue | SD / MM / FI |
| VF01 | Create Billing Document | SD / FI |
| VF02 | Change Billing Document | SD / FI |
| VF03 | Display Billing Document | SD / FI |
| F-28 | Post Incoming Payment | FI |
| FBL5N | Customer Line Items Report | FI |
| VL06O | Outbound Delivery Monitor | SD |

---

## Project Files Index

| File | Description |
|------|-------------|
| `2305100_Vineet_O2C_Capstone_Project_Report.pdf` | Complete Capstone Project Report — 5 pages |
| `O2C_Process_Flow_Diagram.png` | O2C process flow cover diagram |
| `Screenshots/XD01_Customer_Master.png` | SAP XD01 Customer Master screenshot |
| `Screenshots/MM01_Material_Master.png` | SAP MM01 Material Master screenshot |
| `Screenshots/VA01_Sales_Order.png` | SAP VA01 Sales Order screenshot |
| `Screenshots/CO09_ATP_Check.png` | SAP CO09 ATP Availability Overview screenshot |
| `Screenshots/VL01N_Delivery.png` | SAP VL01N Outbound Delivery screenshot |
| `Screenshots/VF01_Billing.png` | SAP VF01 Billing Document screenshot |
| `README.md` | Project overview and full documentation |
| `References.md` | All references and resources used |

---

*Capstone Project — KIIT University | 2025–26 | SAP Data / Analytics Engineer Program*
