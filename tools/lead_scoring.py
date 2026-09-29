def score_lead(
    company_size: int,
    has_website: bool,
    has_email: bool,
) -> dict:
    score = 0

    if company_size >= 10:
        score += 40

    if has_website:
        score += 20

    if has_email:
        score += 40

    if score >= 80:
        category = "high"
    elif score >= 50:
        category = "medium"
    else:
        category = "low"

    return {
        "score": score,
        "category": category,
    }