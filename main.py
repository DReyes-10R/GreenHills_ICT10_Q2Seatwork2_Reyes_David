from pyscript import document

def calc_gwa(e=None):
    first = document.getElementById("first_name").value
    last = document.getElementById("last_name").value

    
    def to_float(idname):
        try:
            return float(document.getElementById(idname).value)
        except:
            return 0.0


    science = to_float("g_science")
    math = to_float("g_math")
    english = to_float("g_english")
    filipino = to_float("g_filipino")
    ict = to_float("g_ict")
    pe = to_float("g_pe")

    total = science + math + english + filipino + ict + pe
    average = total / 6

    # IF–ELSE conditional statement
    if average > 74:
        remark = "PASSED"
    else:
        remark = "FAILED"

   
    document.getElementById("name_out").innerText = f"{first} {last}"
    document.getElementById("summary_out").innerText = (
        f"Science: {science}"
        f"Math: {math}"
        f"English: {english}"
        f"Filipino: {filipino}"
        f"ICT: {ict}"
        f"PE: {pe}"
    )
    document.getElementById("gwa_out").innerText = (
        f"Your General Weighted Average (GWA) is: {average:.2f}"
        f"Status?: {remark}"
    )
