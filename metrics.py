from jiwer import cer, wer

def calculate_metrics(reference, hypothesis):
    """
    Calculate OCR performance metrics.
    reference: Ground truth text
    hypothesis: OCR output text
    """
    ref = reference.strip()
    hyp = hypothesis.strip()
    
    if not ref and not hyp:
        return {"cer": 0.0, "wer": 0.0, "accuracy": 1.0}
    if not ref:
        return {"cer": 1.0, "wer": 1.0, "accuracy": 0.0}
    if not hyp:
        return {"cer": 1.0, "wer": 1.0, "accuracy": 0.0}

    try:
        char_error = cer(ref, hyp)
        word_error = wer(ref, hyp)
        # Simple accuracy heuristic
        accuracy = max(0, 1 - char_error)
        
        return {
            "cer": round(char_error, 4),
            "wer": round(word_error, 4),
            "accuracy": round(accuracy, 4)
        }
    except Exception:
        return {"cer": 1.0, "wer": 1.0, "accuracy": 0.0}

def get_metrics_definitions_md():
    """Returns markdown formatted definitions for metrics."""
    return (
        "### Metric Definitions\n"
        "- **CER (Character Error Rate)**: The ratio of character-level errors (insertions, deletions, substitutions) to the total number of characters in the reference. Lower is better (0.0 is perfect).\n"
        "- **WER (Word Error Rate)**: The ratio of word-level errors to the total number of words in the reference text. Faster way to judge readability.\n"
        "- **Accuracy**: Derived as `1 - CER`, representing the percentage of correctly recognized characters.\n"
    )
