** 1. and 4. Learning Outcomes: We will begin by creating the project structure. For replication, change the initial link with your personal one.

local exam "C:/Users/Ierima_Alin/Desktop/ierima_exam"

mkdir "`exam'"
mkdir "`exam'/raw"
mkdir "`exam'/clean"
mkdir "`exam'/graphs"

**For the next step, we import the raw data from my Github.
local raw "C:/Users/Ierima_Alin/Desktop/ierima_exam/raw"
import excel "https://raw.githubusercontent.com/ierimalin/CFE---Exam-/main/ierima_exam/raw/globalterrorismdb_2021Jan-June_1222dist.xlsx", firstrow clear
export excel "`raw'/globalterrorismdb_2021Jan-June.xlsx", firstrow(variables) replace
import delimited "https://raw.githubusercontent.com/ierimalin/CFE---Exam-/main/ierima_exam/raw/tjet_cy.csv", clear
export delimited "`raw'/tjet_cy.csv", replace


**5. and 6. Data quality checks in Stata. I will split this so that we check GTD data in Stata, and then check TJET data in Python.

cd ierima_exam/raw
import excel "globalterrorismdb_2021Jan-June.xlsx", firstrow clear

describe
misstable summarize

keep eventid iyear country_txt nkill

describe nkill
recast int nkill

**Collapse data so I can get the totla kills per country per year, saved as nkill_total. Transformations, filtering by obs and variables.

collapse (sum) nkill_total=nkill, by(country_txt iyear)
keep if iyear == 2021
keep if nkill_total > 0
save "C:/Users/Ierima_Alin/Desktop/ierima_exam/clean/gtd_aggregated.dta", replace

**8. Summary statistics table

summarize nkill_total, detail
tabstat nkill_total, statistics(mean median sd min max count) columns(statistics)

**9. Graph creation
sort nkill_total
gen rank = _n
keep if rank > _N-5
drop rank

graph hbar nkill_total, over(country_txt) title("Top 5 Countries with Most Terrorist Killings in 2021")

